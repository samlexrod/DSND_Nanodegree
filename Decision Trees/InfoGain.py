import pandas as pd
import numpy as np

df = pd.read_csv('https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5ad940f6_ml-bugs/ml-bugs.csv')

#print(df[df['Length (mm)'] < 17].groupby(['Species']).count())
#print(df[df['Length (mm)'] < 20].groupby(['Species']).count())
#print(df[df.Color == 'Brown'].groupby(['Species']).count())
#print(df[df.Color == 'Blue'].groupby(['Species']).count())
#print(df[df.Color == 'Green'].groupby(['Species']).count())
# using Length < 17 for the information gain code
# slicing dataset
 
#df = df.loc[:, ['Species', 'Length (mm)']]
df.rename(index=str, columns={'Length (mm)':'Length_mm'}, inplace=True)

df['Length_mm_group'] = df['Length_mm'] < 17
df.Length_mm_group.replace(True, '0-16', inplace=True)
df.Length_mm_group.replace(False, '17+', inplace=True)

df_species_count = df[df.Length_mm_group == '0-16'].groupby('Species')['Species'].count()

columns = ['Color', 'Length_mm_group']
interest = 'Species'

"""
# Testing with Recommending Apps
apps_dict = {'Gender': ['F','F','M','F','M','M'], 
             'Occupation': ['Study','Work','Work','Work','Study','Study'],
              'App': ['P','W','S','W','P','P']}

df = pd.DataFrame(apps_dict)
columns = ['Occupation', 'Gender']
interest = 'App'
"""

def entropy(df, columns, interest):
    print('\nData:', interest)
    print('Data_value:', interest, '\n', '*'*10)

    # count and proportion
    df_parentcount = (df.groupby(interest)[interest].count())
    df_parentprop = (df_parentcount/df_parentcount.sum())

    # entropy
    parent_indEntropy = ((-1*df_parentprop)*np.log2(df_parentprop))
    parent_Entropy = parent_indEntropy.sum()

    print('Parent Entropy:', parent_Entropy)

    print('- - '*30)
    for column in columns:
        child_entropy = []
        for column_value in df[column].unique():
            print('\nData:', column)
            print('Data_value:', column_value, '\n', '*'*10)

            # count and proportion
            df_childcount = (df[df[column] == column_value].groupby(interest)[interest].count())
            df_childprop = (df_childcount/df_childcount.sum())

            # entropy
            childvalue_indEntropy = ((-1*df_childprop)*np.log2(df_childprop))
            childvalue_Entropy = childvalue_indEntropy.sum()
            
            print('{} {} Entropy:'.format(column, column_value), childvalue_Entropy)
            child_entropy.append(childvalue_Entropy)

        child_entropy = np.array(child_entropy)
        print('{} Information Gain:'.format(column), parent_Entropy-child_entropy.mean())

        print('_'*20)
    print('- - '*30)

entropy(df, columns, interest)
