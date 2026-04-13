import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    # Count unique students per class
    grouped = courses.groupby("class")["student"].nunique().reset_index()
    
    # Filter classes with at least 5 students
    result = grouped[grouped["student"] >= 5]
    
    # Return only class column
    return result[["class"]]
    