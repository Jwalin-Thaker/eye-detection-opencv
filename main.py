import cv2

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_eye_tree_eyeglasses.xml')

# vairable decalarations
device_index = 0
window_x = 640
window_y = 480
total_time = 0
init_time = 150


def set_video_capture_parameters(cap):
    """
        Sets all the capture parameters for the video stream
        @param -> [cap] - capture object
        @return -> None
    """
    cap.set(3, window_x)
    cap.set(4, window_y)
    cap.set(10, 10)


def initialize_camera(device_index):
    """
        Initialize the video stream from camera
        @param -> [device_index] - to bind hardware
        @return -> [cap] - video capture object
    """
    cap = cv2.VideoCapture(device_index)
    return cap


def detect_faces(img, gray):
    """
        Converts image to grayscale and applies pretrained haar cascade of frontal face
        detection to get relevant data points of the face
        @param -> [img] - frame captured from hardware | [gray] - grayscale version of image
        @return -> [faces] - face related info | [faces_present] - are faces peresent | [total_faces] - total # of faces
    """
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    total_faces = len(faces)
    faces_present = total_faces > 0
    for face in faces:
        (x, y, w, h) = face
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    return faces, faces_present, total_faces


def detect_eyes(img, gray, face):
    """
        Highlights the eyes in a detected face
        @param -> [img] - frame captured from hardware | [gray] - grayscale version of image
        @return -> [eyes] - eye related info | [total_eyes] - total number of eyes detected
    """
    (x, y, w, h) = face
    roi_gray_face = gray[y:y + h, x:x + w]
    roi_color_face = img[y:y + h, x:x + w]
    eyes = eye_cascade.detectMultiScale(
        roi_gray_face, 1.1, 5, minSize=(30, 30), maxSize=(80, 80))
    total_eyes = len(eyes)
    for eye in eyes:
        (ex, ey, ew, eh) = eye
        cv2.rectangle(roi_color_face, (ex, ey),
                      (ex + ew, ey + eh), (0, 255, 0), 2)
    return eyes, total_eyes


def read_eyes(face, eyes, total_eyes):
    """
        Tracks the eyes around the region of interest to draw insights
        @param -> [face] - face related info | [eyes] - eye related info | [total_eyes] - total number of eyes detected
        @return -> None
    """
    (x, y, w, h) = face
    text_position = (int(x), int(y + (12 * h / 10)))
    if total_eyes >= 2:
        cv2.putText(img, 'Eyes open', text_position,
                    cv2.FONT_HERSHEY_PLAIN, 3, (100, 100, 0), 2)
    elif total_eyes == 1:
        positional_ratio = eyes[0][0] / abs(w - eyes[0][0])
        if positional_ratio >= 1.0:
            cv2.putText(img, 'Right closed', text_position,
                        cv2.FONT_HERSHEY_PLAIN, 3, (100, 100, 0), 2)
        else:
            cv2.putText(img, 'Left closed', text_position,
                        cv2.FONT_HERSHEY_PLAIN, 3, (100, 100, 0), 2)
    elif total_eyes == 0:
        cv2.putText(img, 'Eyes closed', text_position,
                    cv2.FONT_HERSHEY_PLAIN, 3, (100, 100, 0), 2)
    else:
        pass


# CODE BEGINS
if __name__ == '__main__':
    print('####### Welcome to DATE Algorithm ########')
    print('~~ Detection And Tracking Eye Algorithm ~~')
    cap = initialize_camera(device_index)
    set_video_capture_parameters(cap)
    while cap.isOpened():
        total_time += 1
        success, img = cap.read()
        if not success:
            raise 'Reading from video capture failed'
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces, faces_present, total_faces = detect_faces(img, gray)
        start = total_time > init_time
        if start:
            if faces_present:
                cv2.putText(img, '{} face(s) detected'.format(total_faces), (100, 50),
                            cv2.FONT_HERSHEY_PLAIN, 3, (0, 100, 0), 2)
                for face in faces:
                    eyes, total_eyes = detect_eyes(img, gray, face)
                    read_eyes(face, eyes, total_eyes)
            else:
                cv2.putText(img, 'No face detected', (100, 50),
                            cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 2)
        else:
            cv2.putText(img, 'Initializing DATE...', (100, 50),
                        cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 2)
        cv2.imshow('Video Camera', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
    print('####### End ########')
