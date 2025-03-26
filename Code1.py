import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split, KFold, cross_val_score

# Load data
data = pd.read_csv("dataset27.csv")
df = pd.DataFrame(data)

def prediction(arr):
    # Extract features and target variable
    X = df.iloc[0:81, 7:16].values
    y = df.iloc[0:81, 18].values
    
    # Standardize the features
    sc = StandardScaler()
    X_scaled = sc.fit_transform(X)
    
    # Split the dataset
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
    
    # Initialize Logistic Regression model
    md = RandomForestClassifier(n_estimators=50, random_state=42)
    
    # Fit the model on the training data
    md.fit(X_train, y_train)
    
    # Perform K-Fold Cross Validation
    kf = KFold(n_splits=20, shuffle=True, random_state=42)
    logregkfold = cross_val_score(md, X_scaled, y, cv=kf)
    
    result = []
    acc = []
    
    for train_index, test_index in kf.split(X_scaled):
        X_train1, X_test1 = X_scaled[train_index], X_scaled[test_index]
        y_train1, y_test1 = y[train_index], y[test_index]
        
        # Fit the model on the K-fold training data
        md.fit(X_train1, y_train1)
        
        # Predict on the K-fold test data
        y_pred = md.predict(X_test1)
        
        # Scale the input array using the same scaler
        arr_scaled = sc.transform(np.array(arr[5:14]).reshape(1, -1))
        
        # Predict the input array
        k = md.predict(arr_scaled)
        result.append(k[0])
        
        # Calculate accuracy for the current fold
        acc_score = accuracy_score(y_test1, y_pred)
        acc.append(acc_score)
    
    print(f"Accuracy scores for each fold: {acc}")
    print(f"Predictions for the input array in each fold: {result}")
    
    # Find the maximum accuracy
    max_acc = max(acc)
     
    print(f"Maximum accuracy: {max_acc}")
    for i in range(len(acc)):
        if acc[i]==max_acc:
            k=i
    if(result[k]==0):
        return "heart"
    if(result[k]==1):
        return "square"
    if(result[k]==2):
        return "round"
    if(result[k]==3):
        return "oval"
             
            