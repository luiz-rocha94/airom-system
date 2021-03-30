# airom-system
Python 3.7 application with Django webframework and MariaDB DataBase

## Install python libs 
pip install -r requirements.txt

## Install and configure MariaDB
user: root\
password: pass\
INSTALL SONAME 'ha_connect';

## Create tables in django models or import from database.
python manage.py inspectdb > models.py

##Configure MindsDB
see mindsdb/config.json\
python -m mindsdb --api=http,mysql --config=config.json\

No module mindsdb_worker
No module python-Levenshtein

http.client.ResponseNotReady: Idle

Warning: Found `num_iterations` in params. Will use it instead of argument
  _log_warning("Found `{}` in params. Will use it instead of argument".format(alia
s))
