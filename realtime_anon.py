import dlib
import cv2
from imutils import face_utils, video
from sklearn.cluster import KMeans
import numpy as np


def anonymizer(image, gray):
    """Anonymize faces using keypoints and clustering on biometric zones."""
    rects = detector(gray, 0)
    for (i, rect) in enumerate(rects):
        # Predict keypoints
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)

        # Cluster
        group = np.array(shape)
        kmeans = KMeans(n_clusters=3, random_state=0).fit(group)
        ppa = [x[0] for x in kmeans.cluster_centers_]
        ppb = [x[1] for x in kmeans.cluster_centers_]

        # Draw cluster on biometric identity zones
        for a, b in zip(ppa, ppb):
            a = int(a)
            b = int(b)
            cv2.circle(image, (a, b), 50, (0, 0, 0), -1)
                   

def process_video():
    """Process video and handle user commands."""
    # Feed from computer camera with threading
    cap = video.VideoStream(src=0).start()

    while True:
        # Read image, anonymize, and wait for user quit.
        image = cap.read()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        anonymizer(image, gray)
        image = cv2.convertScaleAbs(image, alpha=1.0, beta=0)
        cv2.imshow("Realtime Anon", image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
    cap.stop()

if __name__ == "__main__":
    predictor = dlib.shape_predictor('model.dat')
    detector = dlib.get_frontal_face_detector()
    process_video()
