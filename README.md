# selenium_test

This is a repo that built for testing and data collection of WebRTC and WebRTC based video conferencing QoS/QoE in docker. It automatically login to Google and create/join/quit Google Meets. It is based on selenium and SeleniumBase.

## V4L2 loopback

v4l2loopback - a kernel module to create V4L2 virtual video devices (virtual camera).

use v4l2loopback to setup /dev/video0 and /dev/video64 **outside of docker**.

V4L2loopback could only function when there are video0, so we also need to create video0.

`sudo modprobe v4l2loopback devices=2 video_nr=0,64 exclusive_caps=1,1`

## ALSA/PulseAudio

**Currently under construction**

virtual microphone that enable audio input to the meeting.

v4l2loopback only enable video piped to virtual camera

## docker

### dockerfile

uses debian

`cp /usr/bin/chromedriver /usr/local/lib/python3.9/dist-packages/seleniumbase/drivers/`

Put chromium's webdriver to the seleniumbase's directory to avoid downloading the wrong version, especially when used in arm64 arch machines.

Need to update the directory when python3 has newer version.

### docker run

Enable access to kernal modules in docker

`docker run (-it) --privileged debian`

`-it` is interactive terminal, which create a terminal when you run the command, otherwise there won't be an interactive terminal. More refer to docker manual: https://docs.docker.com/engine/reference/commandline/run/

`--privileged` enables access to /dev directory which `/dev/video0` and `/dev/video64` we created will be located. More refer to docker manual: https://docs.docker.com/engine/reference/commandline/run/

## python code

`python3 google_signin.py` login and create a meeting, print the URL of the meeting to stdout.

`python3 google_signin.py 'URL_OF_MEETING'` login and join the meeting with the passed-in URL.

**google_signin.py** uses SeleniumBase undetected mode to sign in Google, create, join, and leave Google Meet. Also collecting webRTC dump.

Before running the python code, define the following in the docker container

`export GOOGLE_ACCT_USER='#Your_Google_Email#'`

`export GOOGLE_ACCT_PASS='#Your_Google_Password#'`

`export GOOGLE_ACCT_PHONE='#Your_Phone_that's_attach_to_the_account#'`

**phone is required to circumvent the verification**

