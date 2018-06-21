#python2.7

import os

fw = open('maindexlist.txt', 'w') 

def dirlist(path):  
    filelist = os.listdir(path)  
  
    for filename in filelist:  
        filepath = os.path.join(path, filename)  
        if os.path.isdir(filepath):  
            dirlist(filepath)  
        elif len(filepath)>5 and filepath[-5:]=='.java':  
            baseStr = filepath.replace('src/main/java/','').replace('.java', '')
            fw.write(baseStr+ '.class\n')
            for index in range(1, 11):
                fw.write(baseStr+ '$' + str(index) + '.class\n')

    fw.close()
dirlist("src/main/java/")  

