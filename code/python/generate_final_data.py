import numpy as np
import csv
import pdb

head = ["engine", "month", "air_temp", "noise", "epr", "egt", "ff", "n1", "n2", "fp_noise", "fp_epr", "fp_egt", "fp_ff", "fp_n1", "fp_n2", "failure_prob"]
body = {}
prev_egt = 0
prev_ff = 0
prev_n1 = 0
prev_n2 = 0

with open("../../data/engine_final.csv", "w") as csv_file :
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerows([head])
    
    for engine_no in range(1, 2):
    
        body[engine_no] = {}
        
        for month in range(1, 61):
            
            body_w = []
            
            body[engine_no][month] = {}
            
            body[engine_no][month]['fp_noise'] = 0
            body[engine_no][month]['fp_epr'] = 0
            
            body[engine_no][month]['air_temp'] = np.random.randint(-15, 1)
            
            if month <= 25:
                body[engine_no][month]['epr'] = np.random.randint(48, 51)
            else:
                body[engine_no][month]['epr'] = np.random.randint(49, 53)
                
            if month == 1:
                
                body[engine_no][month]['egt'] = 1300
                body[engine_no][month]['ff'] = 5000
                body[engine_no][month]['n1'] = 12000
                body[engine_no][month]['n2'] = 10000
                body[engine_no][month]['noise'] = 130
                
            else:
                
                body[engine_no][month]['fp_noise'] = body[engine_no][month-1]['fp_noise']
                body[engine_no][month]['fp_epr'] = body[engine_no][month-1]['fp_epr']
                
                body[engine_no][month]['noise'] = int(130 + month*0.4)
                body[engine_no][month]['egt'] = 1300 + np.random.randint((month-1)*20, month*20)
                body[engine_no][month]['ff'] = 5000 + np.random.randint((month-1)*16, month*16)
                body[engine_no][month]['n1'] = 12000 + np.random.randint((month-1)*54, month*54)
                body[engine_no][month]['n2'] = 10000 + np.random.randint((month-1)*54, month*54)
                
            if body[engine_no][month]['noise'] > 137 :
                body[engine_no][month]['fp_noise'] += np.random.randint(4, 7)
                
            if body[engine_no][month]['epr'] > 50 :
                body[engine_no][month]['fp_epr'] += np.random.randint(9, 12)                

            if body[engine_no][month]['fp_noise'] > 100:
                body[engine_no][month]['fp_noise'] = 100
            if body[engine_no][month]['fp_epr'] > 100:
                body[engine_no][month]['fp_epr'] = 100

            body_w.append(str(engine_no))
            body_w.append(str(month))
            body_w.append(str(body[engine_no][month]['air_temp']))
            body_w.append(str(body[engine_no][month]['noise']))
            body_w.append(str(body[engine_no][month]['epr']))
            body_w.append(str(body[engine_no][month]['egt']))
            body_w.append(str(body[engine_no][month]['ff']))
            body_w.append(str(body[engine_no][month]['n1']))
            body_w.append(str(body[engine_no][month]['n2']))
            body_w.append(str(body[engine_no][month]['fp_noise']))
            body_w.append(str(body[engine_no][month]['fp_epr']))
            
            writer.writerows([body_w])
            
            
            