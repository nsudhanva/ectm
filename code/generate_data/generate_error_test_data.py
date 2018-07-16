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

for engine in range(1, 11):

    df = pd.DataFrame(columns=head)
    df['month'] = np.arange(1, 61)
    
    fp_noise = np.zeros(60)
    fp_egt = np.zeros(60)
    fp_ff = np.zeros(60)
    fp_n1 = np.zeros(60)
    fp_n2 = np.zeros(60)
    total_fp = np.zeros(60)
    
    range_noise = np.random.uniform(0.3, 0.35, size=59)
    range_egt = np.random.randint(25, 31, size=59)
    range_ff = np.random.randint(20, 24, size=59)
    range_n1 = np.random.randint(78, 85, size=59)
    range_n2 = np.random.randint(78, 85, size=59)
    
    random_month = np.random.randint(15, 24) 
    random_noise_increase = np.random.uniform(2, 2.5)
    random_egt_increase = np.random.randint(160, 181)
    random_ff_increase = np.random.randint(140, 161)
    random_n1_increase = np.random.randint(350, 371)
    random_n2_increase = np.random.randint(350, 371)
    
    noise = np.cumsum(range_noise) + start_noise
    noise = np.insert(noise, 0, start_noise)
    noise[random_month:] += random_noise_increase
    
    egt = np.cumsum(range_egt) + start_egt
    egt = np.insert(egt, 0, start_egt)
    egt[random_month:] += random_egt_increase
    
    ff = np.cumsum(range_ff) + start_ff
    ff = np.insert(ff, 0, start_ff)
    ff[random_month:] += random_ff_increase
    
    n1 = np.cumsum(range_n1) + start_n1
    n1 = np.insert(n1, 0, start_n1)
    n1[random_month:] += random_n1_increase
    
    n2 = np.cumsum(range_n2) + start_n2
    n2 = np.insert(n2, 0, start_n2)
    n2[random_month:] += random_n2_increase
    
#    noise_index = np.where(noise >= max_noise)[0][0]
#    fp_noise[noise_index: ] = (noise[noise_index:] - max_noise) / 0.06
#    fp_noise = fp_noise/100
#    fp_noise[fp_noise > 1] = 1
#    
#    egt_index = np.where(egt >= max_egt)[0][0]
#    fp_egt[egt_index: ] = (egt[egt_index:] - max_egt) / 6
#    fp_egt = fp_egt/100
#    fp_egt[fp_egt > 1] = 1
#    
#    ff_index = np.where(ff >= max_ff)[0][0]
#    fp_ff[ff_index: ] = (ff[ff_index:] - max_ff) / 5
#    fp_ff = fp_ff/100
#    fp_ff[fp_ff > 1] = 1
#    
#    n1_index = np.where(n1 >= max_n1)[0][0]
#    fp_n1[n1_index: ] = (n1[n1_index:] - max_n1) / 20
#    fp_n1 = fp_n1/100
#    fp_n1[fp_n1 > 1] = 1
#    
#    n2_index = np.where(n2 >= max_n2)[0][0]
#    fp_n2[n2_index: ] = (n2[n2_index:] - max_n2) / 20
#    fp_n2 = fp_n2/100
#    fp_n2[fp_n2 > 1] = 1
#    
#    total_fp = (fp_noise + fp_egt + fp_ff + fp_n1 + fp_n2) / 5
    
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
    df['engine'] = engine
    
    df.to_csv('../../data/test_data/error_test_data_' + str(engine) + '.csv', index=False)
