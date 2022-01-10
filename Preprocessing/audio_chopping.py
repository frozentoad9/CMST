import os
path = "/home/frozentoad9/CMASR/"
dir_list = os.listdir(path)
dir_list.sort()


subtitle_list = []
for x in dir_list:
    sub_list = os.listdir("/home/frozentoad9/CMASR/"+x)
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


common_lang

import os
from pysubparser import parser
from datetime import datetime, date


path = "/media/frozentoad9/HP x765w/CHOPPED_AUDIO/"
dir_list = os.listdir(path)
dir_list.sort()
dir_list[7]

#creating a new folder for chopped audios
# =============================================================================
# for x in dir_list:
#     os.mkdir(path+x+'/ChoppedAudio')
#     
# =============================================================================

# =============================================================================
# for x in dir_list:
#     direc = os.listdir(path+x+'/ChoppedAudio')
#     for files in direc:
#         os.rename(path+x+'/ChoppedAudio/'+files, path+x+'/ChoppedAudio/'+x+'_'+files)
# 
# =============================================================================

subtitles = parser.parse('/media/frozentoad9/HP x765w/CMASR/0001_Expand To Ten Million/English[100%].srt')

for subtitle in subtitles:
    print(subtitle)

dir_list[7]

dir_list[0]
for i in range(7, 1080):
    direc = dir_list[i]
    for lang in common_lang:
        subtitle_list=[]
        start = []
        end = []
        subtitles = parser.parse('/media/frozentoad9/HP x765w/CMASR/'+direc+'/'+lang)
        for subtitle in subtitles:
            subtitle_list.append(subtitle.text)
            start.append(subtitle.start)
            end.append(subtitle.end)
        dirFiles = os.listdir('/media/frozentoad9/HP x765w/CHOPPED_AUDIO/'+direc+'/ChoppedAudio')
        dirFiles.sort()
        for k in range (0,len(dirFiles)):
          with open('/media/frozentoad9/HP x765w/CHOPPED_AUDIO/'+direc+'/'+lang[:-4]+'.txt','a',encoding='utf-8') as file:
            file.write(f'{dirFiles[k][:4]}_{start[k]}_{end[k]}_{subtitle_list[k]}')
            file.write('\n')
            file.close()
            k=k+1
    print(direc)  

#deleting files:
dirFiles = os.listdir('/media/frozentoad9/HP x765w/CHOPPED_AUDIO/'+dir_list[0]+'/ChoppedAudio')
dirFiles

subtitles = parser.parse('/media/frozentoad9/HP x765w/CMASR/'+dir_list[0]+'/English[100%].srt')
for subtitle in subtitles:
    print(subtitle.text, subtitle.start, subtitle.end)

/media/frozentoad9/HP x765w/CHOPPED_AUDIO/'+direc+lang[:-4]+'.txt'
common_lang[0][:-4]
subtitle_list=[]
subtitles = parser.parse('/media/frozentoad9/HP x765w/CMASR/0001_Expand To Ten Million/English[100%].srt')

for subtitle in subtitles:
    subtitle_list.append(subtitle.text)
subtitle_list

for k in range (0,len(dirFiles)):
  with open('Data.txt','a',encoding='utf-8') as file:
    file.write(f'{dirFiles[k]}   {subtitle_list[k]}')
    file.write('\n')
    file.close()
    k=k+1
    

# =============================================================================
# for x in dir_list:
#     subtitles = parser.parse('/media/frozentoad9/HP x765w/CMASR/'+dir_list[32]+'/English[100%].srt')
#     for subtitle in subtitles:
#       start = datetime.combine(date.min, subtitle.start) - datetime.min
#       start=start.total_seconds()
#       end=datetime.combine(date.min, subtitle.end) - datetime.min
#       end=end.total_seconds()
#       with open(path+dir_list[0]+'/'+dir_list[32]+'.txt','a',encoding='utf-8') as file:
#         file.write(f'{start} {end} {subtitle.text}')
#         file.write('\n')
#         file.close()
#         #print(f'{subtitle.start}    {subtitle.end}    {subtitle.text}')
#         #print(subtitle.text)
#         #print()
#     print(x)
# =============================================================================


audio_files = os.listdir('/media/frozentoad9/HP x765w/CMASR_AUDIO/')
audio_files.sort()
print(audio_files)
#chopping audios

from audioclipextractor import AudioClipExtractor, SpecsParser    

# =============================================================================
# ext = AudioClipExtractor('/media/frozentoad9/HP x765w/CMASR_AUDIO/0001_Expand To Ten Million.mp3',
#                          )
# ext.extract_clips('/media/frozentoad9/HP x765w/CHOPPED_AUDIO/0001_Expand To Ten Million/0001_Expand To Ten Million.txt',
#                   '/media/frozentoad9/HP x765w/CHOPPED_AUDIO/0001_Expand To Ten Million/ChoppedAudio', zip_output=False)
# =============================================================================


sum = 0
for x in dir_list:
    direc = os.listdir(path+x+'/ChoppedAudio')
    sum += len(direc)

print(sum)
     

# =============================================================================
# print('/media/frozentoad9/HP x765w/CHOPPED_AUDIO/'+not_done[0]+'/'+not_done[0]+'.txt')
# not_done = []
# for i in range(580, 583):
#     x = audio_files[i]
#     ext = AudioClipExtractor('/media/frozentoad9/HP x765w/CMASR_AUDIO/'+x)
#     try:
#         x = x[:-4]
#         ext.extract_clips('/media/frozentoad9/HP x765w/CHOPPED_AUDIO/'+x+'/'+x+'.txt',
#                       '/media/frozentoad9/HP x765w/CHOPPED_AUDIO/'+x+'/ChoppedAudio', zip_output=False)
#         print('done--> {}'.format(x))
#     except:
#         not_done.append(x)  
#         print(x)
#     
# 
# audio_files
# audio_files[452][:-4]
# =============================================================================

    

 