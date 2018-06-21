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


data = {}

# i is for engines
for i in range(0, 10000) :    
    data[i] = {}  
    
    # j is for time
    for j in range(0, 10) :
        
        data[i][j] = {}
    
        data[i][j]["atemp"] = int(np.random.uniform(min_atemp, max_atemp))

        if data[i][j]["atemp"] >= -50 and data[i][j]["atemp"] <= -30 :
            
            egt = int(np.random.uniform(500, 1200))
            ff = int(np.random.uniform(4300, 5200))
            n1 = int(np.random.uniform(9000, 13000))
            n2 = int(np.random.uniform(9000, 13000))
            
            data[i][j]["egt"] = egt
            data[i][j]["ff"] = ff
            data[i][j]["n1"] = n1
            data[i][j]["n2"] = n2
            
            if egt < 700 or egt > 1000 :
                data[i][j]["egt_normal"] = False
            else:
                data[i][j]["egt_normal"] = True
            
            if ff < 4500 or ff > 5000 :
                data[i][j]["ff_normal"] = False
            else:
                data[i][j]["ff_normal"] = True

            if n1 < 10000 or n1 > 12000 :
                data[i][j]["n1_normal"] = False
            else:
                data[i][j]["n1_normal"] = True            

            if n2 < 10000 or n2 > 12000 :
                data[i][j]["n2_normal"] = False
            else:
                data[i][j]["n2_normal"] = True
            
        elif data[i][j]["atemp"] > -30 and data[i][j]["atemp"] <= 0 :
            
            egt = int(np.random.uniform(800, 1700))
            ff = int(np.random.uniform(4600, 5400))
            n1 = int(np.random.uniform(10000, 14000))
            n2 = int(np.random.uniform(8000, 12000))
            
            data[i][j]["egt"] = egt
            data[i][j]["ff"] = ff
            data[i][j]["n1"] = n1
            data[i][j]["n2"] = n2
            
            if egt < 1000 or egt > 1500 :
                data[i][j]["egt_normal"] = False
            else:
                data[i][j]["egt_normal"] = True
            
            if ff < 4800 or ff > 5200 :
                data[i][j]["ff_normal"] = False
            else:
                data[i][j]["ff_normal"] = True

            if n1 < 11000 or n1 > 13000 :
                data[i][j]["n1_normal"] = False
            else:
                data[i][j]["n1_normal"] = True            

            if n2 < 9000 or n2 > 11000 :
                data[i][j]["n2_normal"] = False
            else:
                data[i][j]["n2_normal"] = True               
            
        else :
            
            egt = int(np.random.uniform(1200, 2100))
            ff = int(np.random.uniform(4900, 5700))
            n1 = int(np.random.uniform(11000, 15000))
            n2 = int(np.random.uniform(7000, 11000))
            
            data[i][j]["egt"] = egt
            data[i][j]["ff"] = ff
            data[i][j]["n1"] = n1
            data[i][j]["n2"] = n2
            
            if egt < 1400 or egt > 1900 :
                data[i][j]["egt_normal"] = False
            else:
                data[i][j]["egt_normal"] = True
            
            if ff < 5100 or ff > 5500 :
                data[i][j]["ff_normal"] = False
            else:
                data[i][j]["ff_normal"] = True

            if n1 < 12000 or n1 > 14000 :
                data[i][j]["n1_normal"] = False
            else:
                data[i][j]["n1_normal"] = True            

            if n2 < 8000 or n2 > 10000 :
                data[i][j]["n2_normal"] = False
            else:
                data[i][j]["n2_normal"] = True             
        
        if data[i][j]["egt_normal"] == False or data[i][j]["ff_normal"] == False or data[i][j]["n1_normal"] == False or data[i][j]["n2_normal"] == False :
            data[i][j]["normal"] = False
        else :
            data[i][j]["normal"] = True

head_rows = ["Engine", "Time", "Air Temperature", "Exhaust Gas Temperature", "Fuel Flow", "Low Pressure Fan Speed (N1)", "High Pressure Rotor Speed (N2)", "EGT Normal", "Fuel Flow Normal", "N1 Normal", "N2 Normal", "Normal"]                       

with open("engine_data.csv", "w") as csv_file :
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerows([head_rows])
    
    for engine, value in data.items() :
        
        for value, engine_data in value.items() :
            
            final_data = []
            csv_data = []

            csv_data.append(str(engine))
            csv_data.append(str(value))
            csv_data.append(str(engine_data['atemp']))
            csv_data.append(str(engine_data['egt']))
            csv_data.append(str(engine_data['ff']))
            csv_data.append(str(engine_data['n1']))
            csv_data.append(str(engine_data['n2']))
            csv_data.append(str(engine_data['egt_normal']))
            csv_data.append(str(engine_data['ff_normal']))
            csv_data.append(str(engine_data['n1_normal']))
            csv_data.append(str(engine_data['n2_normal']))
            csv_data.append(str(engine_data['normal']))
            
            final_data.append(csv_data)
            
            writer.writerows(final_data)






