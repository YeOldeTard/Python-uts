import cv2
from time import sleep

ASCII = "@%#*+=-:. "
# ASCII = "1234567890`~!@#$%^&*()-_=+[{]}|\;:',<.>/? "

Path = "Bad apple.mp4"
cap = cv2.VideoCapture(Path)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    h, w = gray.shape
    new_w = 80
    new_h = int(h * (new_w / w) * 0.5)
    gray = cv2.resize(gray, (new_w, new_h))
    ascii_frame = ""
    for row in gray:
        for px in row:
            ascii_frame += ASCII[int(px / 255 * (len(ASCII)-1))]
        ascii_frame += "\n"

    print("\x1b[H" + ascii_frame)
    sleep(0.03)

