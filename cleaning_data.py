import pandas as pd

brown_dwarf_data = pd.read_csv("brown_dwarf_data.csv")
brown_dwarf_data = brown_dwarf_data.dropna()
print(brown_dwarf_data)

brown_dwarf_data["Mass"] = brown_dwarf_data["Mass"].astype(float)
brown_dwarf_data["Radius"] = brown_dwarf_data["Radius"].astype(float)

brown_dwarf_data["Mass"] = brown_dwarf_data["Mass"]*0.000954588
brown_dwarf_data["Radius"] = brown_dwarf_data["Radius"]*0.102763

brown_dwarf_data.to_csv("star_data.csv")