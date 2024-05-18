import cv2

Dirs = {
    1 : "EAST",
    2 : "SOUTH",
    3 : "WEST"
}

cap = cv2.VideoCapture(2)
cap.set(cv2.CAP_PROP_FPS, 30)
images = []
err_dict = {
    cv2.STITCHER_OK: "STITCHER_OK",
    cv2.STITCHER_ERR_NEED_MORE_IMGS: "STITCHER_ERR_NEED_MORE_IMGS",
}

def takePicture():
    _, img = cap.read()
    img = cv2.resize(img, (1080,720))
    images.append(img)
    
def Panorama(imgs):
    stitcher = cv2.Stitcher.create()
    (retval, stitchedImage) = stitcher.stitch(imgs)
    
    if retval!= cv2.STITCHER_OK: 
        print(f"stitching falied with error code {retval} : {err_dict[retval]}")
        exit(retval)
    else:
        print('Your Panorama is ready!!!')  
        cv2.imwrite("panorama.jpg", stitchedImage)    

def click_event(event, x, y, flags, params):

    if event == cv2.EVENT_LBUTTONDOWN:
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(image, "NORTH", (x - 50,y - 30), font,
                        1, (0, 0, 255), 2)
        cv2.putText(image, "|", (x, y), font,
                        1, (255, 0, 255), 2)
        pos = x
        for i in range(1,4):
            pos += step 
            pos %= panoWidth
            cv2.putText(image, Dirs.get(i), (pos - 50, y - 30), font,
                        1, (0, 0, 255), 2)
            cv2.putText(image, "|", (pos, y), font,
                            1, (255, 0, 255), 2)
            
        cv2.imwrite('text.jpg', image)
        cv2.destroyAllWindows()
    

if __name__ == '__main__':
    # counter = 0
    # while counter <= 9:
    #     if(input("PRESS 'ENTER' ") == ''):
    #         takePicture()
    #         counter+=1

    # Panorama(images)
    image = cv2.imread('kutas.jpg')
    panoWidth = image.shape[1]
    step = int(panoWidth / 4)
    cv2.imshow('image', image)
    cv2.setMouseCallback('image', click_event)
    cv2.waitKey(0)

    cv2.destroyAllWindows()

