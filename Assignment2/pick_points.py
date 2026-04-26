import cv2 as cv
import numpy as np

N = 6
global n
n = 0
p1 = np.empty((N, 2))
p2 = np.empty((N, 2))

def draw_circle(event, x, y, flags, param):
    global n
    p = param[0]
    if event == cv.EVENT_LBUTTONDOWN and n < N:
        cv.circle(param[1], (x, y), 5, (0, 0, 255), -1)
        cv.putText(param[1], str(n + 1), (x + 8, y - 8),
                   cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
        p[n] = (x, y)
        n += 1

im1 = cv.imread("c1.jpg", cv.IMREAD_REDUCED_COLOR_4)
im2 = cv.imread("c2.jpg", cv.IMREAD_REDUCED_COLOR_4)
im1copy = im1.copy()
im2copy = im2.copy()

cv.namedWindow("Image 1", cv.WINDOW_AUTOSIZE)
cv.setMouseCallback("Image 1", draw_circle, [p1, im1copy])
while True:
    cv.imshow("Image 1", im1copy)
    if n == N: break
    if cv.waitKey(20) & 0xFF == 27: break

n = 0
cv.namedWindow("Image 2", cv.WINDOW_AUTOSIZE)
cv.setMouseCallback("Image 2", draw_circle, [p2, im2copy])
while True:
    cv.imshow("Image 2", im2copy)
    if n == N: break
    if cv.waitKey(20) & 0xFF == 27: break

cv.destroyAllWindows()
print("pts1 =", repr(p1))
print("pts2 =", repr(p2))
