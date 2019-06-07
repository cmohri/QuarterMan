# [QuarterMan](www.quartermman.com)

# Roster
## Amit Narang (PMAN), Jared Asch, Damian Wasilewicz, & Clara Mohri

# Watch our demo video here! (Currently not available)

# Overview

For our final project, our group decided to try to create a version of the Bert Bell Schedule fit for the modern era. We will add new features like customizable templates for different potential schedules, patch bugs in the Bert Bell Schedule, and most importantly we will keep the simplicity and usefulness that has ingrained it into our Stuyvesant society.

# How to run this project

## Locally

1. Clone our repository and navigate to the directory. 

```git clone https://github.com/narang-amit/QuarterMan.git```
```mv QuarterMan/```

2. Install the capability to create a virtual environment and then create a virtual environment. Replace name_of_environment with the desired name of your virtual environment.

- If you're using Python3 or higher:
```python3 -m venv name_of_environment```
- If you're using Python2: 
```pip install virtualenv```
```virtualenv venv```

3. Activate your virtual environment. 

- If you're on Linux/MacOS:
``` . ~/venv/bin/activate```
- If you're on Windows: 
``` source /venv/bin/activate```

4. Install the project's dependencies.

```pip3 install -r /docs/requirements.txt```

5. Run the app!

```make run```

6. Navigate to [this link](http://127.0.0.1:500/). 

7. Enjoy!

## On a server (NOTE: IMPOSSIBLE)

### You cannot host this on a server, as Google OAuth doesn't work on IP addresses. Because of that, we bought a domain and hosted it to show that it was possible. You can find proof at [www.quartermman.com](www.quartermman.com).

#### We had written up these instructions before, so I am including them below as a reference. Once again, these instructions will not function properly.



1. Once you are inside your properly-configured droplet (you can seek some learnination from [here](https://docs.google.com/document/d/12b4gf9_1EiJDt6ValtoDVsZPLhGhyOdmnW4n2Xg5E-A/edit?ts=5cdd8691) and [here](https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-ubuntu-18-04)), navigate to the correct directory. 

```cd /var/www/```

2. Clone our repository. 

```git clone https://github.com/narang-amit/QuarterMan.git elbarto```

3. Navigate to the correct directory.

```cd elbarto/elbarto```

4. Install the capability to create a virtual environment and then create a virtual environment. Replace name_of_environment with the desired name of your virtual environment.

- If you're using Python3 or higher:
```python3 -m venv venv```
- If you're using Python2: 
```pip install virtualenv```
```virtualenv name_of_environment```

6. Activate your virtual environment. 

``` . ~/venv/bin/activate```

7. Navigate to the correct directory. 

```cd ../```

7. Install the project's dependencies.

```pip install -r /docs/requirements.txt```

8. Enable site in apache.

```sudo a2ensite elbarto```
```sudo a2enmod wsgi```

9. Copy the name of the server you wish to put our project on. One way you could do so is by running the following command, which will return the server name.

```curl http://icanhazip.com```

10. Insert the server name in the elbarto.conf file. 

```ServerName name_of_server```

11. Change the permissions of your stuff.

```chgrp -R www-data elbarto```
```chmod -R g+w elbarto```

12. Move the elbarto.conf file to the appropriate directory.

```mv elbarto.conf /etc/apache2/sites-available/```

13. Change the system variables.

```sudo -H nano /etc/environment```

14. In that document, insert the following line.

```FLASK_APP=elbarto/run.py```

15. Go to [this link](https://developers.google.com/adwords/api/docs/guides/authentication#webapp) and follow the instructions to set up your Google OAuth credentials, using your server name when appropriate. 

16. Run the following command in your terminal.

```make```

17.  Restart your Apache server.

```sudo service apache2 restart```

18. Navigate to your server on your browser. You should be good to go. 

# API

We did not use any API's, so there is no need to install anything.

# Necessary Packages

* **Authlib / loginpass **
- We used *Authlib* as our secure means of implementing OAuth2 protocol. *loginpass* is a simplel wrapper around Authlib that eases its integration into our Flask app.

* **Flask-SQLAlchemy / SQLAlchemy**
- *SQLAlchemy* is an Object Relational Mapper that considers the database as a relational algebra engine, not just a collection of tables, which makes it useful now that more abstraction starts to matter. *Flask-SQLAlchemy* is a Flask extension that addds support for SQLAlchemy in our app. 

* **Flask-WTF / WTForms**
- *WTForms* is a form validation library that we used to build our schedule templating form. We used *Flask-WTF* to ease our tying-in of *WTForms* into our Flask app.

* These are all included in our requirements.txt file, and can be installed with
```pip3 install -r doc/requirements.txt```


