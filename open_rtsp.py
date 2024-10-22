import cv2

cv2.namedWindow("RTSP View", cv2.WINDOW_NORMAL)
cap = cv2.VideoCapture("rtsp://localhost:8554/video_stream")

while True:
    ret, frame = cap.read()
    if ret:
        cv2.imshow("RTSP View", frame)

        # Wait for 1 ms and check if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Quitting...")
            break
    else:
        print("Unable to open camera")
        break

cap.release()
cv2.destroyAllWindows()
