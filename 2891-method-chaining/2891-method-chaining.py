import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    result = animals.query('weight > 100')
    result = result.sort_values('weight', ascending = False)
    result = result.drop(columns = ['species', 'age', 'weight'])
    return result