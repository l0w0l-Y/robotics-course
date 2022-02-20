import cv2
import os

# =============================================================================
# Task1: Split an image into several other images of a certain length and width.
# Save all received images to the original folder.
# =============================================================================

# Entering the size of the cropped images.
stepXY = int(input("Enter the size of the cropped image: "))

# Path to save cropped images.
save_path = "cropped_images"

# Image reading.
img = cv2.imread("photo_test.jpg")

# Image width.
imgXMax = img.shape[0]

# Image height.
imgYMax = img.shape[1]


# Cropping the image. Showing it and writing it to a specific directory.
def readAndShowCroppedImage(i, j, step):
    # Cropping the image from i pixel to i + step pixel x-axis and j to j+step y-axis.
    imgCropped = img[i:i + step, j: j + step]
    # Showing the cropped image.
    cv2.imshow(f"cropped_image_{str(i)}_{str(j)}", imgCropped)
    # Saving the cropped image in current directory.
    cv2.imwrite(f"{save_path}/{stepXY}/cropped_image_{str(i)}_{str(j)}.jpg", imgCropped)


# If the step size is larger than the image size, cropping is not possible.
if (stepXY > imgXMax) or (stepXY > imgYMax):
    print("You can't crop the image. Step larger than the image size.")
else:
    # Directory path to save images.
    path = os.path.join(save_path, str(stepXY))
    # If the directory with path doesn't exist, it creates a new one. Otherwise, it deletes all files from it.
    if not os.path.isdir(path):
        # Create new directory with path.
        os.makedirs(path)
    else:
        # Getting all files from directory with path.
        allfiles = os.listdir(path)
        for file in allfiles:
            filePath = os.path.join(path, file)
            # Delete file.
            os.remove(filePath)

    for x in range(0, imgXMax, stepXY):
        for y in range(0, imgYMax, stepXY):
            # If a piece of the leftover image is smaller than our step, we do not crop it,
            # because we only need images of the height and width of this step.
            if (imgYMax - y) < stepXY or (imgXMax - x) < stepXY:
                break
            else:
                readAndShowCroppedImage(x, y, stepXY)
# Doesn't close the window when the code ends.
cv2.waitKey(0)
