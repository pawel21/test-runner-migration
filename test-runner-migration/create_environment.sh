#!/usr/bin/env bash
if [[ `uname` == 'Linux' ]]; then
    if ! [[ -x "$(command -v pip)" ]]; then
        sudo apt-get install -y python-pip
    fi
elif [[ `uname` == 'Darwin' ]]; then
    if ! [[ -x "$(command -v pip)" ]]; then
        echo "You are using OSX. Please install pip manually to run this script correctly"
        exit 1
    fi
else
    echo "This script is only supported on Ubuntu and OSX!"
    exit 1
fi

pip install virtualenv

# TODO this should be set at the top of the script but currently we use python from CT-DEVENV
# this python doesnt have pip module
set -e
set -o pipefail

virtualenv --no-site-packages venv
source venv/bin/activate
python -m pip install -r requirements.txt
pyb -v -X
deactivate
