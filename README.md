# Ship Resistance Calculation (Holtrop-Mennen Method)

This project provides a Python script to estimate ship total resistance using a Holtrop-Mennen style empirical approach.

The current implementation is a command-line calculator in `main.py` that asks for hull and operating parameters, computes intermediate coefficients, and prints:

- Total Resistance without Bulbous Bow

## What the script does

The script computes resistance components and combines them into a total value.

Main computed pieces include:

- Froude number and Reynolds number
- Friction coefficient and frictional resistance
- Form-factor related viscous correction
- Wave-making and wave-breaking resistance terms
- Transom-related additional pressure term (computed, but currently excluded from the final sum)
- Model-ship correlation resistance

Final output in code:

- `E60 = E33 * E31 + E37 + E49 + 0 + 0 + E58`

This means the present result intentionally excludes:

- Additional pressure resistance of bulbous bow (`E52`, currently commented out)
- Additional pressure resistance of immersed transom (`E55`, calculated but not added)

## Requirements

- Python 3.8+
- Standard library only (`math`)

No external package installation is required.

## How to run

From the project root:

```bash
python3 main.py
```

Then enter the requested inputs one by one.

## Input parameters

The script prompts for 21 numeric inputs (float). Names below follow the variable names in `main.py`:

1. `E2` - LWL (Length on Waterline)
2. `E3` - LBP (Length Between Perpendiculars)
3. `E4` - Breadth Moulded
4. `E5` - Draught Moulded on F.P
5. `E6` - Draught Moulded on A.P
6. `E7` - Displacement Volume Moulded
7. `E8` - Longitudinal Centre of Buoyancy
8. `E9` - Transverse Bulb Area
9. `E10` - Centre of Bulb Area above keel line
10. `E11` - Midship Section Coefficient
11. `E12` - Waterplane Area Coefficient
12. `E13` - Transom Area
13. `E14` - Wetted Area Appendages
14. `E15` - Stern Shape Parameter
15. `E16` - Propeller Diameter
16. `E17` - Number of Propeller Blades
17. `E18` - Clearance Propeller with keel line
18. `E19` - Ship Speed
19. `E20` - Block Coefficient
20. `E21` - Immersion of Propeller Shaft
21. `E22` - Density in kg/m3

## Output

The script prints a single line:

```text
Total Resistance without Bulbous Bow is : <value>
```

The computed value is in Newtons if your inputs are given in consistent SI units.

## Notes and current limitations

- The script is fully interactive; there are no command-line flags or file input support.
- Some inputs are collected but not currently used in the final resistance expression (`E3`, `E6`, `E8`, `E16`, `E17`, `E18`, `E21`, `E22`).
- Waterline entrance angle term is fixed as `E39 = 1` in the current implementation.
- The script assumes valid numeric input and does not perform input validation.

## Suggested next improvements

- Add input validation and unit checks.
- Add non-interactive mode (arguments or JSON/CSV input).
- Include all enabled resistance components in a selectable final sum.
- Return and display a full breakdown table of component resistances.
- Add automated tests using known benchmark hull data.
