import pandas as pd

matrix_labels = ['TruePositive', 'TrueNegative', 'FalsePositive', 'FalseNegative']
predictions = [6, 5, 2, 1]

predictions = ([[x] for x in predictions])

print(predictions)

dict = dict(zip(matrix_labels, predictions))

print(dict)

df = pd.DataFrame(dict)

print(df)


accuracy = (df.TruePositive.sum() + df.TrueNegative.sum()) / df.sum().sum()
precision = (df.TruePositive.sum() / (df.TruePositive.sum() + df.FalsePositive.sum()))
recall = (df.TruePositive.sum() / (df.TruePositive.sum() + df.FalseNegative.sum()))
harmonic = (2 * (precision * recall)/(precision + recall))


beta = 0.5
harmonic_beta = ((1 + beta**2) * (precision * recall)/((beta**2*precision) + recall))

print('Accuracy: {:2.2%}'.format(accuracy))
print('Precision: {:2.2%}'.format(precision))
print('Recall: {:2.2%}'.format(recall))
print('F1 Score or Harmonic Mean: {:2.2%}'.format(harmonic))


print(2 * (0.556 * 0.833)/(0.556 + 0.833))






