import glob
import random

txt_files = glob.glob('obj/*.jpg')
files = glob.glob('obj/*.txt')

#for f in files:
#    with open(f,'r') as _file:
#        line = _file.read()
#    with open(f,'w') as _file:
#        lx = '0'+ line[1:]
#        _file.write(lx.strip('\n'))
#        _file.close()

random.shuffle(txt_files)
trn_files = txt_files[:round(len(txt_files)*0.8)]
tst_files = txt_files[round(len(txt_files)*0.8):]

print(trn_files)
with open('train.txt', 'w') as file1:
    for f in trn_files:
        name = f.split('.')[0]
        if f != trn_files[-1]:
            file1.writelines('darknet/data/'+name+'.jpg'+'\n')
        else:
            file1.writelines('darknet/data/'+name+'.jpg')
    file1.close()

with open('test.txt', 'w') as file2:
    for f in tst_files:
        name = f.split('.')[0]
        if f != tst_files[-1]:
            file2.writelines('darknet/data/'+name+'.jpg'+'\n')
        else:
            file2.writelines('darknet/data/'+name+'.jpg')
    file2.close()
