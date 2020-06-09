CS1999: Buggy Race Editor
=========================

# 3-ENV: switching between Production and Development


## How I loaded Flask and venv on Windows:

1. In Command Line I went to my directory in which CS1999-buggy-race-editor folder was

2. I then created a venv in cmd by entering **py -m venv venv** which creates a venv directory in CS1999-buggy-race-editor

3. After making the venv, I then installed Flask by typing **pip install flask**

4. I then had to activate venv. I did this by typing in **venv\Scripts\activate**

5. After both venv and Flask were inside the directory, I then initialised the database by typing in **py init_db.py** which responded by the print statement in *init_db.py*

6. I then had to set the flask app to the python file. This was done by: **set FLASK_APP=app2.py**.

7. Now I had to choose which environment mode I wanted app.py to be in. I chose *development mode* by doing this: **set FLASK_ENV=development**.

8. When completed with a task (or done for the day), I used **CTRL + C** to stop flask from running.

9. Finally, I deactivated venv by typing in **deactivate**.

## Production Environment:

Production environment is set (in Windows) by using **set FLASK_ENV=production**. Production environment, from my understanding, doesn't allow the developer to see their changes from Python. What I mean by this is that when the developer makes a change in app.py, it won't be detected by Command prompt and won't be updated in the webserver.

## Development Environment:

Development environment is set by using **set FLASK_ENV=development**. This environment allows the developer to see what changes have been made, if made any, in the Command prompt and so when the user refreshes their webserver, the changes are seen in the webpages. I used this environment.