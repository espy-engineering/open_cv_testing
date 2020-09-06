import cv2
import numpy as np

test = cv2.imread('IMG_2253.JPG')

test_gray = cv2.cvtColor(test, cv2.COLOR_BGR2GRAY)
test_blur = cv2.GaussianBlur(test_gray, (9, 9), 0)
test_edge = cv2.Canny(test, 50, 50)
test_cropped = test[0:100, 200:500]
cv2.imshow('test', test)
cv2.imshow('test_gray', test_gray)
cv2.imshow('test_blur', test_blur)
cv2.imshow('test_edge', test_edge)
cv2.imshow('cropped', test_cropped)
cv2.waitKey(0)

# video = cv2.VideoCapture('IMG_3971.m4v')
#
# while True:
#     success, image = video.read()
#     cv2.imshow('test', image)
#     if cv2.waitKey(1) & 0xFF ==ord('q'):
#         break

#
# video = cv2.VideoCapture(0)
# video.set(3, 1920)
# video.set(4, 1080)
# video.set(10, 1000)
#
# while True:
#     success, image = video.read()
#     cv2.imshow('test', image)
#     if cv2.waitKey(10) & 0xFF ==ord('q'):
#         break


print('Done')
