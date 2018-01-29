# SOFE4620_Assignment1
SOFE4620 Data Mining Assignment 1

This assignment uses the undocument NHL API discovered by Kevin Sidwar (https://www.kevinsidwar.com/iot/2017/7/1/the-undocumented-nhl-stats-api)

The main URL for access to the API is https://statsapi.web.nhl.com/api/v1 and requires endpoints for data retrieval

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

team_data.csv contains data about teams in the NHL division, this includes:
* Team Name
* Venue Information
* Division/Conference/Franchise Information
* and more

player_data.csv contains data about all players in the NHL, this includes:
* Player Name
* Birth/Height/Weight Information
* Current Team/Position/Player Play Status
* Yearly Play Statistics (includes full hockey career)
* and more

**Important Note - CSV Files**

Some data is kept as a dictionary for a few key reasons, first of which the API is not always consistent as some players may be missing statistics or have unique stats for one season (ie. https://goo.gl/nUj9Ja) and not another. The second reason to keep some data in the dictionary format is that it allows easier manipulation if/when this data is used for data processing in general use cases or in machine learning. Program readability was preffered over human readability.

The following data is kept in dictionary format:

team_data.csv
* venue
* division
* conference
* franchise

player_data.csv
* currentTeam
* primaryPosition
* stats
