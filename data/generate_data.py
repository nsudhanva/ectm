import numpy as np
import csv
import pdb

min_atemp = -50
max_atemp = 35

min_egt = 700
max_egt = 1900

min_ff = 4500
max_ff = 5000

min_n1 = 10000
max_n1 = 14000

min_n1 = 8000
max_n2 = 12000

head = ["Engine", "Time", "Air Temperature", "Exhaust Gas Temperature", "Fuel Flow", "Low Pressure Fan Speed (N1)", "High Pressure Rotor Speed (N2)", "EGT Normal", "Fuel Flow Normal", "N1 Normal", "N2 Normal", "Normal"]                       
engine_no = 0
time = 0

with open("engine_data.csv", "w") as csv_file :
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerows([head])
    
    for i in range(0, 100000):
        
        body = []
        
        if i % 5000 == 0:
            engine_no += 1
        
        if time > 23:
            time = 0

        body.append(str(engine_no))
        body.append(str(time))
        
        atemp = int(np.random.uniform(min_atemp, max_atemp))
        body.append(str(atemp))

        if atemp >= -50 and atemp <= -30 :
            
            egt = int(np.random.uniform(500, 1200))
            ff = int(np.random.uniform(4300, 5200))
            n1 = int(np.random.uniform(9000, 13000))
            n2 = int(np.random.uniform(9000, 13000))
            
            if egt < 700 or egt > 1000 :
                egt_normal = False
            else:
                egt_normal = True
            
            if ff < 4500 or ff > 5000 :
                ff_normal = False
            else:
                ff_normal = True

            if n1 < 10000 or n1 > 12000 :
                n1_normal = False
            else:
                n1_normal = True            

            if n2 < 10000 or n2 > 12000 :
                n2_normal = False
            else:
                n2_normal = True
            
        elif atemp > -30 and atemp <= 0 :
            
            egt = int(np.random.uniform(800, 1700))
            ff = int(np.random.uniform(4600, 5400))
            n1 = int(np.random.uniform(10000, 14000))
            n2 = int(np.random.uniform(8000, 12000))
            
            if egt < 1000 or egt > 1500 :
                egt_normal = False
            else:
                egt_normal = True
            
            if ff < 4800 or ff > 5200 :
                ff_normal = False
            else:
                ff_normal = True

            if n1 < 11000 or n1 > 13000 :
                n1_normal = False
            else:
                n1_normal = True            

            if n2 < 9000 or n2 > 11000 :
                n2_normal = False
            else:
                n2_normal = True               
            
        else :
            
            egt = int(np.random.uniform(1200, 2100))
            ff = int(np.random.uniform(4900, 5700))
            n1 = int(np.random.uniform(11000, 15000))
            n2 = int(np.random.uniform(7000, 11000))
            
            if egt < 1400 or egt > 1900 :
                egt_normal = False
            else:
                egt_normal = True
            
            if ff < 5100 or ff > 5500 :
                ff_normal = False
            else:
                ff_normal = True

            if n1 < 12000 or n1 > 14000 :
                n1_normal = False
            else:
                n1_normal = True            

            if n2 < 8000 or n2 > 10000 :
                n2_normal = False
            else:
                n2_normal = True             
        
        if egt_normal == False or ff_normal == False or n1_normal == False or n2_normal == False :
            normal = False
        else :
            normal = True

        body.append(str(egt))
        body.append(str(ff))
        body.append(str(n1))
        body.append(str(n2))
        body.append(str(egt_normal))
        body.append(str(ff_normal))
        body.append(str(n1_normal))
        body.append(str(n2_normal))
        body.append(str(normal))
        
        writer.writerows([body])
        
        time += 1