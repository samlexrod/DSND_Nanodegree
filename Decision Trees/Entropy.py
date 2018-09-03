import numpy as np
from math import log2
import pandas as pd

# entropy is the log of the proportions of items in the list

# grabbing the balls
red_balls = ['red'] * 8
blue_balls = ['blue'] * 3
yellow_balls = ['yellow'] * 2

# putting the balls in the bucket
bucket = red_balls + blue_balls + yellow_balls

# counting the balls in the buckets  
bucket_counts = np.unique(np.array(bucket), return_counts=True)

df_buckets = pd.DataFrame([list(bucket_counts)[1]], columns=list(bucket_counts)[0])


# taking the probabilities
prob_red = list(df_buckets.red / df_buckets.sum().sum())[0]
prob_blue = list(df_buckets.blue / df_buckets.sum().sum())[0]
prob_yellow = list(df_buckets.yellow / df_buckets.sum().sum())[0]


# replacing ball colors with probability values
bucket = np.array([ball.replace('red', str(prob_red)).\
            replace('blue', str(prob_blue)).\
            replace('yellow', str(prob_yellow)) for ball in bucket]).astype(float)

# taking the absolute log of the probabilities
bucket_log2 = np.log2(bucket)*-1

print(bucket)
print(bucket_log2)
print(bucket_log2.sum()/df_buckets.sum().sum())

