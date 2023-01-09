import pandas as pd

list = [["Apple", "Red"], ["Banana", "Yellow"], ["Orange","Orange"], ["Guava","Green"]]

mydataframe = pd.DataFrame(list, columns = ['Fruits', 'Colour'])
print(mydataframe)