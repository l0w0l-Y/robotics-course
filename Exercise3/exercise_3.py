import cv2

# =============================================================================
# Exercise 3: Record a video from a webcam to a mp4-file with OpenCV.
# =============================================================================

# Takes a video stream from a webcam.
videoCapture = cv2.VideoCapture(0)

# Decodes and returns the next video frame.
retval, frame = videoCapture.read()

# Video frame width.
width = frame.shape[0]

# Video frame height.
height = frame.shape[1]

# The video codec specifies how the video stream is compressed.
fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')

# Opens a video stream with parameters.
videoWriter = cv2.VideoWriter('video/output.avi', fourcc, 24.0, (height, width))

while videoCapture.isOpened():
    # Decodes and returns the next video frame.
    retval, frame = videoCapture.read()
    # If the file exists, writes it to the video stream. Otherwise, breaks the loop.
    if retval:
        # Writes a frame to a video stream.
        videoWriter.write(frame)
        # Updates frame on the window.
        cv2.imshow('camera', frame)
        # Contains index of pressed key.
        key = cv2.waitKey(20) & 0xFF
        # Enters ESC button.
        if key == 27:
            break
    else:
        break

# Closes video file or capturing device.
videoCapture.release()

# Closes the video writer.
videoWriter.release()

# Closes all windows.
cv2.destroyAllWindows()
