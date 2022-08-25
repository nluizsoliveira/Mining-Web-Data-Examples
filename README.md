# Mining Web Data
This repository holds examples on mining web data implemented by me. 

Currently, cases are: 

1. Requesting a .csv using python `requests` and scheduling it periodically using `cron` services
2. Consuming league of legends API (Expiring token example)

I'm currently working on providing examples for: 

3. Scraping a static page with `beautifulSoup`
4. Orchestrating a whole website scraping with `scrapy`
5. Consuming hidden APIs by investigating network traffic 
6. Using a proxy to bypass ip restrictions
7. Scraping dynamic webpages with Selenium

## How to run Scripts
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
