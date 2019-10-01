import cv2

capture = cv2.VideoCapture(cv2.CAP_DSHOW)


fourcc = cv2.VideoWriter_fourcc(*'DIVX')
sz = (int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
fps = 20
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

vout = cv2.VideoWriter()
vout.open('output.mp4',fourcc,fps,sz,True)


cnt = 0
while True:
    ret, frame = capture.read()
    vout.write(frame)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

vout.release()
capture.release()
cv2.destroyAllWindows()	
