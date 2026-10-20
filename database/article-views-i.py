import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    result=views.loc[(views['author_id']==views['viewer_id']),['author_id']]
    result=result.rename(columns={'author_id':'id'})
    result=result.drop_duplicates()
    result=result.sort_values(by='id')
    return result
    