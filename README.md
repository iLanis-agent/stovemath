# Stove Math

Honest camp-stove arithmetic. The box claims a three-minute boil; Stove Math multiplies, divides
and tells you whether the canister sees day six.

## What it does

Three panels of hypothetical arithmetic on labeled norms:

- **The boil truth** - liters times claimed minutes per liter: the honest wait.
- **The canister truth** - fuel grams vs. the burn norm: the honest boil count.
- **The trip truth** - hot meals over the trip vs. the boils you carry: spare, tight, or pack a second.

## The boundary

Stove Math keeps boil-time, fuel and meal arithmetic only. Every burn figure is a labeled norm,
not a promise - wind, altitude, cold and pot lid change real burns. Follow the stove's manual,
never use it in a tent, and pack fuel for the weather you might get. Every figure is hypothetical
arithmetic on labeled norms, not a statement about any real stove or canister.

## Files

- `index.html` - landing page
- `app.html` - the app
- `engine.js` - the arithmetic (shared by the page and the tests)
- `oracle.py` - a Python mirror of the engine, float for float
- `expected.json` - oracle output for its inline cases
- `test.js` - runs the engine against `expected.json`

## Test

```
python3 oracle.py   # regenerates expected.json from its inline cases
node test.js        # 25 cases / 25 checks
```

Live at https://ilanis-agent.github.io/stovemath/
