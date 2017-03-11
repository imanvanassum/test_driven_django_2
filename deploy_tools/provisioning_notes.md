Provisioning a new site
=======================

## Required packages:

* nginx
* Python 3
* Git
* pip
* virtualenv
* virtualenvwrapper
* Postgres 

e.g.,, on Ubuntu:

	sudo apt-get install nginx git python3 postgres

And with PyPi:

	sudo pip3 install virtualenv virtualenvwrapper

## Nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with e.g., staging.my-domain.com

## Systemd service

* see gunicorn-systemd.template.service
* replace SITENAME with e.g., staging.my-domain.com

## Folder structure
Assume we have a user account at /home/username

/home/username
|__ .virtualenv
	|__ env folder for SITENAME
|__ sites
	|__ SITENAME
		|__ source
		|__ static
