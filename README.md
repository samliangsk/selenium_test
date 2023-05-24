# selenium_test

This is a test repo for selenium and SeleniumBase.

## docker run

use v4l2loopback to setup video64 outside of docker.

seems like ffmpeg and v4l2 or video devices could only function when there are video0, so we also need to create video0

`sudo modprobe v4l2loopback devices=2 video_nr=0,64 exclusive_caps=1,1`

pass video64 in when run `docker run (-it) --privileged debian`

## python code

**check_cam.py** buggy temperable testing file used to test video

**google_signin.py** uses SeleniumBase to sign in Google, join and leave Google Meet. Also collecting webRTC dump.

Login verification error solved, use phone number to circumvent
