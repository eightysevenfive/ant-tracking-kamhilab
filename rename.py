import glob
import random
import subprocess

txt_files = glob.glob('obj/*.jpeg')
#files = glob.glob('obj/*.txt')

#for f in files:
#    with open(f,'r') as _file:
#        line = _file.read()
#    with open(f,'w') as _file:
#        lx = '0'+ line[1:]
#        _file.write(lx.strip('\n'))
#        _file.close()
        
#random.shuffle(txt_files)
#trn_files = txt_files[:round(len(txt_files)*0.8)]
#tst_files = txt_files[round(len(txt_files)*0.8):]

#print(trn_files)
for f in txt_files:
    name = f.split('.')[0]+'.jpg'
    subprocess.run(['mv',f,name])
'''
with open('test.txt', 'w') as file2:
    for f in tst_files:
        name = f.split('.')[0]
        if f != tst_files[-1]:
            file2.writelines('data/'+name+'.jpg'+'\n')
        else:
            file2.writelines('data/'+name+'.jpg')
    file2.close()    

'''
