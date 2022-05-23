from dataclasses import dataclass
from itertools import combinations
from typing import Counter

import pandas as pd
import pyvis
from rich import print
from rich.progress import track


@dataclass
class Node:
    drug_name: str
    category: str


@dataclass
class GraphData:
    src_drug: str
    dest_drug: str


df: pd.DataFrame = pd.read_csv("./drugs_wide.csv")  # type: ignore

print(df.head())


combos: list[tuple[str, str]] = []

columns: list[str] = list(df.columns)

for i, row in track(df.iterrows(), total=df.shape[0], transient=True):
    row_drugs: list[str] = []
    for col in columns:
        if row[col] == 1:
            row_drugs.append(col)

    drug_data: list[tuple[str, str]] = []
    for drug in row_drugs:
        if drug.endswith("_primary"):
            category = "primary"
        elif drug.endswith("_secondary"):
            category = "secondary"
        else:
            print(f"Drug name does not end with correct value: {drug}")
            continue

        drug_name = drug.removesuffix("_primary").removesuffix("_secondary")
        drug_data.append((drug_name, category))

    combos.extend(drug_data)


counts = Counter(combos)
print(counts.most_common(10))
