export FLASK_APP=service.py
export PYTHONPATH=$PWD/../../..:PYTHONPATH
echo $PYTHONPATH
flask run --host=0.0.0.0 --port=55001
