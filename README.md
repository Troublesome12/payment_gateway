```
#### Setup python environment and activation
- Install python 3.7 using terminal
```shell script
$ sudo apt install python3.7-minimal
$ sudo apt-get install python3-pip python3-dev libpq-dev
```
- Make python3.7 as default python version in Ubuntu
```shell script
$ sudo nano ~/.bashrc
# in bashrc file write below line at the end of code
alias python=python3.7
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
$ pip install -r requirements_upay.txt
```
- Create *.env* file and copy *.env.example* and update all data

#### Setup django admin panel
- Run All scripts with quickstart including migration
```shell script
python manage.py runscript quick_start
````

#### Create superuser
```shell
$ python manage.py createsuperuser
```
- Run Django Server
```shell script
$ python manage.py runserver 0.0.0.0:6000
```