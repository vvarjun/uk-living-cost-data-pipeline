import pandas as pd


def transform_living_cost_data(input_path: str, output_path: str) -> None:
    df = pd.read_csv(input_path)

    df["total_monthly_cost"] = (
        df["avg_rent"] + df["food_cost"] + df["transport_cost"]
    )

    df["annual_living_cost"] = df["total_monthly_cost"] * 12

    df["affordability_ratio"] = (
        df["annual_living_cost"] / df["avg_salary"]
    ).round(2)

    df["net_migration"] = (
        df["migration_inflow"] - df["migration_outflow"]
    )

    df.to_csv(output_path, index=False)


if __name__ == "__main__":
    transform_living_cost_data(
        "data/raw/living_cost_sample.csv",
        "data/processed/living_cost_processed.csv"
    )