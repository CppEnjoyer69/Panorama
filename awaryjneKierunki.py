import cv2

Dirs = ['E', 'S', 'W']
m_Dirs = ['NE', 'SE', 'SW', 'NW']


def click_event(event, x, y, flags, params):

    if event == cv2.EVENT_LBUTTONDOWN:
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(image, "N", (x - 8,y - 30), font,
                        1, (0, 30, 255), 2)
        cv2.putText(image, "|", (x, y), font,
                        1, (255, 0, 255), 2)
        pos = x
       
        for dir in Dirs:
            pos += step
            pos %= panoWidth
            cv2.putText(image, dir, (pos - 8, y - 30), font,
                        1, (255, 80, 0), 2)
            cv2.putText(image, "|", (pos, y), font,
                            1, (255, 0, 255), 2)
            
        m_pos = int(x + step/2)
        for dir in m_Dirs:
            cv2.putText(image, dir, (m_pos - 12, y - 30), font,
                        0.6, (255, 150, 0), 2)
            cv2.putText(image, "|", (m_pos, y), font,
                            0.6, (255, 0, 255), 2)
            m_pos += step
            m_pos %= panoWidth  
            
        cv2.imwrite('PANORAMA.jpg', image)
        cv2.destroyAllWindows()

if __name__ == '__main__':

    image = cv2.imread('car.jpg') #dajecie tu nazwe zdjecia 
    panoWidth = image.shape[1]
    step = int(panoWidth / 4)

    cv2.imshow('image', image)
    cv2.setMouseCallback('image', click_event)
    cv2.waitKey(0)

    cv2.destroyAllWindows()

