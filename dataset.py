import pandas as pd
data = {
    'age': [22, 23, 24, 25, 26],
    'income': [25000, 40000, 60000, 50000, 30000],
    'loan_amount': [5000, 15000, 20000, 10000, 7000],
    'credit_score': [650, 700, 750, 680, 690],
    'loan_approved': [1, 1, 0, 1, 0]  #1=Approved,0=Denied
}
df = pd.DataFrame(data)
df.to_csv('loan_data.csv', index=False)
print("Since i dont have data set i created 'loan_data.csv' with small datas")
