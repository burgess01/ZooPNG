FROM ubuntu:18.04
RUN yes | apt-get update && \
yes | apt install build-essential && \
yes | apt-get install python3.8 && \
yes | apt-get install python3-pip && \
pip3 install sly 
WORKDIR /root
