# get base image debian
FROM debian

RUN apt-get update

RUN apt-get install -y git python3 python3-pip chromium chromium-driver v4l2loopback-dkms ffmpeg


RUN pip3 install selenium
RUN pip3 install seleniumbase

# RUN pip3 install pyvirtualdisplay

# RUN apt-get install -y vim

RUN cp /usr/bin/chromedriver /usr/local/lib/python3.9/dist-packages/seleniumbase/drivers/
