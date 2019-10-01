import cv2

capture = cv2.VideoCapture(cv2.CAP_DSHOW)


while True:
    ret, frame = capture.read()
    cv2.imshow("Video Capture", frame)
    a = cv2.waitKey(1)
    k = a & 0xFF
    if k == 27:
        break


capture.release()
cv2.destroyAllWindows()
