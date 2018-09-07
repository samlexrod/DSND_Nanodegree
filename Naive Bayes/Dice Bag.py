import pandas as pd

standard_six = [1, 2, 3, 4, 5, 6]*3
non_standard_six = [2, 3, 3, 4, 4, 5]*2

standard_isthree = standard_six.count(3)
non_standard_isthree = non_standard_six.count(3)

bag = {'DiceType': ['standard', 'non-standard'], 'Side_Count': [6*3, 6*2],
       'IsThree': [standard_isthree, non_standard_isthree]}

print(bag)


df = pd.DataFrame(bag)

print(df)

df['DiceType_Prob'] = df.Side_Count / df.Side_Count.sum()

print(df)

df['IsThree_Prob'] = df.IsThree / df.Side_Count

print(df)

df['IsThree_Given_Type'] = df.DiceType_Prob * df.IsThree_Prob

print(df)

df['posterior_prob'] = df['IsThree_Given_Type'] / df['IsThree_Given_Type'].sum()

print(df)

