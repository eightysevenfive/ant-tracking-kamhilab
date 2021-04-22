import os
import csv
import subprocess

# ROOT = os.getcwd()+'/05FrameData/obj/'
ROOT = os.getcwd()+'/obj/'

os.chdir(ROOT)

for f in os.listdir(ROOT):
    if ' copy' in f:
        x = f.replace(' copy', '')
        subprocess.run(['mv',f,x])
    '''
    lines = []
    name = f
    with open(f, 'r') as _f:
        lines.extend(_f.readlines())
        lines = [elt.replace('\n', '').split() for elt in lines]
        for line in lines:
            if line[0] == '2':
                line[0] = '0'
            if line[0] == '3':
                line[0] = '1'
        lines = [' '.join(elt) for elt in lines]
        subprocess.run(['rm', f'{ROOT+f}'])
    print(lines)
    with open(name, 'w') as _h:
        if len(lines) == 1:
            _h.write(lines[0])
        else:
            _h.write(lines[0])
            _h.write('\n')
            _h.write(lines[1])
        _h.close()
    '''
