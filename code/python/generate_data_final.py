import numpy as np
import csv
import pdb

head = ["engine", "month", "air_temp", "noise", "epr", "egt", "ff", "n1", "n2", "noise_n", "epr_n", "egt_n", "ff_n", "n1_n", "n2_n", "normal", "failure_prob"]
body = {}
prev_egt = 0
prev_ff = 0
prev_n1 = 0
prev_n2 = 0

with open("../../data/engine_data_1.csv", "w") as csv_file :
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerows([head])
    
    for engine_no in range(1, 2):
    
        body[engine_no] = {}
        
        for month in range(1, 61):
            
            body_w = []
            
            body[engine_no][month] = {}
            body[engine_no][month]['failure_prob'] = 0
            
            body[engine_no][month]['air_temp'] = np.random.randint(-15, 1)
            
            if month < 18 :
                body[engine_no][month]['epr'] = np.random.randint(48, 51)
            else :
                body[engine_no][month]['epr'] = np.random.randint(48, 55)
                
            if month == 1:
                
                body[engine_no][month]['egt'] = np.random.randint(1100, 80 + 1300 + abs((body[engine_no][month]['air_temp']*2)))
                body[engine_no][month]['ff'] = np.random.randint(4800, 80 + 5000)
                body[engine_no][month]['n1'] = np.random.randint(11000, 100 + 12500)
                body[engine_no][month]['n2'] = int(np.random.uniform(9000, 100 + 11000))
                body[engine_no][month]['noise'] = np.random.randint(120, 126)
                
            else:
                
                prev_egt = body[engine_no][month - 1]['egt']
                prev_ff = body[engine_no][month - 1]['ff']
                prev_n1 = body[engine_no][month - 1]['n1']
                prev_n2 = body[engine_no][month - 1]['n2']
                prev_noise = body[engine_no][month - 1]['noise']
                
                body[engine_no][month]['egt'] = np.random.randint(prev_egt, 80 + prev_egt + np.random.randint(1, 100) + abs((body[engine_no][month]['air_temp']*2)))
                body[engine_no][month]['ff'] = np.random.randint(prev_ff, 80 + prev_ff + np.random.randint(1, 100))
                body[engine_no][month]['n1'] = np.random.randint(prev_n1, 100 + prev_n1 + np.random.randint(1, 300))
                body[engine_no][month]['n2'] = np.random.randint(prev_n2, 100 + prev_n2 + np.random.randint(1, 300))
                body[engine_no][month]['noise'] = np.random.randint(prev_noise, prev_noise + np.random.randint(1, 3))
                
            if body[engine_no][month]['egt'] > 1900 :
                body[engine_no][month]['egt_n'] = False
                body[engine_no][month]['failure_prob'] += 18
            else:
                body[engine_no][month]['egt_n'] = True
            
            if body[engine_no][month]['ff'] > 5500 :
                body[engine_no][month]['ff_n'] = False
                body[engine_no][month]['failure_prob'] += 18
            else:
                body[engine_no][month]['ff_n'] = True
    
            if body[engine_no][month]['n1'] > 14000 :
                body[engine_no][month]['n1_n'] = False
                body[engine_no][month]['failure_prob'] += 18
            else:
                body[engine_no][month]['n1_n'] = True            
    
            if body[engine_no][month]['n2'] > 12000 :
                body[engine_no][month]['n2_n'] = False
                body[engine_no][month]['failure_prob'] += 18
            else:
                body[engine_no][month]['n2_n'] = True
                
            if body[engine_no][month]['noise'] > 140 :
                body[engine_no][month]['noise_n'] = False
                body[engine_no][month]['failure_prob'] += 18
            else:
                body[engine_no][month]['noise_n'] = True
                
            if body[engine_no][month]['epr'] > 50 :
                body[engine_no][month]['epr_n'] = False
                body[engine_no][month]['failure_prob'] += 10
            else:
                body[engine_no][month]['epr_n'] = True
                
            if body[engine_no][month]['egt_n'] == False or body[engine_no][month]['ff_n'] == False or body[engine_no][month]['n1_n'] == False or body[engine_no][month]['n2_n'] == False or body[engine_no][month]['noise_n'] == False or body[engine_no][month]['epr_n'] == False :
                body[engine_no][month]['normal'] = False
            else :
                body[engine_no][month]['normal'] = True
    
            body_w.append(str(engine_no))
            body_w.append(str(month))
            body_w.append(str(body[engine_no][month]['air_temp']))
            body_w.append(str(body[engine_no][month]['noise']))
            body_w.append(str(body[engine_no][month]['epr']))
            body_w.append(str(body[engine_no][month]['egt']))
            body_w.append(str(body[engine_no][month]['ff']))
            body_w.append(str(body[engine_no][month]['n1']))
            body_w.append(str(body[engine_no][month]['n2']))
            body_w.append(str(body[engine_no][month]['noise_n']))
            body_w.append(str(body[engine_no][month]['epr_n']))
            body_w.append(str(body[engine_no][month]['egt_n']))
            body_w.append(str(body[engine_no][month]['ff_n']))
            body_w.append(str(body[engine_no][month]['n1_n']))
            body_w.append(str(body[engine_no][month]['n2_n']))
            body_w.append(str(body[engine_no][month]['normal']))
            body_w.append(str(body[engine_no][month]['failure_prob']))
            
            writer.writerows([body_w])
            
            