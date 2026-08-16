import pandas as PD
import matplotlib.pyplot as plt


party = [
    {"name":"pikachu", "atk":56, "def": 69},
    {"name":"aggron", "atk":78, "def": 210},
    {"name":"garchomp", "atk":110, "def": 75}
]

df = PD.DataFrame(party)
"""
print(df)
print(df.sort_values("atk", ascending=False))
print(df["def"].mean())
print(df["atk"].max())"""

plt.figure(figsize=(8,5))
plt.bar(df["name"], df["atk"])
plt.ylabel("attack")
plt.title("Pokemon attack comparison")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("chart.png")
plt.close()