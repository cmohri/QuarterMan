# QuarterMan

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
```virtualenv name_of_environment```

3. Activate your virtual environment. 

- If you're on Linux/MacOS:
``` . ~/name_of_environment/bin/activate```
- If you're on Windows: 
``` source /name_of_environment/bin/activate```

4. Install the project's dependencies.

```pip install -r /doc/requirements.txt```

5. Run the app!

```make run```

6. Navigate to [this link](http://127.0.0.1:500/). 

7. Enjoy!

## On a server

1. Once you are inside your droplet, navigate to the correct directory. 

```mv /var/www/```

2. Clone our repository. 

```git clone https://github.com/narang-amit/QuarterMan.git```

3. Navigate to the correct directory.

```mv QuarterMan/elbarto```

4. Install the capability to create a virtual environment and then create a virtual environment. Replace name_of_environment with the desired name of your virtual environment.

- If you're using Python3 or higher:
```python3 -m venv name_of_environment```
- If you're using Python2: 
```pip install virtualenv```
```virtualenv name_of_environment```

6. Activate your virtual environment. 

``` . ~/name_of_environment/bin/activate```

7. Navigate to the correct directory. 

```mv ../```

7. Install the project's dependencies.

```pip install -r /doc/requirements.txt```

3. Copy the name of the server you wish to put our project on. One way you could do so is by running the following command, which will return the server name.

```curl http://icanhazip.com```

4. Insert the server name and the email address you wish people to contact you on in the elbarto.conf file. 

```ServerName name_of_server```
```ServerAdmin email_to_contact```

5. Navigate to your server on your browser. You should be good to go. 

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
```pip3 install -r docrequirements.txt```


