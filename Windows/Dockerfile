# The Debian 7 builder
FROM mcr.microsoft.com/windows:1903
FROM python
# get the important packages
#RUN apt-get update && apt-get upgrade -y && apt-get install python3-pip -y
#RUN apt-get -y install git wget tar make
#RUN apt-get -y install gcc g++ make libxml2-dev libboost-dev libboost-test-dev libboost-system-dev libpcre3-dev re2c
#RUN apt-get -y install libxext-dev libreadline-dev libx11-dev dos2unix
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install distro
# copy the script
COPY ./run_build.py ./
# run the script
CMD ["python3","run_build.py"]
