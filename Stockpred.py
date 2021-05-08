# -*- coding: utf-8 -*-
"""
Created on Sat May  8 16:09:37 2021

@author: JOKER
"""
import pandas as pd
import numpy as np
import investpy
from datetime import datetime, date

# start date should be within 5 years of current date according to iex API we have used
# The more data we have, the better results we get!


# use your token in place of token which you will get after signing up on IEX cloud
# Head over to https://iexcloud.io/ and sign-up to get your API token
#df = get_historical_data("AAPL", start=start, end=end, output_format="pandas", token="your_token")

df = investpy.get_stock_historical_data(stock='ITC',
                                        country='India',
                                        from_date='01/01/2019',
                                        to_date='01/01/2020')
print(df.head())



from sklearn.model_selection import train_test_split

prices = df[df.columns[0:1]]
prices.reset_index(level=0, inplace=True)
prices["timestamp"] = pd.to_datetime(prices.Date).astype(np.int64) // (10**9)
prices = prices.drop(['Date'], axis=1)
prices

dataset = prices.values
X = dataset[:,1].reshape(-1,1)
Y = dataset[:,0:1]

validation_size = 0.15
seed = 7

X_train, X_validation, Y_train, Y_validation = train_test_split(X, Y, test_size=validation_size, random_state=seed)
print(prices)






from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR

# Test options and evaluation metric
num_folds = 10
seed = 7
scoring = "r2"

# Spot-Check Algorithms
models = []
models.append((' LR ', LinearRegression()))
models.append((' LASSO ', Lasso()))
models.append((' EN ', ElasticNet()))
models.append((' KNN ', KNeighborsRegressor()))
models.append((' CART ', DecisionTreeRegressor()))
models.append((' SVR ', SVR()))




from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

# evaluate each model in turn
results = []
names = []
for name, model in models:
    kfold = KFold(n_splits=num_folds, random_state=seed, shuffle=True)
    cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
    # print(cv_results)
    results.append(cv_results)
    names.append(name)
    msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
    print(msg)
    
    
    
    




# Future prediction, add dates here for which you want to predict
dates = ["2020-12-23", "2020-12-24", "2020-12-25", "2020-12-26", "2020-12-27",]
#convert to time stamp
for dt in dates:
  datetime_object = datetime.strptime(dt, "%Y-%m-%d")
  timestamp = datetime.timestamp(datetime_object)
  # to array X
  np.append(X, int(timestamp))

from matplotlib import pyplot as plt
from sklearn.metrics import mean_squared_error

# Define model
model = DecisionTreeRegressor()
# Fit to model
model.fit(X_train, Y_train)
# predict
predictions = model.predict(X)
print(mean_squared_error(Y, predictions))

# %matplotlib inline 
fig= plt.figure(figsize=(24,12))
plt.plot(X,Y)
plt.plot(X,predictions)
plt.show()

















