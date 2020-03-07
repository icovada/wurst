
# wurst
Do things with CUCM CURRI
## Modules
### num2name
Add an alerting name to any call.
Example: Add your customer's name to calls coming in from PSTN
### speedydial
Transform a number into another
Example: Assign a short code number to numbers you dial often.
## Docker
    docker-compose up

Because ain't nobody got time fo dat.
You can run the createsuperuser command invoking an interactive shell to the container
## Installation

    git clone git@github.com:icovada/wurst.git
    cd wurst
    pipenv install
    pipenv run python manage.py makemigrations
    pipenv run python manage.py migrate
    pipenv run python manage.py createsuperuser

Follow the instructions to create the super user

To run a production server it's recommended to do so using gunicorn. If you want to look around you can just run

    pipenv run python manage.py startserver
and visit http://localhost:8000/admin

## CUCM Integration
Simply add a new External Call Control Profile pointing to this URL:

    http://<your server's IP>/<modulename>/service
And configure it under whichever object you want to run it for