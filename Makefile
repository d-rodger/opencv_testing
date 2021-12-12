PYTHON = python3.9
VENV_BIN = ./venv/bin

.PHONY: all

all: venv

venv:
	$(PYTHON) -m venv venv
	$(VENV_BIN)/pip install --upgrade pip
	$(VENV_BIN)/pip install --upgrade setuptools
	$(VENV_BIN)/pip install -r requirements.txt
	# cd venv/lib/python3.9/site-packages/
	# ln -s /usr/local/lib/python3.9/site-packages/cv2.cpython-39m-x86_64-linux-gnu.so ./cv2.so

