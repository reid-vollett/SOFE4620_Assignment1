# SOFE4620_Assignment1
SOFE4620 Data Mining Assignment 1

This assignment uses the undocument NHL API discovered by Kevin Sidwar (https://www.kevinsidwar.com/iot/2017/7/1/the-undocumented-nhl-stats-api)

The main URL for access to the API is https://statsapi.web.nhl.com/api/v1

## Windows Setup
* Install GIT if not already installed, see [here](https://git-scm.com/download/win)
* Run CMD as admin, and clone the project
```git clone https://github.com/reid-vollett/SOFE4620_Assignment1```
* Install [Python 3.6.3](https://www.python.org/ftp/python/3.6.4/python-3.6.4.exe) 
**Note:** Older versions of Python not tested, but may work
* If required, add Python to your Windows environment variable. See this [guide](https://www.pythoncentral.io/add-python-to-path-python-is-not-recognized-as-an-internal-or-external-command/) for more information.
* Run the following commands to install, configure, and run the [Python virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
```
pip install virtualenv virtualenvwrapper
virtualenv venv
venv\Scripts\activate
pip install -r requirements.txt
```
* To stop the execution of the Python virtual environment, run ```deactivate```

## Project Running
* To run the project, open the Python virtual environment
* Within the cloned repository, run ```python main.py```
* View generated CSV files

team_data.csv contains data about NHL teams

player_data.csv contains data about all NHL players 


