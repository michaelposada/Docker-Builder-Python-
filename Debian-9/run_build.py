#python

# This python script will be run with when the docker image generated from the
# Dockerfile in this directory is run
import os

print("Going to clone InstallSynApps")
os.system("git clone --single-branch --branch=feature-integrated-packager https://github.com/jwlodek/installSynApps")
os.system("cd installSynApps")
os.system("python3 installCLI.py -y -c addtlConfDirs/minConfigureLinux")

