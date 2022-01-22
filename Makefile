
make setup-windows:
	virtualenv venv -p python3.8
	. venv/Scripts/activate
	pip install pip-tools
	pip-compile requirements.in
	pip install -r requirements.txt
