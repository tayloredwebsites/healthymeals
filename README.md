# HealthyMeals

A Django-Powered Diet Support Website to help make and eat healthier meals to meet your dietary goals

[![CircleCI](https://dl.circleci.com/status-badge/img/circleci/BZR3uzdbU6P9JdMbhCLMmZ/PhQcorR5decQrvhgn17chH/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/circleci/BZR3uzdbU6P9JdMbhCLMmZ/PhQcorR5decQrvhgn17chH/tree/main)
[![Coverage Status](https://tayloredwebsites.github.io/healthymeals/docs/coverage/coverage_badge.svg)](https://tayloredwebsites.github.io/healthymeals/docs/coverage/html/index.html)
[![Test Status](https://tayloredwebsites.github.io/healthymeals/docs/tests/tests_badge.svg)](https://tayloredwebsites.github.io/healthymeals/docs/tests/index.html)
[![Flake8 Status](https://tayloredwebsites.github.io/healthymeals/docs/flake8/flake8_badge.svg)](https://tayloredwebsites.github.io/healthymeals/docs/flake8/html/index.html)

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)


License: AGPLv3


## Getting Started Developing

This app is being developed as a docker container from the get go.  This should help minimize scaling issues if this is successful.  See the following instructions for getting going.  Please feel free to contact me about doing pull requests, especially for improving documentation.

### install docker desktop

- [Docker Desktop main page](https://www.docker.com/products/docker-desktop/)
- [Docker Desktop - Macs with Apple Silicon](https://docs.docker.com/desktop/setup/install/mac-install/)
- [Docker Desktop - Macs with Intel Chips](https://desktop.docker.com/mac/main/amd64/Docker.dmg)
- [Docker Desktop - Linux](https://docs.docker.com/desktop/setup/install/linux/)
- [Docker Desktop - Windows](https://docs.docker.com/desktop/setup/install/windows-install/)

### Clone software repository from Github

see: [https://github.com/tayloredwebsites/healthymeals](https://github.com/tayloredwebsites/healthymeals)

    git clone git@github.com:tayloredwebsites/healthymeals.git

### build the docker container

    docker compose -f docker-compose.local.yml build
    python -m pip install pre-commit

### bring up the website on localhost:8000/

    docker compose -f docker-compose.local.yml up

### Run the code quality suite

Running nox will validate the code with the following tools:

- pytest: to run automated tests
- coverage: to report on code coverage of automated tests
- genbadge: to generate test and coverage badges to view on README.md on github
- ruff: to validate to coding standards
- mypy: for type checking


      docker compose -f docker-compose.local.yml run --rm django nox

## To Do: Additional Setup Instructions

### Database configurations, backups, and restores

#### To create a **normal user account**

Just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

#### To create a **superuser account**, use this command:

      $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.


### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](https://cookiecutter-django.readthedocs.io/en/latest/2-local-development/developing-locally.html#using-webpack-or-gulp).

### Deployment

The following details how to deploy this application.

#### Docker

See detailed [cookiecutter-django Docker documentation](https://cookiecutter-django.readthedocs.io/en/latest/3-deployment/deployment-with-docker.html).

### Settings

Moved to [settings](https://cookiecutter-django.readthedocs.io/en/latest/1-getting-started/settings.html).
