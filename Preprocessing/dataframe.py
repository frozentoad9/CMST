import numpy as np
import pandas as pd

import os
path = "/home/frozentoad9/CMASR/"
dir_list = os.listdir(path)
dir_list.sort()


subtitle_list = []
for x in dir_list:
    sub_list = os.listdir(path+x)
    sub_list.sort()
    subtitle_list.append(sub_list)

# using common languages as columns
common_lang = []
for x in subtitle_list[0]:
    count = 0
    for i in range(1080):
        if x in subtitle_list[i]:
            count+=1
    if count==1080:
        print(x)
        common_lang.append(x)

print(common_lang)


test = open(path+dir_list[857]+"/"+'French (France)[100%].srt').read().strip('\n').split('\n\n')

for i in test:
    print(i.split('\n')[0])
    

final_data = [x for x in range(27)]
i = 0
for direc in dir_list:
    direc_list = os.listdir(path+direc)
    direc_list.sort()
    temp1 = open(path+direc+"/"+"English[100%].srt").read().strip('\n').split('\n\n')
    time_stamp = []
    for x in temp1:
        time_stamp.append(direc.split('_')[0]+"_"+'_'.join(x.split('\n')[1].split(' --> ')))
    for files in direc_list:
        if files in common_lang:
            temp2 = open(path+direc+"/"+files).read().strip('\n').split('\n\n')
            trans = []
            for y in temp2:
                trans.append(y.split('\n')[2])
            time_stamp = np.column_stack((time_stamp, trans))
    final_data = np.vstack((final_data, time_stamp))
    print(len(final_data))

df_columns = ['time_stamp']+common_lang
print(df_columns)
#deleting unnecessary row in array
final_data = np.delete(final_data, (0), axis=0)
print(final_data[0])    


df = pd.DataFrame(final_data, columns=df_columns)
df.shape

#saving dataframe to csv file
df.to_csv('dataframe.csv', index=None)


print(final_data[0][0].split('_')) 
print(final_data[1][0].split('_')) 
from datetime import datetime


sum = datetime.strptime('0:00:00,0', '%H:%M:%S,%f')
print(sum)
for i in range(len(final_data)):
    t_stamp = final_data[0][0].split('_')
    d1 = datetime.strptime(t_stamp[1], "%H:%M:%S,%f")
    d2 = datetime.strptime(t_stamp[2], "%H:%M:%S,%f")
    sum += (d2-d1)
print(sum)

sum.hour()












