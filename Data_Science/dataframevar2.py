import pandas as pd
import numpy as np 

list = np.array([[0, 1],[2,3],[4, 5],[6,7]])

mydf = pd.DataFrame(list, columns=['Even', 'Odd'])
print(mydf)