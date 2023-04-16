import cv2 
def takesnapshot():
    #initialising cv2
    videocaptureobject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videocaptureobject.read
        #cv2 imwrite()method is used to save an image to any storage device 
        cv2.imwrite('new picture.jpg',frame)
        result=False 

    # Release the camera
    videocaptureobject.release()
        # Close all the windows that might be opened while this process
takesnapshot()
    