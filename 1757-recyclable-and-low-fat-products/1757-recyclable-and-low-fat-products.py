import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    rdf=products[(products['low_fats']=='Y') & (products['recyclable']=='Y')]
    return rdf[['product_id']]