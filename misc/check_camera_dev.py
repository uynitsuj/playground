import cv2
import glob
print(glob.glob("/dev/video"))
for camera in glob.glob("/dev/video"):
    c = cv2.VideoCapture(camera)
    print(camera)
print('\n' + '\033[1m'+'WARNING:'+'\033[0m'+' unable to open video source for /dev/video' +
      str(0)+'. \033[1m' + 'CAMERA HARDWARE DISCONNECT?' + '\033[0m\n')
print('\nWARNING: unable to open video source for /dev/video' +
      str(0)+'. \033[1m' + 'CAMERA HARDWARE DISCONNECT?' + '\033[0m\n')
