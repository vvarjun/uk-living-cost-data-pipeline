import pandas as pd
import matplotlib.pyplot as plt
def run_quality_checks(path):
    df = pd.read_csv(path)

    assert df.isnull().sum().sum() == 0, "Missing values found"
    assert (df["avg_salary"] > 0).all(), "Invalid salary values"
    assert (df["avg_rent"] > 0).all(), "Invalid rent values"

    df.plot(x="region", y="affordability_ratio", kind="bar")
    plt.title("Affordability Ratio by Region")
    plt.savefig("dashboards/affordability.png")
    print("Data quality checks passed")

if __name__ == "__main__":
    run_quality_checks("data/processed/living_cost_processed.csv")