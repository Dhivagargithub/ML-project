import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
import pickle
data = pd.read_csv('loan_data.csv')  # Ensure you have a dataset named 'loan_data.csv'
data.fillna(method='ffill', inplace=True)  # Fill missing values
features = ['age', 'income', 'loan_amount', 'credit_score']
target = 'loan_approved'
X = data[features]
y = data[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
model = LogisticRegression()
model.fit(X_train, y_train)
with open('loan_model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
accuracy, conf_matrix
