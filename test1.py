import cv2
import numpy as np

# test = cv2.imread('IMG_2253.JPG')
#
# test_gray = cv2.cvtColor(test, cv2.COLOR_BGR2GRAY)
# test_blur = cv2.GaussianBlur(test_gray, (9, 9), 0)
# test_edge = cv2.Canny(test, 50, 50)
# test_cropped = test[0:100, 200:500]
# cv2.imshow('test', test)
# cv2.imshow('test_gray', test_gray)
# cv2.imshow('test_blur', test_blur)
# cv2.imshow('test_edge', test_edge)
# cv2.imshow('cropped', test_cropped)
# cv2.waitKey(0)

# video = cv2.VideoCapture('IMG_3971.m4v')
#
# while True:
#     success, image = video.read()
#     cv2.imshow('test', image)
#     if cv2.waitKey(1) & 0xFF ==ord('q'):
#         break


video = cv2.VideoCapture(0)
video.set(3, 640)
video.set(4, 360)
video.set(10, 50)

while True:
    success, original = video.read()
    grey_scaled = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    edge_detected = cv2.Canny(grey_scaled, 75, 75)
    edge_detected_2 = cv2.Canny(original, 75, 75)
    # edge_detected = edge_detected[:, :, np.newaxis]
    # displayed = np.concatenate((original, edge_detected), axis=1)
    cv2.imshow('Original', original)
    cv2.imshow('Edges', edge_detected)
    cv2.imshow('Edges 2', edge_detected_2)
    cv2.imshow('Grey', grey_scaled)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break


print('Done')
