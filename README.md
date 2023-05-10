## Base DRF project with session, base token and JWT auth

### Run
Init virtual env
```bash
python -m venv venv
```
Activate venv
```bash
source venv/bin/activate
```
or for Windows
```bash
./venv/bin/activate.bat
```
Change working directory
```bash
cd drfwomensite
```
Make migrations
```bash
python manage.py migrate
```
Create superuser
```bash
python manage.py createsuperuser
```
Run Django project
```bash
python manage.py runserver
```
