import numpy as np
import csv
import pdb
import pandas as pd

head = ["engine", "month", "noise", "egt", "ff", "n1", "n2", "fp_noise", "fp_egt", "fp_ff", "fp_n1", "fp_n2", "failure_prob"]

prev_noise = 0
prev_egt = 0
prev_ff = 0
prev_n1 = 0
prev_n2 = 0

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

for num in range(1, 11):

    rand_month_noise = np.random.randint(1, 31)
    rand_month_egt = np.random.randint(1, 31)
    
    range_noise = np.random.uniform(0.15, 0.8, size=59)
    range_egt = np.random.randint(40, 45, size=59) 
    range_ff = np.random.randint(37, 42, size=59)
    range_n1 = np.random.randint(99, 106, size=59)
    range_n2 = np.random.randint(102, 106, size=59)
    
    cum_range_noise = np.cumsum(range_noise)
    cum_range_noise += start_noise
    cum_range_noise = np.insert(cum_range_noise, 0, start_noise)
    cum_range_noise[rand_month_noise:61] = cum_range_noise[rand_month_noise:61] + 2
    
    cum_range_egt = np.cumsum(range_egt)
    cum_range_egt += start_egt
    cum_range_egt = np.insert(cum_range_egt, 0, start_egt)
    
    
    df = pd.DataFrame(columns=head)
    
    df['month'] = np.arange(1, 61)
    df['noise'] = cum_range_noise
    df['engine'] = 1
    
#    df.loc[df['month'] == 1, 'noise'] = start_noise
    df.loc[df['month'] == 1, 'egt'] = start_egt
    df.loc[df['month'] == 1, 'ff'] = start_ff
    df.loc[df['month'] == 1, 'n1'] = start_n1
    df.loc[df['month'] == 1, 'n2'] = start_n2
    
    
    
    
        
        