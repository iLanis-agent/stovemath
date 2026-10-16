// Stove Math engine - hypothetical arithmetic on labeled norms only.
// Fuel norms are illustrative; wind, altitude and cold change real burns.

function plural(n, one, many) { return n === 1 ? one : many; }

function fixed1(x) { return (Math.floor(x * 10 + 0.5) / 10).toFixed(1); }

function boilMinutes(liters, claim) {
  if (!(liters > 0)) throw new Error("the liters must be above zero");
  if (!(claim > 0)) throw new Error("the claimed minutes must be above zero");
  return liters * claim;
}

function boilTruth(liters, claim) {
  const minutes = boilMinutes(liters, claim);
  let verdict;
  if (minutes <= 5) verdict = "done before the cocoa's missed";
  else if (minutes <= 12) verdict = "a working wait honestly";
  else if (minutes <= 25) verdict = "a patient pot honestly";
  else verdict = "start the pot before the sunset";
  return `The stove claims ${claim} minutes a liter; your ${liters}-liter pot is ${fixed1(minutes)} minutes - ${verdict}.`;
}

function canisterBoils(grams, burn) {
  if (!(grams > 0)) throw new Error("the canister size must be above zero");
  if (!(burn > 0)) throw new Error("the burn norm must be above zero");
  return Math.floor(grams / burn);
}

function canisterTruth(grams, burn, liters) {
  if (!(grams > 0)) throw new Error("the canister size must be above zero");
  if (!(burn > 0)) throw new Error("the burn norm must be above zero");
  if (!(liters > 0)) throw new Error("the liters must be above zero");
  const perBoil = burn * liters;
  const boils = Math.floor(grams / perBoil);
  let verdict;
  if (boils <= 5) verdict = "a weekend of boils honestly";
  else if (boils <= 15) verdict = "a long weekend honestly";
  else if (boils <= 40) verdict = "a week of coffee honestly";
  else verdict = "a whole season honestly";
  return `A ${grams}-gram canister at the ${burn}-gram-per-liter burn norm and ${liters}-liter boils is ${boils} ${plural(boils, "boil", "boils")} - ${verdict}.`;
}

function tripTruth(days, meals, grams, burn, liters) {
  if (!(days > 0)) throw new Error("the days must be above zero");
  if (!(meals > 0)) throw new Error("the meals must be above zero");
  if (!(grams > 0)) throw new Error("the canister size must be above zero");
  if (!(burn > 0)) throw new Error("the burn norm must be above zero");
  if (!(liters > 0)) throw new Error("the liters must be above zero");
  const needed = days * meals;
  const perBoil = burn * liters;
  const boils = Math.floor(grams / perBoil);
  const diff = boils - needed;
  let tail;
  if (diff > 0) tail = `a margin of ${diff} ${plural(diff, "boil", "boils")} on the labeled norms`;
  else if (diff === 0) tail = "no margin at all on the labeled norms";
  else tail = `a deficit of ${-diff} ${plural(-diff, "boil", "boils")} on the labeled norms`;
  return `${days} ${plural(days, "day", "days")} at ${meals} hot ${plural(meals, "meal", "meals")} a day needs ${needed} ${plural(needed, "boil", "boils")}; the canister panel holds ${boils} ${plural(boils, "boil", "boils")} - ${tail}.`;
}

if (typeof module !== "undefined") {
  module.exports = { boilMinutes, boilTruth, canisterBoils, canisterTruth, tripTruth };
}
