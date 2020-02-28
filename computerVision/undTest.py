import cv2
import sys
import numpy as np
DIM=(480, 480)
K=np.array([[137.47480192731283, 0.0, 233.15271191197178], [0.0, 136.51222480271173, 238.0308498249484], [0.0, 0.0, 1.0]])

D=np.array([[0.08358109300208671], [0.03019361080419839], [-0.05440030778498185], [0.013300415794029468]])

def undistort(img_path):
    img = cv2.imread(img_path)
    h,w = img.shape[:2]
    map1, map2 = cv2.fisheye.initUndistortRectifyMap(K, D, np.eye(3), K, DIM, cv2.CV_16SC2)
    undistorted_img = cv2.remap(img, map1, map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
    cv2.imshow("undistorted", undistorted_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == '__main__':
    for p in sys.argv[1:]:
        undistort(p)
