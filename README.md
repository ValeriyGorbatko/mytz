## Cloning project:

git clone https://github.com/ValeriyGorbatko/mytz.git

## Create virtualenv:

virtualenv -p python3 venv

## Activate venv:

source venv/bin/activate

## Install packages:

pip install -r requirements.txt

## DB migrate:

./manage.py migrate

## Add djsoc.local to hosts:

echo "127.0.0.1 djsoc.local" >> /etc/hosts

## Runserver and open in browser:

./manage.py runserver djsoc.local:8000
