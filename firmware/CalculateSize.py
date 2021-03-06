# calculate bootloader location and free userspace

import sys
import math

def printmnsize(codesize,pagesize=64,memsize=8192):
    pages=math.ceil(codesize/pagesize)
    freespace=memsize-pages*pagesize-6
    bootstart=memsize-pages*pagesize

    print('Codesize: {:04d} bytes, BOOTLOADER ADDRESS: 0x{:04X}, Free user memory {:04d} bytes.'.format(codesize,bootstart,freespace))

codesize=0

for currentline in sys.stdin.readlines():
    splitline=currentline.split()
    try:
        if splitline[0] == 'Total':
            codesize = int(splitline[1])
    except:
        pass

if (codesize == 0):
    print("Codesize could not be found!")
    exit()

print('8K  Device -- ',end='')
printmnsize(codesize,pagesize=64,memsize=8192)
print('16K Device -- ',end='')
printmnsize(codesize,pagesize=64,memsize=16384)
