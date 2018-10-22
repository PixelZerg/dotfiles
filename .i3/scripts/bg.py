import time
import subprocess
import random
import glob
import os

IMG_TYPES=('*.png','*.jpeg','*.jpg')

while True:
    imgs=[]
    for img_type in IMG_TYPES:
        imgs.extend(glob.glob(os.path.expanduser('~/Pictures/wallpapers/**/'+img_type),recursive=True))
    random.shuffle(imgs)

    while imgs:
        prc=subprocess.Popen(['xwinwrap','-ov','-fs','--','sleep','1'])
        time.sleep(0.3)
        subprocess.call(['feh','--bg-fill',imgs.pop()])
        prc.kill()
        time.sleep(60*5)
