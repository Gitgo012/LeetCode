import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    diabetic_patients=patients[patients['conditions'].str.contains(r'(^|\s)DIAB1', na=False)]
    return diabetic_patients