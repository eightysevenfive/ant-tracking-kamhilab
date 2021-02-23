import os
import subprocess

ROOT = os.getcwd()+'/data/'

image_dirs = [d for r, d, f in os.walk(ROOT)][0]
file_by_dir = [os.listdir(ROOT+d) for d in image_dirs]

for dir_index, image_dir in enumerate(image_dirs):
    try:
        largest_num = max([len(f.split('_')[1].split('.')[0]) for f in file_by_dir[dir_index]])
        for f in file_by_dir[dir_index]:
            opath = ROOT+image_dir+'/'+f
            name = f.split('_')[0]
            ext = f.split('.')[1]
            number = f.split('_')[1].split('.')[0]
            if len(number) <= largest_num:
                to_add = largest_num - len(number)
                number = ('0'*to_add)+number
            f_name = name+'_'+number+'.'+ext
            npath = ROOT+image_dir+'/'+f_name
            subprocess.run(['mv', f'{opath}', f'{npath}'])
    except IndexError:
        pass
