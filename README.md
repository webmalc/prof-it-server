# prof-it-server
prof-it django rest backend

## users
 two-factor setup url: account/two_factor/setup/

## installation
1. install requirements: postgresql, redis, python3, npm, pip
2. create and activate virtualenv for project
3. copy profit/settings_local.py.dist to profit/settings_local.py and change it
4. run: pip install -r requirements.txt   (python libs)
5. run: npm install   (js libs)
6. run: ./manage.py makemigrations    (migrate DB)
6. run: ./manage.py migrate    (migrate DB)
7. run: ./manage.py createsuperuser   (new user for admin backend)
8. !!! optional !!! run: ./manage.py loaddata tests/technologies tests/pages tests/works    (load test db fixtures)
9. run: pytest --pep8 --flakes (run tests to determine if everything is alright )
10. run: ./manage.py runserver_plus   (run dev server)
11. open url: http://localhost:8000 (Well done! =))
