import pandas as pd
import numpy as np


url = "https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/chapter-02-car-price/data.csv"
data = pd.read_csv(url)
y = data["price"]

x = data.drop(["price"])