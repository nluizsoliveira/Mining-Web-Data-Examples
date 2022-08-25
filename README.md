# Mining Web Data
Each folder has a `README.md` file with instructions for mining a specific case. 

For simplyfing things, an unique file containing all projects libraries is available at `requirements.txt`. 

Before running a script, create a `virtual environment`, enter it and install requirements: 

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

This is only necessary once.


Then, enter the individual folder and read further instructions on `README.md`. For example, project 0 can be run with: 

```bash
cd 0_schedule_database_download/
python script.py
```

However it also uses **crontab** to schedule the script periodically. Read its `README` to further instructions on how to set it. 