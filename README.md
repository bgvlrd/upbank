# upbank

## UPBank: Bank Auto Loan Information System: 

This information system aims to enable potential borrowers to apply for a loan in order to acquire property (house, car) or construct/renovate a house (multi-purpose loan). 

## How to run UPBank?
* Clone this repository
```
git clone https://github.com/bgvlrd/upbank.git
```

* Go to the project directory (in your command line)
```
cd UPBank
```

* Activate virtual environment
```
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
python manage.py migate
```

* Create your own superuser
```
python manage.py createsuperuser
```

* Run the server
```
python manage.py runserver
```
