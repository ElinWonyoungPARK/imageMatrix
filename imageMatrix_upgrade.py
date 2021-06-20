def verticalLine(imgMatrix, patternPeriod=100, vTilt=1081, fgR=0, fgG=0, fgB=0, bgR=255, bgG=255, bgB=255):
    '''
    Draw vertical line pattern
        - imgMatrix : image 를 만들어 저장할 numpy array
        - patternPeriod : pattern 이 반복되는 주기
        - vTilt : vertical line 몇개마다 horizonal line 이 1-pixel shift 되어 tilt 효과가 나오는지
        - fgR/fgB/fgB : foreground color [0~255]
        - bgR/bgB/bgB : background color [0~255]
    '''
    verticalSize = len(imgMatrix)
    horizontalSize = len(imgMatrix[0])
    colorLayer = len(imgMatrix[0][0])

    for v in range(0, verticalSize):
        for h in range(0, horizontalSize):
            if (((h+v/vTilt)//(patternPeriod/2))%2==1):
                img[v, h, 2] = fgR  # Red layer
                img[v, h, 1] = fgG  # Green layer
                img[v, h, 0] = fgB  # Blue layer


if __name__ == '__main__':

    #import modules
    import numpy as np
    import cv2

    # resolution setting
    horizontalResolution = 1920
    verticalResolutuion = 1080
    colorLayer = 3
    windowName = 'pattern'

    # background color setting
    bgR = 255
    bgG = 255
    bgB = 255

    # foreground color setting
    fgR = 255
    fgG = 0
    fgB = 0 

    # pattern form parameter
    patternPeriod = 50 # horizontal pattern period
    verticalTilt = 1081    # vertical tilt

    # image 를 외부에서 불러 오는 경우
    '''
    img = cv2.imread("C:/Code/Python/openCV/imageLib/fruits.jpg")
    if img is None:
        print('Image load failed')
        sys.exit()
    '''

    # image 를 만드는 경우
    img = np.full((verticalResolutuion, horizontalResolution, colorLayer), (bgB, bgG, bgR), dtype=np.uint8)
        # array generation : (Vertical, Horizontal, RGB) (Blue, Green, Red)

    verticalLine(img, patternPeriod, verticalTilt, fgR, fgG, fgB, bgR, bgG, bgB)

    # full screen display
    cv2.namedWindow(windowName, cv2.WINDOW_GUI_EXPANDED)
    cv2.setWindowProperty(windowName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    # screen 에 display
    cv2.imshow(windowName,img)
    cv2.waitKey()
    cv2.destroyAllWindows()
