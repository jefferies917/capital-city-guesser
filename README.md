# Capital City Guesser
Django API project to test your capital city knowledge

## Installation

First install [Python 3.11.1](https://www.python.org/downloads/release/python-3111/) and clone the repo

Then pipenv:

    pip install pipenv

Navigate to the projects base directory and install required packages:

    pipenv install

Apply Migrations:

    pipenv run python manage.py migrate

Now you should be ready to run the quiz!

## Run Quiz

Start Development Server:

    pipenv run python manage.py runserver

Now go to 127.0.0.1:8000 in any browser or use [this link](https://127.0.0.1:8000) 

## Testing

In the base directory run:

    pytest guessing/tests.py