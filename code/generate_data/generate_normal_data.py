import numpy as np
import pdb
import pandas as pd

head = ["engine", "month", "noise", "egt", "ff", "n1", "n2", "fp_noise", "fp_egt", "fp_ff", "fp_n1", "fp_n2", "total_fp"]        

start_noise = 130
start_egt = 1300
start_ff = 5000
start_n1 = 12000
start_n2 = 10000

max_noise = 137
max_egt = 1900
max_ff = 5500
max_n1 = 14000
max_n2 = 12000

fp_noise = np.zeros(60)
fp_egt = np.zeros(60)
fp_ff = np.zeros(60)
fp_n1 = np.zeros(60)
fp_n2 = np.zeros(60)
total_fp = np.zeros(60)

range_noise = np.random.uniform(0.2, 0.24, size=59)
range_egt = np.random.randint(18, 24, size=59) 
range_ff = np.random.randint(16, 19, size=59)
range_n1 = np.random.randint(65, 73, size=59)
range_n2 = np.random.randint(65, 73, size=59)

noise = np.cumsum(range_noise) + start_noise
noise = np.insert(noise, 0, start_noise)

egt = np.cumsum(range_egt) + start_egt
egt = np.insert(egt, 0, start_egt)

ff = np.cumsum(range_ff) + start_ff
ff = np.insert(ff, 0, start_ff)

n1 = np.cumsum(range_n1) + start_n1
n1 = np.insert(n1, 0, start_n1)

n2 = np.cumsum(range_n2) + start_n2
n2 = np.insert(n2, 0, start_n2)

noise_index = np.where(noise >= max_noise)[0][0]
fp_noise[noise_index: ] = (noise[noise_index:] - max_noise) / 0.06
fp_noise = fp_noise/100
fp_noise[fp_noise > 1] = 1

egt_index = np.where(egt >= max_egt)[0][0]
fp_egt[egt_index: ] = (egt[egt_index:] - max_egt) / 6
fp_egt = fp_egt/100
fp_egt[fp_egt > 1] = 1

ff_index = np.where(ff >= max_ff)[0][0]
fp_ff[ff_index: ] = (ff[ff_index:] - max_ff) / 5
fp_ff = fp_ff/100
fp_ff[fp_ff > 1] = 1

n1_index = np.where(n1 >= max_n1)[0][0]
fp_n1[n1_index: ] = (n1[n1_index:] - max_n1) / 20
fp_n1 = fp_n1/100
fp_n1[fp_n1 > 1] = 1

n2_index = np.where(n2 >= max_n2)[0][0]
fp_n2[n2_index: ] = (n2[n2_index:] - max_n2) / 20
fp_n2 = fp_n2/100
fp_n2[fp_n2 > 1] = 1

total_fp = (fp_noise + fp_egt + fp_ff + fp_n1 + fp_n2) / 5

df = pd.DataFrame(columns=head)
df['engine'] = np.ones(60)
df['month'] = np.arange(1, 61)
df['noise'] = noise
df['egt'] = egt
df['ff'] = ff
df['n1'] = n1
df['n2'] = n2
df['fp_noise'] = fp_noise
df['fp_egt'] = fp_egt
df['fp_ff'] = fp_ff
df['fp_n1'] = fp_n1
df['fp_n2'] = fp_n2
df['total_fp'] = total_fp

df.to_csv('../../data/normal_data.csv', index=False)
