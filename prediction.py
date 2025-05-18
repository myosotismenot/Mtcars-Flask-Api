import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("mtcars.csv")

data = data.drop("model", axis=1)
X = data.drop(["mpg", "vs", "am"], axis=1)
y = data["mpg"]

model = LinearRegression().fit(X,y)

def mpg_prediction(dict_values, model=model):
	inputs = pd.DataFrame([dict_values])
	prediction = model.predict(inputs)[0]
	return prediction

