#!/bin/bash
# This bash script will be run with when the docker image generated from the
# Dockerfile in this directory is run
export http_proxy=INSERT PROXY HERE
export https_proxy=$http_proxy
git config --global http.proxy INSERT PROXY HERE
git clone --single-branch --branch=feature-integrated-packager https://github.com/jwlodek/installSynApps
cd installSynApps
python3 installCLI.py -y -c addtlConfDirs/minConfigureLinux