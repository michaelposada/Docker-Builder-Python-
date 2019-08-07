#!/bin/bash
# This bash script will be run with when the docker image generated from the
# Dockerfile in this directory is run
export http_proxy=http://10.0.137.23:8888
export https_proxy=$http_proxy
git config --global http.proxy http://10.0.137.23:8888
git clone --single-branch --branch=feature-integrated-packager https://github.com/jwlodek/installSynApps
cd installSynApps
python3 installCLI.py -y -c addtlConfDirs/minConfigureLinux