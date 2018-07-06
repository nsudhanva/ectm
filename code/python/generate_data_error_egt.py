import numpy as np
import csv
import pdb

head = ["engine", "month", "air_temp", "noise", "epr", "egt", "ff", "n1", "n2", "noise_n", "epr_n", "egt_n", "ff_n", "n1_n", "n2_n", "normal", "failure_prob"]
body = {}
prev_egt = 0
prev_ff = 0
prev_n1 = 0
prev_n2 = 0

with open("../../data/engine_data_error_egt.csv", "w") as csv_file :
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerows([head])
    
    for engine_no in range(1, 101):
    
        body[engine_no] = {}
        
        for month in range(1, 61):
            
            body_w = []
            
            body[engine_no][month] = {}
            
            body[engine_no][month]['failure_prob'] = 0
            
            body[engine_no][month]['air_temp'] = np.random.randint(-15, 1)
            
            if month <= 36:
                body[engine_no][month]['epr'] = np.random.randint(48, 51)
            else:
                body[engine_no][month]['epr'] = np.random.randint(49, 53)
                
            if month == 1:
                
                body[engine_no][month]['egt'] = 1300
                body[engine_no][month]['ff'] = 5000
                body[engine_no][month]['n1'] = 12000
                body[engine_no][month]['n2'] = 1000
                body[engine_no][month]['noise'] = 130
                
            else:
                
                prev_failure_prob = body[engine_no][month-1]['failure_prob']
                body[engine_no][month]['failure_prob'] = prev_failure_prob
                
                body[engine_no][month]['egt'] = 1600 + np.random.randint((month-1)*11, month*11)
                body[engine_no][month]['ff'] = 5000 + np.random.randint((month-1)*9, month*9)
                body[engine_no][month]['n1'] = 12000 + np.random.randint((month-1)*35, month*35)
                body[engine_no][month]['n2'] = 10000 + np.random.randint((month-1)*35, month*35)
                body[engine_no][month]['noise'] = int(130 + month*0.2)
            
            if body[engine_no][month]['egt'] > 1750 :
                body[engine_no][month]['egt_n'] = False
                body[engine_no][month]['failure_prob'] += 1
            else:
                body[engine_no][month]['egt_n'] = True
            
            if body[engine_no][month]['ff'] > 5350 :
                body[engine_no][month]['ff_n'] = False
                body[engine_no][month]['failure_prob'] += 1
            else:
                body[engine_no][month]['ff_n'] = True
    
            if body[engine_no][month]['n1'] > 13500 :
                body[engine_no][month]['n1_n'] = False
                body[engine_no][month]['failure_prob'] += 1
            else:
                body[engine_no][month]['n1_n'] = True            
    
            if body[engine_no][month]['n2'] > 11500 :
                body[engine_no][month]['n2_n'] = False
                body[engine_no][month]['failure_prob'] += 1
            else:
                body[engine_no][month]['n2_n'] = True
                
            if body[engine_no][month]['noise'] > 137 :
                body[engine_no][month]['noise_n'] = False
                body[engine_no][month]['failure_prob'] += 1
            else:
                body[engine_no][month]['noise_n'] = True
                
            if body[engine_no][month]['epr'] > 50 :
                body[engine_no][month]['epr_n'] = False
                body[engine_no][month]['failure_prob'] += 1
            else:
                body[engine_no][month]['epr_n'] = True
                
            if body[engine_no][month]['egt_n'] == False or body[engine_no][month]['ff_n'] == False or body[engine_no][month]['n1_n'] == False or body[engine_no][month]['n2_n'] == False or body[engine_no][month]['noise_n'] == False or body[engine_no][month]['epr_n'] == False :
                body[engine_no][month]['normal'] = False
            else :
                body[engine_no][month]['normal'] = True
                
            if body[engine_no][month]['failure_prob'] > 100:
                body[engine_no][month]['failure_prob'] = 100
    
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
            
            