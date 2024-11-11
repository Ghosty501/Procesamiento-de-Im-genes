import cv2 as cv 

cap = cv.VideoCapture(0)

if cap.isOpened():
    while True:
        frame = cap.read()[1]
        print(type(frame))
        cv.imshow("FRAME", frame)
        
        if cv.waitKey(33):
            break
        
        
else:
    print("No se inicializó la webcam")

cap.release()

cv.destroyAllWindows()
