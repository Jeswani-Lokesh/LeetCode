import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Merge customers with orders using left join
    merged = customers.merge(
        orders,
        how="left",
        left_on="id",
        right_on="customerId"
    )
    
    # Keep only rows where order id is null
    result = merged[merged["customerId"].isna()]
    
    # Return only customer names
    return result[["name"]].rename(columns={"name": "Customers"})
    