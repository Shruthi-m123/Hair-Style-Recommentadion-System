import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold,cross_val_score
data=pd.read_csv("dataset27.csv")
df=pd.DataFrame(data)
def prediction(arr):
    X=df.iloc[0:81,7:16].values
    y=df.iloc[0:81,18].values
    sc=StandardScaler()
    X_scaled=sc.fit_transform(X)
    X_train,X_test,y_train,y_test=train_test_split(X_scaled,y,test_size=0.2)
    md=LogisticRegression(max_iter=500)
    md.fit(X_train,y_train)
    kf=KFold(n_splits=20,shuffle=True)
    logregkfold= cross_val_score(md, X, y, cv=kf)
    result=[]
    acc=[]
    for train_index, test_index in kf.split(X):
       X_train1, X_test1 = X_scaled[train_index], X_scaled[test_index]
       y_train1, y_test1 = y[train_index], y[test_index]
       md.fit(X_train1, y_train1)
       y_pred = md.predict(X_test1)
       arr_scaled = sc.transform(np.array(arr[5:14]).reshape(1, -1))
       k = md.predict(arr_scaled)
       result.append(k)
       s = accuracy_score(y_test1, y_pred)
       acc.append(s)
    print(acc,result)
    # max_acc=max(acc)
    # max_index=acc.index(max_acc)
    # c1=result.count(0)
    # c2=result.count(1)
    # c3=result.count(2)
    # c4=result.count(3)
    # if c1==max(c1,c2,c3,c4):
    #     return 0
    # if c2==max(c1,c2,c3,c4):
    #     return 1
    # if c3==max(c1,c2,c3,c4):
    #     return 2
    # if c4==max(c1,c2,c3,c4):
    #     return 3
           
    
    