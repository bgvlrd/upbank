# UPBank: Bank Auto Loan Information System

This information system aims to enable potential borrowers to apply for a loan in order to acquire property (house, car) or construct/renovate a house (multi-purpose loan). 

## Contents of this Repository
* accounts - contains the login, registration of the system
* App - where most of the system works
* templates - frontend files
* UPBank - admin files

## How to run UPBank?
* Clone this repository
```
git clone https://github.com/bgvlrd/upbank.git
```

* Go to the directory where the repository is stored (in your command line)
* If your repository is stored in your Desktop, go to your Desktop
```
cd <where your put your repository>
```

* Create, install, and activate virtual environment
```
pip install virtualenv
virtualenv <name of your choice>
*Preferably name it "upbank" to put the scripts and libs folder in the upbank folder.

*Go to the upbank folder*
cd upbank

*Activate the virtual environment*
MAC: source bin/activate
Windows: .\Scripts\Activate
```

* Install necessary requirements
```
pip install -r requirements.txt
```

## Interacting with the system
* Make migrations and migrate
```
python manage.py makemigrations
python manage.py migrate
```

* Create your own superuser
```
python manage.py createsuperuser
```

* Run the server
```
python manage.py runserver
```


