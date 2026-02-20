# Instructions

## Input Files

To run an O2 sweep, you will need the following files:
1. `chem.inp` - The Chemkin mechanism
2. `thermo.dat` - The Chemkin thermochemistry data
3. `species.csv` - A CSV file matching species to their Chemkin names (see format below)
4. `concentrations.csv` - A CSV file giving the relative concentrations of oxygen, nitrogen, and fuel (see format below)

### CSV File Formats

You can create a CSV file from an Excel spreadsheet by clicking "Save as" and selecting "CSV" from the dropdown menu. There may be multiple "CSV" options, any of which will work.

#### The `concentrations.csv` file

_Format_:
|	O2 |	N2 |	fuel |
| --- | --- | --- |
|	0.0058 |	0.9891 |	0.005 |
|	0.0116 |	0.9833 |	0.005 |
|	... |	... |	... |

These columns give the relative concentrations of molecular oxygen, molecular nitrogen, and fuel.
Your final results will be added as columns to this table.
You can include additional columns, such as a **phi** column, that will also be included in your results table.

#### The `species.csv` file

_Format_:
|species	| name |
| --- | --- |
|	O2 |	O2(6) |
|	N2 |	N2 |
|	fuel |	C5H8(522) |
| ... | ... |
| water | H2O(5) |
| oxygen | O2(6) |
| ... | ... |

The **name** column gives the Chemkin name of each species as used in `chem.inp` and `thermo.dat`.

For the first three rows, keep the values in the **species** column as-is and enter the Chemkin names of oxygen, nitrogen, and your fuel in the **name** column.
These three columns will be used to set concentrations as identified in your `concentrations.csv` file above.

For the remaining rows, fill in the **species** column with an arbitrary common name of your choice, such as "water", and give the corresponding Chemkin name of each species in the **name** column.
Do this for every species that you want to extract data for.
The values in your **species** column will be used as column labels in your final results table.

