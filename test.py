import cv2
import sys
from filter import *
import numpy as np
if __name__ == '__main__':
    tracker = cv2.TrackerMOSSE_create()
    cap = cv2.VideoCapture(0)
    cap_height=480
    cap_width=640
    cap.set(3, cap_width)
    cap.set(4, cap_height)
    if not cap.isOpened():
        print("Failed to open camera")
        sys.exit()

    ok, frame = cap.read()
    if not ok:
        print('Failed to read camera')
        sys.exit()
    print(frame.shape)
    bbox = cv2.selectROI(frame, False)
    ok = tracker.init(frame, bbox)

    while True:
        ok, frame = cap.read()
        if not ok:
            break

        timer = cv2.getTickCount()
        ok, bbox = tracker.update(frame)

        fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
        if ok:
            p1 = (int(bbox[0]), int(bbox[1]))
            p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
            cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)
            xcp,ycp=aim(bbox)
            xcp=int(xcp)
            ycp=int(ycp)
        else:
            cv2.putText(frame, "Tracking failure detected", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
            xcp,ycp=get_current_x()
            xcp=int(xcp)
            ycp=int(ycp)
        cv2.circle(frame, (xcp,ycp), radius=2, color=(0,0,255), thickness=1)

        cv2.putText(frame, "FPS : " + str(int(fps)), (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2);

        cv2.imshow("Tracking", frame)

        k = cv2.waitKey(1) & 0xff
        if k == 27: break #esc
