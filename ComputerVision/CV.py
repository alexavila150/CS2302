import cv2


def convertToGray(image):
    # for i in range(image.shape[0]):
    #   for j in range(image.shape[1]):
    # avg = (.3 * image[i][j][0] + .3 * image[i][j][1] + .3 * image[i][j][2])
    # image[i][j][0] = avg
    # image[i][j][1] = avg
    # image[i][j][2] = avg
    #      image[i][j][0] = 255 - image[i][j][0]
    #     image[i][j][1] = 255 - image[i][j][1]
    #    image[i][j][2] = 255 - image[i][j][2]
    return 255 - image


# Get first camera that it finds open
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Operation to do on the frame
    frame = convertToGray(frame)
    # cv2 implementation of it -> gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
