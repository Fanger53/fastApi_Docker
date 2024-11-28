# fastApi_Docker
Linux Kernel
basic install for fastApi trought docker
create the virtual environment
python3 -m venv ./venv

activate ./venv
source ./venv/bin/activate
desactivar entorno virtual ./venv/
deactivate
#after activate virtual environment use this comands

install fastApi
pip install "fastapi[standard]"

install pip good practice
install pip install -U pip
install uvicorn
pip install "uvicorn[standart]"

run the main file app
uvicorn main:app --reload
