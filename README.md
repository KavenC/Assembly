## Requirement ##
Python 3.4.3
pip

## Installation ##
1. Create virtualenv
```bash
./Assembly$ python3 -m venv env
```
2. activate env
```bash
./Assembly$ source env/bin/activate
```
3. install packages
```bash
(env)./Assembly$ pip install -r requirement.txt
```
4. Run webserver
```bash
(env)./Assembly$ cd assembly
(env)./Assembly/assembly$ ./manage.py runserver
```
5. Browser goto http://localhost:8080/admin/ for admin panel.
