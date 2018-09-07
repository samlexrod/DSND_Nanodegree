import numpy as np
import pandas as pd

spam = ['Win money now!', 'Make cash easy!', 'Cheap money, reply']
ham = ['How are you?', 'There you are', 'Can I borrow money', 'Say hi to grandma.', 'Was the exam easy?']

spam_money = [x.find('money')>0 for x in spam].count(True)
ham_money = [x.find('money')>0 for x in ham].count(True)

email = {'Email_Type': ['spam', 'ham'], 
         'Email_count': [len(spam), len(ham)],
         'HaveMoney_count': [spam_money, ham_money] }

df = pd.DataFrame(email)

print(email)

df['Email_Type_Prob'] = df['Email_count']/df['Email_count'].sum()
df['HaveMoney_Prob'] = df['HaveMoney_count']/df['Email_count']
df['HaveMoney_Type_Prob'] = df['Email_Type_Prob'] * df['HaveMoney_Prob'] 
df['HaveMoney_Given_Type_Prob'] = df['HaveMoney_Type_Prob'] / df['HaveMoney_Type_Prob'].sum()

print(df)

print((1/12)/(1/40+1/12))