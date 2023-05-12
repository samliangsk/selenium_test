# selenium_test

This is a test repo for selenium and SeleniumBase.

## docker run

use v4l2loopback to setup video60.

`sudo modprobe v4l2loopback devices=1 video_nr=60 card_label=\"VirtCam\" exclusive_caps=1 max_buffers=2`

pass video60 in when run `docker run --device /dev/video60`


**google_signin.py** uses SeleniumBase to sign in Google, join and leave Google Meet. Also collecting webRTC dump.

Login verification error might occur, currently trying to fix/go around such error.
