import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

df = pd.read_csv('house_prices_dataset.csv')

X = df[['Size_sqft','Bedrooms','Age_years']]
y = df['Price']

regressor_model = LinearRegression()
regressor_model.fit(X,y)

pickle.dump(regressor_model, open('regressor_model.pkl', 'wb'))