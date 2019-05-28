#!/bin/sh

echo "Hello!"

sudo apt install zip unzip python3 python3-virtualenv
mkdir ChatterBot
cd ChatterBot
python3 -m virtualenv ChatterBotEnv
wget https://github.com/19-1-skku-oss/2019-1-OSS-L3/archive/master.zip
unzip master.zip
mv 2019-1-OSS-L3-master/* .
rmdir 2019-1-OSS-L3-master
rm master.zip
./ChatterBotEnv/bin/pip3  install -r requirements.txt
./ChatterBotEnv/bin/pip3  install -r dev-requirements.txt
./ChatterBotEnv/bin/python3 -m spacy download en
mkdir extras
mv ORIREADME.md dev-requirements.txt runtests.py tests LICENSE README.md docs graphics setup.cfg tests_django MANIFEST.in examples requirements.txt setup.py tox.ini extras
clear
echo "ChatterBot 폴더 내에서 'source ChatterBotEnv/bin/activate'를 실행하고 'python3 test.py' 를 실행하여 정상적으로 설치되었는지 확인하십시오."
