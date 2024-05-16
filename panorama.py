import cv2

Dirs = {
    1 : "NORTH",
    2 : "EAST",
    3 : "SOUTH",
    4 : "WEST"
}
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 30)
images = []
err_dict = {
    cv2.STITCHER_OK: "STITCHER_OK",
    cv2.STITCHER_ERR_NEED_MORE_IMGS: "STITCHER_ERR_NEED_MORE_IMGS",
}

def takePicture():
    _, img = cap.read()
    img = cv2.resize(img, (1920,1080))
    images.append(img)
    

def Panorama(imgs):
    stitcher = cv2.Stitcher.create()
    (retval, output) = stitcher.stitch(imgs)
    if retval!= cv2.STITCHER_OK: 
        print(f"stitching falied with error code {retval} : {err_dict[retval]}")
        exit(retval)
    else:
        pos = 0
        for i in range(1,5):
            step = 350
            pos += step
            output = cv2.putText(output, Dirs.get(i), (pos, 200), cv2.FONT_HERSHEY_COMPLEX, 3, (0, 0, 255), 4, cv2.LINE_AA, False)

        print('Your Panorama is ready!!!')  
        cv2.imwrite("panorama.jpg", output)    

if __name__ == '__main__':
    counter = 0
    while counter <= 5:
        if(input("PRESS 'f': ") == 'f'):
            takePicture()
            counter+=1
    Panorama(images)

cv2.destroyAllWindows()
