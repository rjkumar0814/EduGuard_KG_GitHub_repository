from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
df = pd.read_csv(ROOT / "results/predictive_performance_reported.csv")

ax = df.plot(x="model", y="auroc", kind="bar", legend=False)
ax.set_ylabel("AUROC")
ax.set_xlabel("")
ax.set_title("Reported predictive performance")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig(ROOT / "figures/reported_aggregate_auroc.pdf")
plt.close()
