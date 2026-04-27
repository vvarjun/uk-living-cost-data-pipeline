-- Regions with highest affordability pressure
SELECT
    region_name,
    affordability_ratio
FROM fact_living_cost f
         JOIN dim_region r
              ON f.region_id = r.region_id
ORDER BY affordability_ratio DESC;

-- Migration and housing pressure
SELECT
    region_name,
    avg_rent,
    net_migration
FROM fact_living_cost f
         JOIN dim_region r
              ON f.region_id = r.region_id
ORDER BY net_migration DESC;