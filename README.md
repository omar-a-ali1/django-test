# project rapid pour appliques les base de framework **Django**
## requirement : 
- python 
- docker
- numpy
- pandas
- sklearn
- django
- djangorestframework
## telechargement de dependence
```python
    pip install -r requirement.txt
```
## demerage de base de donnees (postgres)
```bash
    docker compose -f compose up
```
## demarage de project 
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
## resume 
ce projet Django contient 2 applications 
/api qui contient un modèle de machine learning déployé  
/crud qui contient peration *CRUD* sur un tableau (prudents)