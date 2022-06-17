
import pandas as pd
import numpy as np

def Show_difference(y_test, y_pred, n=10):

  dic = {'Actual' : y_test.ravel(),
         'Predicted' : y_pred,
         'Difference' : abs(y_test.ravel()-y_pred)}
  
  df_result = pd.DataFrame(dic).sort_values(by=['Difference']).reset_index(drop=True)

  return df_result.head(n)