import cv2 as cv
import numpy as np
import pandas as pd

#camera = cv.VideoCapture(0)  # get video from camera
# camera = cv.VideoCapture("E:/Gloppiness_project/drop/HG/Xanthan_HG_200FPS_0.1ml_drop1_000000.avi")
camera = cv.VideoCapture("data/demo.avi")
count  = 0
filament_diameter = []
while camera.isOpened():
    ret, frame = camera.read()

    if ret:
        edges = cv.Canny(frame, 120, 120)
        cv.imshow('Canny', edges)
        
        rows, cols = len(edges), len(edges[0])
        left_edges, right_edges = [], []
        for i in range(rows):
            for j in range(cols):
                if edges[i][j] == 255:
                    left_edges.append(j)
                    break

        for i in range(rows):
            for j in range(cols-1, -1, -1):
                if edges[i][j] == 255:
                    right_edges.append(j)
                    break

        filament_diameter.append(np.subtract(right_edges, left_edges))

        count += 1
        camera.set(cv.CAP_PROP_POS_FRAMES, count)
    else:
        camera.release()
        break

    if cv.waitKey(5) == ord('x'):
        break
camera.release()
cv.destroyAllWindows()


df_filament_diameter = pd.DataFrame(filament_diameter).T
df_filament_diameter.shape
df_filament_diameter.to_csv('data/filament_diameter.csv')

# filament_diameter = []
# while True:

#     ret, frame = camera.read()
#     # cv.imshow('Camera',frame)
#     # laplacian = cv.Laplacian(frame, cv.CV_64F)
#     # laplacian = np.uint8(laplacian)
#     # cv.imshow('Laplacian', laplacian)
    
#     edges = cv.Canny(frame, 120, 120)
# #     print(edges.max())
# #     print(edges.min())
# #     print(len(edges))
# #     print(len(edges[0]))
    
#     cv.imshow('Canny', edges)
    
# ##########################################################
#     rows, cols = len(edges), len(edges[0])
    
#     left_edges, right_edges = [], []
#     for i in range(rows):
#         for j in range(cols):
#             if edges[i][j] == 255:
#                 left_edges.append(j)
#                 break
#     for i in range(rows):
#         for j in range(cols-1, -1, -1):
#             if edges[i][j] == 255:
#                 right_edges.append(j)
#                 break
#     filament_diameter.append(np.subtract(right_edges, left_edges))
    
# ############################################################
    
#     if cv.waitKey(5) == ord('x'):
#         break
# camera.release()
# cv.destroyAllWindows()


# df_filament_diameter = pd.DataFrame(filament_diameter).T
# df_filament_diameter.shape
# df_filament_diameter.to_csv('data/filament_diameter.csv')

