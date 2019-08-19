    
import numpy as np
import cv2
from PIL import ImageGrab
from PIL import Image
import wave


fourcc = cv2.VideoWriter_fourcc('X','V','I','D') #you can use other codecs as well.
vid = cv2.VideoWriter('record.avi', fourcc, 16, (1920, 1080))
while(True):
    img = ImageGrab.grab()
    img_np = np.array(img)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    #frame = rescale_frame(frame)
    vid.write(frame)
    cv2.imshow("frame", frame)
    cv2.resizeWindow('frame', 300,300)
    key = cv2.waitKey(1)
    if key == 27:
        break    


vid.release()
cv2.destroyAllWindows()
