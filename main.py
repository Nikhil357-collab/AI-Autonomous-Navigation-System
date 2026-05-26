import cv2
import time

from detection.object_detection import detect_objects
from detection.lane_detection import detect_lanes
from detection.collision_warning import collision_warning

from  detection.steering_logic import navigation_decision

from  detection.dashboard import draw_dashboard

########################################
# OPEN VIDEO
########################################

cap = cv2.VideoCapture(
    "AI_Based_Navigation_System/road_video.mp4"
)

# Webcam option
# cap = cv2.VideoCapture(0)

if not cap.isOpened():

    print("ERROR: Cannot open video")

    exit()

########################################
# FPS VARIABLES
########################################

prev_time = 0

########################################
# MAIN LOOP
########################################

while True:

    success, frame = cap.read()

    if not success:

        print("Video Finished")

        break

    ####################################
    # RESIZE FRAME
    ####################################
    frame = cv2.resize(frame, (800, 680))

    ####################################
    # OBJECT DETECTION
    ####################################

    detected_frame, object_count, results = detect_objects(frame)

    ####################################
    # LANE DETECTION
    ####################################

    lane_frame, lane_center = detect_lanes(
        detected_frame
    )

    ####################################
    # STEERING LOGIC
    ####################################

    frame_center = frame.shape[1] // 2

    steering, speed, horn = navigation_decision(
        lane_center,
        frame_center,
        object_count
    )

    ####################################
    # COLLISION WARNING
    ####################################

    risk = collision_warning(object_count)

    ####################################
    # AI STATUS
    ####################################

    if object_count > 0:

        status = "ACTIVE - OBSTACLE DETECTED"

    else:

        status = "ACTIVE - ROAD CLEAR"

    ####################################
    # FPS
    ####################################

    current_time = time.time()

    fps = int(
        1 / (current_time - prev_time)
    )

    prev_time = current_time

    ####################################
    # DASHBOARD
    ####################################

    final_frame = draw_dashboard(
        lane_frame,
        status,
        object_count,
        fps,
        steering,
        speed,
        horn,
        risk
    )

    ####################################
    # CENTER GUIDELINE
    ####################################

    cv2.line(
        final_frame,
        (frame_center, 0),
        (frame_center, 480),
        (255,255,255),
        2
    )

    ####################################
    # SHOW WINDOW
    ####################################

    cv2.imshow(
        "AI Autonomous Navigation System",
        final_frame
    )

    ####################################
    # EXIT BUTTON
    ####################################

    key = cv2.waitKey(1)

    if key == ord('q'):

        print("Exiting System")

        break

########################################
# RELEASE
########################################

cap.release()

cv2.destroyAllWindows()