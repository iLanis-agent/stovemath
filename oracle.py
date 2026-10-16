import math, json

def plural(n, one, many):
    return one if n == 1 else many

def fixed1(x):
    return f"{math.floor(x * 10 + 0.5) / 10:.1f}"

def boil_minutes(liters, claim):
    if not (liters > 0):
        raise ValueError("the liters must be above zero")
    if not (claim > 0):
        raise ValueError("the claimed minutes must be above zero")
    return liters * claim

def boil_truth(liters, claim):
    minutes = boil_minutes(liters, claim)
    if minutes <= 5:
        verdict = "done before the cocoa's missed"
    elif minutes <= 12:
        verdict = "a working wait honestly"
    elif minutes <= 25:
        verdict = "a patient pot honestly"
    else:
        verdict = "start the pot before the sunset"
    return f"The stove claims {claim} minutes a liter; your {liters}-liter pot is {fixed1(minutes)} minutes - {verdict}."

def canister_truth(grams, burn, liters):
    if not (grams > 0):
        raise ValueError("the canister size must be above zero")
    if not (burn > 0):
        raise ValueError("the burn norm must be above zero")
    if not (liters > 0):
        raise ValueError("the liters must be above zero")
    per_boil = burn * liters
    boils = math.floor(grams / per_boil)
    if boils <= 5:
        verdict = "a weekend of boils honestly"
    elif boils <= 15:
        verdict = "a long weekend honestly"
    elif boils <= 40:
        verdict = "a week of coffee honestly"
    else:
        verdict = "a whole season honestly"
    return f"A {grams}-gram canister at the {burn}-gram-per-liter burn norm and {liters}-liter boils is {boils} {plural(boils, 'boil', 'boils')} - {verdict}."

def trip_truth(days, meals, boils):
    if not (days > 0):
        raise ValueError("the days must be above zero")
    if not (meals > 0):
        raise ValueError("the meals must be above zero")
    if not (boils > 0):
        raise ValueError("the canister boils must be above zero")
    needed = days * meals
    if needed * 2 <= boils:
        verdict = "fuel to spare honestly"
    elif needed <= boils:
        verdict = "a tight fit honestly"
    else:
        verdict = "pack a second canister"
    return f"{days} {plural(days, 'day', 'days')} at {meals} hot {plural(meals, 'meal', 'meals')} a day is {needed} {plural(needed, 'boil', 'boils')}; the canister holds {boils} - {verdict}."

FNS = {"boilTruth": boil_truth, "canisterTruth": canister_truth, "tripTruth": trip_truth}

cases = [
 {"fn":"boilTruth","args":[2,3.5]},
 {"fn":"boilTruth","args":[1,3.5]},
 {"fn":"boilTruth","args":[3,3.5]},
 {"fn":"boilTruth","args":[5,3.5]},
 {"fn":"boilTruth","args":[8,3.5]},
 {"fn":"boilTruth","args":[0.5,4]},
 {"fn":"boilTruth","args":[0,3.5]},
 {"fn":"boilTruth","args":[2,0]},
 {"fn":"canisterTruth","args":[230,10,1]},
 {"fn":"canisterTruth","args":[100,10,2]},
 {"fn":"canisterTruth","args":[230,10,1.5]},
 {"fn":"canisterTruth","args":[450,10,1]},
 {"fn":"canisterTruth","args":[110,10,0.5]},
 {"fn":"canisterTruth","args":[40,10,1]},
 {"fn":"canisterTruth","args":[0,10,1]},
 {"fn":"canisterTruth","args":[230,0,1]},
 {"fn":"canisterTruth","args":[230,10,0]},
 {"fn":"tripTruth","args":[4,2,23]},
 {"fn":"tripTruth","args":[1,2,23]},
 {"fn":"tripTruth","args":[7,3,23]},
 {"fn":"tripTruth","args":[10,3,23]},
 {"fn":"tripTruth","args":[2,1,4]},
 {"fn":"tripTruth","args":[0,2,23]},
 {"fn":"tripTruth","args":[4,0,23]},
 {"fn":"tripTruth","args":[4,2,0]}
]

out = []
for c in cases:
    try:
        out.append({"fn": c["fn"], "args": c["args"], "out": FNS[c["fn"]](*c["args"])})
    except ValueError as e:
        out.append({"fn": c["fn"], "args": c["args"], "err": str(e)})
json.dump(out, open("expected.json", "w"), indent=1)
print(f"{len(out)} cases")
