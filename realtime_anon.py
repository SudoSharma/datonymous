import dlib
import cv2
from imutils import face_utils, video
from sklearn.cluster import KMeans
import numpy as np


def hog_detector(image, gray):
    # Get faces into webcam's image
    rects = detector(gray, 0)
    # For each detected face, find the landmark.
    for (i, rect) in enumerate(rects):
        # Make the prediction and transfom it to numpy array
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)

        # Cluster
        ZZ = np.array(shape)
        kmeans = KMeans(n_clusters=3, random_state=0).fit(ZZ)
        ppa = [x[0] for x in kmeans.cluster_centers_]
        ppb = [x[1] for x in kmeans.cluster_centers_]

        for a, b in zip(ppa, ppb):
            a = int(a)
            b = int(b)
            cv2.circle(image, (a, b), 50, (0, 0, 0), -1)
                   

def facial_landmarks():
    # Feed from computer camera with threading
    cap = video.VideoStream(src=0).start()

    while True:
        # Getting out image by webcam
        image = cap.read()

        # Converting the image to gray scale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        hog_detector(image, gray)

        # show the output frame
        # adding brightness and contrast -> α⋅p(i,j)+β where p(i.j) is pixel value for each point
        image = cv2.convertScaleAbs(image, alpha=1.0, beta=0)
        cv2.imshow("Facial Landmarks", image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
    cap.stop()

if __name__ == "__main__":
    predictor = dlib.shape_predictor('model.dat')
    detector = dlib.get_frontal_face_detector()
    facial_landmarks()
