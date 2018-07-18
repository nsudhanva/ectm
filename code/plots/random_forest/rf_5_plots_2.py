import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df1 = pd.read_csv('../../../data/test_data/test_data_6.csv')
df2 = pd.read_csv('../../../data/test_data/test_data_7.csv')
df3 = pd.read_csv('../../../data/test_data/test_data_8.csv')
df4 = pd.read_csv('../../../data/test_data/test_data_9.csv')
df5 = pd.read_csv('../../../data/test_data/test_data_10.csv')
ndf = pd.read_csv('../../../data/normal_data.csv')

fp_1 = df1['rf_total_fp'].values
fp_2 = df2['rf_total_fp'].values
fp_3 = df3['rf_total_fp'].values
fp_4 = df4['rf_total_fp'].values
fp_5 = df5['rf_total_fp'].values
fp_n = ndf['total_fp'].values

months = ndf['month'].values

plt.figure(figsize=(20, 15))
plt.plot(months, fp_n, color = 'green', linestyle='-', marker='.', label='Age under normal conditions - Normal')
plt.plot(months, fp_1, color = 'red', linestyle='-', marker='.', label='Age under normal conditions - Engine ' + str(df1['engine'][0]))
plt.plot(months, fp_2, color = 'blue', linestyle='-', marker='.', label='Age under normal conditions - Engine ' + str(df2['engine'][0]))
plt.plot(months, fp_3, color = 'black', linestyle='-', marker='.', label='Age under normal conditions - Engine ' + str(df3['engine'][0]))
plt.plot(months, fp_4, color = 'yellow', linestyle='-', marker='.', label='Age under normal conditions - Engine ' + str(df4['engine'][0]))
plt.plot(months, fp_5, color = 'orange', linestyle='-', marker='.', label='Age under normal conditions - Engine ' + str(df5['engine'][0]))

plt.axvline(x=np.where(fp_n==1)[0][0]+1, color='green', label='Predicted Failure Month - Normal')
plt.axvline(x=np.where(fp_1==1)[0][0]+1, color='red', label='Predicted Failure Month - Engine ' + str(df1['engine'][0]))
plt.axvline(x=np.where(fp_2==1)[0][0]+1, color='blue', label='Predicted Failure Month - Engine ' + str(df2['engine'][0]))
plt.axvline(x=np.where(fp_3==1)[0][0]+1, color='black', label='Predicted Failure Month - Engine ' + str(df3['engine'][0]))
plt.axvline(x=np.where(fp_4==1)[0][0]+1, color='yellow', label='Predicted Failure Month - Engine ' +  str(df4['engine'][0])) 
plt.axvline(x=np.where(fp_5==1)[0][0]+1, color='orange', label='Predicted Failure Month - Engine ' + str(df5['engine'][0]))

plt.xticks(np.arange(1, 62, 2))
plt.yticks(np.arange(0, 1.05, 0.05))

plt.title('Age (in months) vs Probability of Failure')
plt.legend(loc='best')
plt.xlabel('Age (in months)')
plt.ylabel('Probability of Failure')
plt.show()

plt.savefig('../../../outputs/random_forest/rf_5_plots_2.png')
