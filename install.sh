#!/bin/bash

echo "먼저 https://github.com/19-1-skku-oss/2019-1-OSS-L3에 접속하여 자신의 repo에 저장소가 fork 되었는지 확인합니다"
echo -e "fork 되어있다면 자신의 GitHub ID를 입력해주세요 : \c"

read githubid

sudo apt install -y git zip unzip python2.7 python3 python3-pip
python3 -m pip install virtualenv
git clone https://github.com/${githubid}/2019-1-OSS-L3.git ChatterBot
cd ChatterBot
python3 -m virtualenv ChatterBotEnv
./ChatterBotEnv/bin/pip3  install -r requirements.txt
./ChatterBotEnv/bin/pip3  install -r dev-requirements.txt
./ChatterBotEnv/bin/python3 -m spacy download en
clear
echo "ChatterBot 폴더 내에서 'source ChatterBotEnv/bin/activate'를 실행하고 'python3 test.py' 를 실행하여 정상적으로 설치되었는지 확인하십시오."
