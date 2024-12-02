import sys
import cv2
import time 

def convert_jpeg_to_png(in_filename,out_filename=None):
    time.sleep(10)
    if out_filename is None:
        out_filename=in_filename.split(".")[0]+".png"
    
    an_image = cv2.imread(in_filename)
    cv2.imwrite(out_filename, an_image)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        convert_jpeg_to_png(sys.argv[1])
    else:
        convert_jpeg_to_png(sys.argv[1],sys.argv[2])

