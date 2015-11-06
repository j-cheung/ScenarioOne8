#!/bin/bash

sudo systemctl stop httpd

#https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-apache-and-mod_wsgi-on-centos-7
#Install mod_wsgi
sudo yum install python-setuptools http mod_wsgi

#Install virtualenv
sudo pip install virtualenv

#Clone from github repository
cd
cd Desktop
git clone https://github.com/stupidjc/ScenarioOne8
cd ScenarioOne8
git checkout -b production remotes/origin/production

#Configure the virtual environment
cd
cd Desktop/ScenarioOne8/toDoList

#Create virtual environment:
virtualenv myprojectenv
#Activate virtual environment
source myprojectenv/bin/activate
#Install Django in virtual environment
pip install django


echo '
STATIC_ROOT = os.path.join(BASE_DIR, "static/")' >> ~/Desktop/ScenarioOne8/toDoList/toDoList/settings.py
cd
cd ~/Desktop/ScenarioOne8/toDoList
./manage.py collectstatic


sudo cp -R ~/Desktop/ScenarioOne8 /var/www/html

#Leave virtual environment
deactivate

#Configure Apache
cd /etc/httpd/conf.d
sudo rm django.conf
sudo touch django.conf

#Adding to django.conf

echo '
Alias /static /home/localuser/Desktop/ScenarioOne8/toDoList/static
<Directory /home/localuser/Desktop/ScenarioOne8/toDoList/static>
    Require all granted
</Directory>

<Directory /home/localuser/Desktop/ScenarioOne8/toDoList/toDoList>
    <Files wsgi.py>
        Require all granted
    </Files>
</Directory>

WSGIDaemonProcess toDoList python-path=/home/localuser/Desktop/ScenarioOne8/toDoList:/home/localuser/Desktop/ScenarioOne8/toDoList/myprojectenv/lib/python2.7/site-packages
WSGIProcessGroup toDoList
WSGIScriptAlias / /home/localuser/Desktop/ScenarioOne8/toDoList/toDoList/wsgi.py' | sudo tee --append /etc/httpd/conf.d/django.conf
echo '
LoadModule wsgi_module modules/mod_wsgi.so' | sudo tee --append /etc/httpd/conf.d/django.conf

cd ..
cd conf
echo '
LoadModule wsgi_module modules/mod_wsgi.so' | sudo tee --append httpd.conf


#Permission Issues
cd
sudo usermod -a -G localuser apache
chmod 710 /home/localuser
chmod 664 ~/Desktop/ScenarioOne8/toDoList/db.sqlite3
sudo chown :apache ~/Desktop/ScenarioOne8/toDoList/db.sqlite3
sudo chown :apache ~/Desktop/ScenarioOne8/toDoList

#Start server
sudo systemctl start httpd
