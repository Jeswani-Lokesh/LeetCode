import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:



    # Filter rows where:
    # area is greater than or equal to 3,000,000
    # OR population is greater than or equal to 25,000,000
    filtered_df = world[
        (world["area"] >= 3000000) | 
        (world["population"] >= 25000000)
    ]
    
    # Select only required columns
    result = filtered_df[["name", "population", "area"]]
    
    # Return final DataFrame
    return result
    