from os import getpid, getppid
from time import sleep

def square(x):
    return x*x

def get_pids(val, wait=0):
    sleep(wait)
    print('Pid: {}, PPid: {}, Value: {}'
          .format(getpid(), getppid(), val))

def printer(val, wait=0):
    sleep(wait)
    print('Pid: {}, PPid: {}, Value: {}'
          .format(getpid(), getppid(), val))

from convert_jpeg_to_png import *

def convert(q):
    in_filename,out_filename = q.get()
    convert_jpeg_to_png(in_filename,out_filename)

def convert_many(q):
    while True:
        in_filename,out_filename = q.get()
        if in_filename == "DONE":
            break
        else:
            convert_jpeg_to_png(in_filename,out_filename)

import cv2
def load_many(in_q,out_q):
    while True:
        in_filename = in_q.get()
        if in_filename == "DONE":
            break
        else:
            image=cv2.imread(in_filename)
            out_q.put(image)

import numpy as np
from multiprocessing import shared_memory
            
def load_many_shm(in_q,out_q,shm_name,t_shape,t_dtype):
    existing_shm = shared_memory.SharedMemory(name=shm_name)
    images = np.ndarray(t_shape, dtype=t_dtype, buffer=existing_shm.buf)
    
    while True:
        in_filename,i = in_q.get()
        if in_filename == "DONE":
            print('DONE: Pid: {}, PPid: {}'.format(getpid(), getppid()))
            break
        else:
            print('Reading: Pid: {}, PPid: {}, File: {}, Index: {}'.format(getpid(), getppid(),in_filename,i))

            images[i]=cv2.imread(in_filename)
            out_q.put(i)