import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score

from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

def make_model(model, x_train, y_train):
    return model.fit(x_train, y_train)

def all_models(x_train, x_test, y_train, y_test, 
               objects = [LinearRegression(fit_intercept=False), 
                          Pipeline([('ss', StandardScaler()), ('knn', KNeighborsRegressor())]), 
                          DecisionTreeRegressor(),
                          RandomForestRegressor(), 
                          XGBRegressor(), 
                          ],
               index = ['Linear Regression', 'K-Nearest Neighbors', 'Decision Tree', 
                        'Random Forest', 'XGBoost']
               
              ):
    models = []
    rmse = []
    rsquared = []

    for i, o in enumerate(objects):
        models.append(make_model(o, x_train, y_train))
        print(f'{index[i]} model fit...')
        
    for i in models:
        prediction = i.predict(x_test)
        rmse.append(mean_squared_error(y_test, prediction, squared=False))
        rsquared.append(r2_score(y_test, prediction))
    df = pd.DataFrame(np.array([rmse, rsquared]).T, 
                      index = index, columns = ['RMSE', 'R-Squared'])
    display(df)

    return models

def plot_importances(model, vectorizer, title='Feature Importances'):
    importances = sorted(list(zip(model.feature_importances_, vectorizer.get_feature_names())))[-20:]
    plot = pd.DataFrame(importances, columns=['Importance', 'Feature'])
    
    fig, ax = plt.subplots(figsize=(15, 8))
    sns.barplot(data=plot, y=plot.index, x=0)
    ax.set_title(title)
    ax.set_xlabel('Importance')
    ax.set_ylabel('Feature')
    plt.show();