import numpy as np
import copy
import cv2
from numpy import float32

# =============================================================================
# Exercise 2: One practical application of warping in OpenCV
# can be to warp an image into a smaller one with a mouse clicking.
# Need to implement image deformation on mouse click.
# =============================================================================

# The name of the editor window.
window_name = "Editor window"

# Enters the wrapped image width.
width = int(input("Enter the wrapped image width: "))

# Enters the wrapped image height.
height = int(input("Enter the wrapped image height: "))

# Contains the editing image name.
img_name = "cards_image.jpg"

# Gets an Image. It doesn't change.
init_img = cv2.imread(img_name)

# Gets an Image. Image that changes in the program.
img = cv2.imread(img_name)

# Saves image to cache.
cache = img

# Count of selected points. Can wrap the image if the number of points is 4.
pointCount = 0

# Whether the images returned to the cache.
isBack = False

# The array that contains the coordinates of the selected points.
wrappedImagePoints = np.zeros((4, 2), float32)

# Path to save cropped images.
save_path = "wrapped_images"


# Draws circle on the image.
def draw_circle(event, x, y, flags, param):
    # Uses global values.
    global img
    global cache
    global pointCount
    global wrappedImagePoints
    global isBack
    # Event is equal to double-clicking the left mouse button.
    if event == cv2.EVENT_LBUTTONDBLCLK:
        # Saves condition image on the cache.
        cache = copy.deepcopy(img)
        # Added new cache. Haven't called it yet.
        isBack = False
        # Adds a point to the array.
        wrappedImagePoints[pointCount] = [float32(x), float32(y)]
        # Increases a point count.
        pointCount += 1
        # Draws circle on the image.
        cv2.circle(img, (x, y), 5, (255, 0, 230), -1)
    else:
        # Event is equal to clicking the right mouse button.
        if event == cv2.EVENT_RBUTTONDOWN:
            if pointCount > 0:
                if not isBack:
                    # Returns condition image from the cache.
                    img = copy.deepcopy(cache)
                    # The cache has been returned.
                    isBack = True
                    # Reduces a point count.
                    pointCount -= 1


# Shows the image.
cv2.imshow(window_name, img)

# Sets mouse callback function to the window.
cv2.setMouseCallback(window_name, draw_circle)
while True:
    # Constantly refreshes the image.
    cv2.imshow(window_name, img)
    # Containing index of pressed key.
    key = cv2.waitKey(20) & 0xFF
    # Enters ESC button.
    if key == 27:
        break
    # Enters Space button.
    if key == ord(' '):
        if pointCount == 4:
            sideMatrix = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
            # Gets perspective transform with 2 float arrays.
            matrix = cv2.getPerspectiveTransform(wrappedImagePoints, sideMatrix)
            # The wrapped image.
            wrappedImg = cv2.warpPerspective(init_img, matrix, (width, height))
            # Destroys the original image window
            cv2.destroyWindow(window_name)
            # Saves the wrapped image.
            cv2.imwrite(f"{save_path}/wrapped_image_{img_name}", wrappedImg)
            # Shows the wrapped image.
            cv2.imshow("Wrapped_image", wrappedImg)
            # Doesn't close the window when the code ends.
            cv2.waitKey(0)
            # Breaks out of the eternal loop.
            break
