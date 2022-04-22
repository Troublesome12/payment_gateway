#### Setup python environment and activation

- Install python 3.10 using terminal
```shell script
$ sudo apt install python3.10-minimal
$ sudo apt-get install python3-pip python3-dev libpq-dev
```
- Make python3.10 as default python version in Ubuntu [Optional]
```shell script
$ sudo nano ~/.bashrc
# in bashrc file write below line at the end of code
alias python=python3.10
# save the file using Ctrl+x and restart bashrc file
$ source ~/.bashrc
```
- Create virtual environment and activate venv in project
```shell script
$ python -m venv venv
$ source venv/bin/activate
```

#### Install project dependencies and configure .env file
- Install libraries using requirements.txt
```shell script
$ pip install -r requirements.txt
```
- Copy **.env.example** and Create **.env** file and update all data
```shell script
$ cp .env.example .env
# must update .env file
```

#### Setup django admin panel
```shell script
$ python manage.py migrate
$ python manage.py createsuperuser
````
- Run Django Server
```shell script
$ python manage.py runserver
# python manage.py runserver 0.0.0.0:8006
```

#### Run Test Files
```shell script
$ python manage.py test account
$ python manage.py test payment
````
