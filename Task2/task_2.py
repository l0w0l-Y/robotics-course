import numpy as np
import copy
import cv2
from numpy import float32

# =============================================================================
# Task 2: One practical application of warping in OpenCV
# can be to warp an image into a smaller one with a mouse clicking.
# Need to implement image deformation on mouse click.
# =============================================================================

# The name of the editor window.
window_name = "Editor window"

# Entering the wrapped image width.
width = int(input("Enter the wrapped image width: "))

# Entering the wrapped image height.
height = int(input("Enter the wrapped image height: "))

# Containing the editing image name.
img_name = "cards_image.jpg"

# Image reading. It doesn't change.
init_img = cv2.imread(img_name)

# Image that changes in the program.
img = cv2.imread(img_name)

# Saving image to cache
cache = img

# Count of selected points. Can wrapping the image if the number of points is 4.
pointCount = 0

# Whether the images returned to the cache.
isBack = False

# The array that contains the coordinates of the selected points.
wrappedImagePoints = np.zeros((4, 2), float32)

# Path to save cropped images.
save_path = "wrapped_images"


# Drawing circle on the image.
def draw_circle(event, x, y, flags, param):
    # Using global values.
    global img
    global cache
    global pointCount
    global wrappedImagePoints
    global isBack
    # Event is equal to double-clicking the left mouse button.
    if event == cv2.EVENT_LBUTTONDBLCLK:
        # Saving condition image on the cache.
        cache = copy.deepcopy(img)
        # Added new cache. Haven't called it yet.
        isBack = False
        # Adding a point to the array.
        wrappedImagePoints[pointCount] = [float32(x), float32(y)]
        # Increasing a point count.
        pointCount += 1
        # Drawing circle on the image.
        cv2.circle(img, (x, y), 5, (255, 0, 230), -1)
    else:
        # Event is equal to clicking the right mouse button.
        if event == cv2.EVENT_RBUTTONDOWN:
            if pointCount > 0:
                if not isBack:
                    # Returning condition image from the cache.
                    img = copy.deepcopy(cache)
                    # Have called cache.
                    isBack = True
                    # Reducing a point count.
                    pointCount -= 1


# Showing the image.
cv2.imshow(window_name, img)

# Setting mouse callback function to the window.
cv2.setMouseCallback(window_name, draw_circle)
while True:
    # Constantly refreshing the image.
    cv2.imshow(window_name, img)
    # Containing index of pressed key.
    key = cv2.waitKey(20) & 0xFF
    # Entering ESC button.
    if key == 27:
        break
    # Entering Space button.
    if key == ord(' '):
        if pointCount == 4:
            sideMatrix = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
            # Getting perspective transform with 2 float arrays.
            matrix = cv2.getPerspectiveTransform(wrappedImagePoints, sideMatrix)
            # The wrapped image.
            wrappedImg = cv2.warpPerspective(init_img, matrix, (width, height))
            # Destroying the original image window
            cv2.destroyWindow(window_name)
            # Saving the wrapped image.
            cv2.imwrite(f"{save_path}/wrapped_image_{img_name}", wrappedImg)
            # Showing the wrapped image.
            cv2.imshow("Wrapped_image", wrappedImg)
            # Doesn't close the window when the code ends.
            cv2.waitKey(0)
            # Breaking out of the eternal loop.
            break
