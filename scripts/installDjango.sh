#!/bin/bash
#Script to install Django

#Install the EPEL Repository
#(contains extra packages not maintained as part of the core distrbution)
sudo yum install epel-release

#Install pip from EPEL repositories
echo "Installing pip..."
sudo yum install python-pip
echo "pip installed"

#Install Django globally (using pip)
echo "Installing Django"
sudo pip install Django
echo "Django installed"

#To verify that installation was successful
echo "Version of Django installed:"
django-admin --version
