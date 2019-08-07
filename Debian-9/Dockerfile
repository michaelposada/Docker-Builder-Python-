# The Debian 9 builder
FROM debian:9
ENV http_proxy INSERT PROXY HERE
# get the important packages
RUN apt-get update && apt-get upgrade -y && apt-get install python3-pip -y
RUN python3 -m pip --proxy INSERT PROXY HERE install --upgrade pip
RUN apt-get -y install git wget tar make
RUN apt-get -y install gcc g++ make libxml2-dev libboost-dev libboost-test-dev libboost-system-dev libpcre3-dev re2c
RUN apt-get -y install libxext-dev libreadline-dev libx11-dev dos2unix
RUN python3 -m pip --proxy INSERT PROXY HERE install distro
# copy the script
COPY ./run_build.sh ./
RUN dos2unix ./run_build.sh
# run the script
CMD ["bash", "run_build.sh"]