import subprocess
import cv2

subprocess.Popen('ffmpeg -hide_banner -loglevel error -stream_loop -1 -re -i ./fake_video.flv -c copy -f v4l2 /dev/video0',shell=True)



# Open the first camera connected to the computer
cap = cv2.VideoCapture(0)

# Set the video codec to MP4V
fourcc = cv2.VideoWriter_fourcc(*'MP4V')

# Set the video recording parameters
fps = 30.0
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv2.VideoWriter('output.mp4', fourcc, fps, (frame_width, frame_height))

# Record video for 30 seconds
duration = 30.0  # seconds
start_time = cv2.getTickCount()
while (cv2.getTickCount() - start_time) / cv2.getTickFrequency() < duration:
    ret, frame = cap.read()
    if ret:
        out.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the camera and the video writer
cap.release()
out.release()

# Close all windows
cv2.destroyAllWindows()
