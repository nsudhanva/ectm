import numpy as np
import csv
import pdb

head = ["engine", "month", "egt", "ff", "n1", "n2", "egt_n", "ff_n", "n1_n", "n2_n", "normal", "failure_prob"]
body = {}
prev_egt = 0
prev_ff = 0
prev_n1 = 0
prev_n2 = 0

with open("..engine_data.csv", "w") as csv_file :
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerows([head])
    
    for engine_no in range(1, 101):
    
        body[engine_no] = {}
        
        for month in range(1, 25):
            
            body_w = []
            
            body[engine_no][month] = {}
            body[engine_no][month]['failure_prob'] = 0

            if month > 1:
                
                prev_egt = body[engine_no][month - 1]['egt']
                prev_ff = body[engine_no][month - 1]['ff']
                prev_n1 = body[engine_no][month - 1]['n1']
                prev_n2 = body[engine_no][month - 1]['n2']
            
            if month == 1:
                
                body[engine_no][month]['egt'] = np.random.randint(1100, 1300)
                body[engine_no][month]['ff'] = np.random.randint(4800, 5000)
                body[engine_no][month]['n1'] = np.random.randint(11000, 12500)
                body[engine_no][month]['n2'] = int(np.random.uniform(9000, 11000))
                
            else:
                
                body[engine_no][month]['egt'] = np.random.randint(prev_egt, prev_egt + np.random.randint(1, 100))
                body[engine_no][month]['ff'] = np.random.randint(prev_ff, prev_ff + np.random.randint(1, 100))
                body[engine_no][month]['n1'] = np.random.randint(prev_n1, prev_n1 + np.random.randint(1, 300))
                body[engine_no][month]['n2'] = np.random.randint(prev_n2, prev_n2 + np.random.randint(1, 300))
                
            if body[engine_no][month]['egt'] > 1900 :
                body[engine_no][month]['egt_n'] = False
                body[engine_no][month]['failure_prob'] += 25
            else:
                body[engine_no][month]['egt_n'] = True
            
            if body[engine_no][month]['ff'] > 5500 :
                body[engine_no][month]['ff_n'] = False
                body[engine_no][month]['failure_prob'] += 25
            else:
                body[engine_no][month]['ff_n'] = True
    
            if body[engine_no][month]['n1'] > 14000 :
                body[engine_no][month]['n1_n'] = False
                body[engine_no][month]['failure_prob'] += 25
            else:
                body[engine_no][month]['n1_n'] = True            
    
            if body[engine_no][month]['n2'] > 12000 :
                body[engine_no][month]['n2_n'] = False
                body[engine_no][month]['failure_prob'] += 25
            else:
                body[engine_no][month]['n2_n'] = True
                
            if body[engine_no][month]['egt_n'] == False or body[engine_no][month]['ff_n'] == False or body[engine_no][month]['n1_n'] == False or body[engine_no][month]['n2_n'] == False :
                body[engine_no][month]['normal'] = False
            else :
                body[engine_no][month]['normal'] = True
    
            body_w.append(str(engine_no))
            body_w.append(str(month))
            body_w.append(str(body[engine_no][month]['egt']))
            body_w.append(str(body[engine_no][month]['ff']))
            body_w.append(str(body[engine_no][month]['n1']))
            body_w.append(str(body[engine_no][month]['n2']))
            body_w.append(str(body[engine_no][month]['egt_n']))
            body_w.append(str(body[engine_no][month]['ff_n']))
            body_w.append(str(body[engine_no][month]['n1_n']))
            body_w.append(str(body[engine_no][month]['n2_n']))
            body_w.append(str(body[engine_no][month]['normal']))
            body_w.append(str(body[engine_no][month]['failure_prob']))
            
            writer.writerows([body_w])
            
            