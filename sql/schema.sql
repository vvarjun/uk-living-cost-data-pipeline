CREATE TABLE dim_region (
                            region_id INTEGER PRIMARY KEY,
                            region_name VARCHAR(100)
);

CREATE TABLE fact_living_cost (
                                  cost_id INTEGER PRIMARY KEY,
                                  region_id INTEGER,
                                  year INTEGER,
                                  avg_rent DECIMAL(10,2),
                                  avg_salary DECIMAL(10,2),
                                  food_cost DECIMAL(10,2),
                                  transport_cost DECIMAL(10,2),
                                  total_monthly_cost DECIMAL(10,2),
                                  annual_living_cost DECIMAL(10,2),
                                  affordability_ratio DECIMAL(5,2),
                                  net_migration INTEGER,
                                  FOREIGN KEY (region_id) REFERENCES dim_region(region_id)
);