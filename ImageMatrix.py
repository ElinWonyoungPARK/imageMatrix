#%%

#import modules
import numpy as np
import cv2
import sys

# resolution setting
H_RES = 1920
V_RES = 1080
C_LAYER = 3
win_name = 'pattern'

# background color setting
bg_R = 255
bg_G = 255
bg_B = 255

# foreground color setting
fg_R = 0
fg_G = 0
fg_B = 0 

# pattern form parameter
p_period = 500    # horizontal pattern period
v_tilt = 1080    # vertical tilt

# image 를 외부에서 불러 오는 경우
'''
img = cv2.imread("C:/Code/Python/openCV/imageLib/fruits.jpg")
if img is None:
    print('Image load failed')
    sys.exit()
'''

# image 를 만드는 경우
img = np.full((V_RES, H_RES, C_LAYER), (bg_B, bg_G, bg_R), dtype=np.uint8)
    # array generation : (Vertical, Horizontal, RGB) (Blue, Green, Red)


for v in range(0, V_RES):
    for h in range(0, H_RES):
        if (((h+v/v_tilt)//(p_period/2))%2==1):
            img[v, h, 2] = fg_R  # Red layer
            img[v, h, 1] = fg_G  # Green layer
            img[v, h, 0] = fg_B  # Blue layer


# full screen display
cv2.namedWindow(win_name, cv2.WINDOW_GUI_EXPANDED)
cv2.setWindowProperty(win_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# window location setting(name, x, y)
#cv2.moveWindow(win_name, 300, 200)
# screen display
cv2.imshow(win_name,img)
cv2.waitKey()
cv2.destroyAllWindows()


# save file as bmp
#cv2.imwrite('C:/Users/User/OpenCv/image.bmp', img)
