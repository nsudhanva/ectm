import numpy as np
import pdb
import pandas as pd
import random

head = ["engine", "month", "noise", "egt", "ff", "n1", "n2", 'act_fp_noise', 'act_fp_egt', 'act_fp_ff', 'act_fp_n1', 'act_fp_n2', 'act_total_fp', "mlr_fp_noise", "mlr_fp_egt", "mlr_fp_ff", "mlr_fp_n1", "mlr_fp_n2", "mlr_total_fp", "dt_fp_noise", "dt_fp_egt", "dt_fp_ff", "dt_fp_n1", "dt_fp_n2", "dt_total_fp", "rf_fp_noise", "rf_fp_egt", "rf_fp_ff", "rf_fp_n1", "rf_fp_n2", "rf_total_fp"]           

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
    
    range_noise = np.random.uniform(np.random.uniform(0.2, 0.5), np.random.uniform(0.5, 1.1), size=59)
    range_egt = np.random.randint(np.random.randint(10, 35), np.random.randint(35, 75), size=59)
    range_ff = np.random.randint(np.random.randint(10, 35), np.random.randint(35, 85), size=59)
    range_n1 = np.random.randint(np.random.randint(50, 110), np.random.randint(110, 130), size=59)
    range_n2 = np.random.randint(np.random.randint(45, 100), np.random.randint(100, 140), size=59)
    
    random_month = np.random.randint(1, 24)
    random_noise_increase = np.random.uniform(2, 2.5)
    random_egt_increase = np.random.randint(160, 181)
    random_ff_increase = np.random.randint(140, 161)
    random_n1_increase = np.random.randint(350, 371)
    random_n2_increase = np.random.randint(350, 371)
    
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

    all_params = ['noise', 'egt', 'ff', 'n1', 'n2']
    sample_size = random.randint(0, 5)
    samples = random.sample(all_params, sample_size)

    for sample in samples:
        
        if sample == 'noise':
            noise[random_month:] += random_noise_increase
            
        elif sample == 'egt':
            egt[random_month:] += random_egt_increase
            
        elif sample == 'ff':
            ff[random_month:] += random_ff_increase
            
        elif sample == 'n1':
            n1[random_month:] += random_n1_increase
            
        else:
            n2[random_month:] += random_n2_increase
    
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
    
    total_fp[min(([np.where(fp_noise == 1)[0][0], np.where(fp_egt == 1)[0][0], np.where(fp_ff == 1)[0][0], np.where(fp_n1 == 1)[0][0], np.where(fp_n2 == 1)[0][0]])): ] = 1
    
    df['noise'] = noise
    df['egt'] = egt
    df['ff'] = ff
    df['n1'] = n1
    df['n2'] = n2
    df['act_fp_noise'] = fp_noise
    df['act_fp_egt'] = fp_egt
    df['act_fp_ff'] = fp_ff
    df['act_fp_n1'] = fp_n1
    df['act_fp_n2'] = fp_n2
    df['act_total_fp'] = total_fp
    df['engine'] = engine
    
    df.to_csv('../../data/test_data/test_data_' + str(engine) + '.csv', index=False)
