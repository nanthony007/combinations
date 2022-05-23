import pandas as pd

pd.set_option("display.max_columns", None)

df = pd.read_sas("one_encounter_join.sas7bdat", encoding="utf-8")

target_cols = [
    "cohort_new",
    "meth",
    "heroin",
    "buprenorphine",
    "morphine",
    "codeine",
    "cocaine",
    "fentanyl",
    "cannabinoids",
    "amphetamine",
    "caffeine",
    "gabapentin",
    "alprazolam",
    "ketamine",
    "oxycodone",
    "hydrocodone",
    "tramadol",
    "methadone",
]
dff = df[target_cols].copy().fillna(0)

print(dff.head())

# dff.to_csv("stimulink-drugs-wide.csv", index=False)
