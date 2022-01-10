import os
path = "/home/frozentoad9/CMASR/"
dir_list = os.listdir(path)
dir_list.sort()

print(dir_list)


subtitle_list = []
for x in dir_list:
    sub_list = os.listdir(path+x)
    sub_list.sort()
    subtitle_list.append(sub_list)

print(subtitle_list[0])

total_lines = []
eng_length = []
for direc in dir_list:
    direc_list = os.listdir(path+direc)
    direc_list.sort()
    file_length = []
    for files in direc_list:
        length = (open(path+direc+"/"+files).read().strip('\n').split('\n\n')[-1].split('\n')[0])
        if 'English' in files:
            eng_length.append(length)
        file_length.append(length)
    total_lines.append(file_length)
        
        
print(total_lines[0]) 
print(len(eng_length))

count = 0
for i in range(1080):
    total = len(total_lines[i])
    for j in range(total):
        if eng_length[i]!=total_lines[i][j]:
            print(dir_list[i])
            print(subtitle_list[i][j])
            count += 1
print(count)

common_lang = []
for x in subtitle_list[0]:
    count = 0
    for i in range(1080):
        if x in subtitle_list[i]:
            count+=1
    if count==1080:
        print(x)
        common_lang.append(x)


print(len(common_lang))


print(subtitle_list[2])

count = 0
for x in subtitle_list:
    if 'Spanish[100%].srt' in x:
        count+=1
    else:
        print(count)
print(count)


print(subtitle_list[0][23])

test = open(path+dir_list[0]+"/"+subtitle_list[0][23]).read().strip('\n').split('\n\n')

for i in test:
    print(i.split('\n')[2])
print(test)

print(total_lines[0][0])





# =============================================================================
# count = 0
# for direc in dir_list:
#     direc_list = os.listdir(path+direc)
#     direc_list.sort()
#     for files in direc_list:
#         if '100%' not in files:
#             print(direc)
#             print(files)       
# print(count)
# =============================================================================
