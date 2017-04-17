import cv2
import sys

if name == __main__:
    #set up the tracker for the object tracking
    tracker = cv2.Tracker_create("MIL")
    #initialize the stream of video
    vid_stream = cv2.VideoCapture(/home/video.mp4)

    if not vid_stream.isOpened():
        print "Set the path properly\
                Video Could be opened"
        sys.exit()

    #check whether video is fone or not
    ret, frame = vid_stream.read()
    if not ret:
        print "Cannot read video.Try again!"
        sys.exit()
    #modify the box as per requirement

    bound_box = (100,100,100,100)

    #initialize the tracker
    ret = tracker.init(frame,bound_box)

    #start streaming the video
    while True:
        ret,frame = vid_stream.read()
        if not ret:
            break
        ret,bound_box= tracker.update(frame)
        #show box in video
        if ret:
            para1 = (int(bound_box[0]),int bound_box[1])
            para2 = (int(bound_box[0] + bound_box[2]), int(bound_box[1] + bound_box[3]))


        cv2.imshow("Ongoing Tracking",frame)
        #ESC to exit.
        key = cv2.waitKey(1) & 0xff
        if key==27:
            break
