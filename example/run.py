from pathlib import Path

import cantera
import polars
from cantera.ck2yaml import Parser

from cantera_helper import reactors

out_file = "results.csv"
conc_file = "concentration.csv"  # Concentrations spreadsheet
ck_mech_file = "full_cyclopentane_chem.inp"  # Mechanism
ct_mech_file = Path(ck_mech_file).with_suffix(".yaml")
temp_k = 825  # Temperature (K)
pres_atm = 1.1  # Pressure (atm)
tau_s = 4  # Residence time (s)
vol_cm3 = 1  # Volume (cm^3)
species = [  # Species to save results for
    "CPT(563)",
    "O2(6)",
    "N2",
    "H2(2)",
    "H2O(5)",
    "CO(12)",
    "CO2(13)",
    "CH4(33)",
    "CH3CHO(41)",
    "C2H4(52)",
    "C3H6(131)",
    "C3H4O(165)",
    "C4H6(227)",
    "C4H8(253)",
    "C5H6(478)",
    "C5H8(522)",
    "C5H8O(825)",
    "C6H6(970)",
    "HO2(8)",
    "OH(4)",
]
gather_every = 15  # Gather every nth concentration for testing

# Read in concentrations and select appropriate columns
print("\nReading in concentrations...")
conc_df = polars.read_csv(conc_file)
concs = conc_df.select("CPT(563)", "N2", "O2(6)").rows(named=True)
print(conc_df)

# Read in ChemKin mechanism and convert to Cantera
print("\nConverting ChemKin mechanism to Cantera YAML...")
Parser.convert_mech(ck_mech_file, out_name=ct_mech_file)


# Load mechanism and set initial conditions
print("\nDefining model and conditions...")
model = cantera.Solution(ct_mech_file)
pres_atm *= cantera.one_atm  # convert to Pa from atm
vol_cm3 *= (1e-2) ** 3  # convert to m^3 from cm^3


# Run simulations for each point and store the results in an array
print("\nRunning simulations...")
solns = cantera.SolutionArray(model)
for conc in concs:
    print(f"Starting simulation for {conc}")
    reactor = reactors.jsr(
        model=model, temp=temp_k, pres=pres_atm, tau=tau_s, vol=vol_cm3, conc=conc
    )
    solns.append(reactor.thermo.state)

# Extract results
print("\nExtracting results...")
sim_df = conc_df.with_columns(
    polars.Series(s, solns(s).X.flatten() * 10**6) for s in species
)
print(sim_df)
sim_df.write_csv(out_file)