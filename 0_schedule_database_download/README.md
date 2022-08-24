# Schedule a Database Download
The most basic case of mining web data is when data is available in a structured format for donwnload. 

The most popular format for databases is **CSV**, Comma Separated Values. 

I CSV, the first line **may** contain the **headers** (or **labels**) of the data, while every subsequence line contains a data instance itself. For example: 

`hurricanes.csv`: "hurricane and tropical storm counts for 2005-2015. Each record includes 13 values: month, historical average, counts for 2005 through 2015. Eight records are stored, for months "May" through "Dec". There is also an initial header line."

```
"Month", "Average", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015"
"May",  0.1,  0,  0, 1, 1, 0, 0, 0, 2, 0,  0,  0  
"Jun",  0.5,  2,  1, 1, 0, 0, 1, 1, 2, 2,  0,  1
"Jul",  0.7,  5,  1, 1, 2, 0, 1, 3, 0, 2,  2,  1
"Aug",  2.3,  6,  3, 2, 4, 4, 4, 7, 8, 2,  2,  3
"Sep",  3.5,  6,  4, 7, 4, 2, 8, 5, 2, 5,  2,  5
"Oct",  2.0,  8,  0, 1, 3, 2, 5, 1, 5, 2,  3,  0
"Nov",  0.5,  3,  0, 0, 1, 1, 0, 1, 0, 1,  0,  1
"Dec",  0.0,  1,  0, 1, 0, 0, 0, 0, 0, 0,  0,  1
```

There may be cases where the header line is ommited, being described in a somewhere else. 

## General Idea
1.  Download a database programatically
2.  Schedule the task so the script is executed every x time (hourly, daily, weekly, etc)

## Case
Schedule a script that downloads Covid data from Victoria, the Australian State, available at 
https://www.coronavirus.vic.gov.au/victorian-coronavirus-covid-19-data

![](https://i.imgur.com/aOq0oJv.png)

![](https://i.imgur.com/922IbRz.png)

## Approach
1. Pick the link to the desired db: 
    ```
    https://docs.google.com/spreadsheets/d/e/2PACX-1vQ9oKYNQhJ6v85dQ9qsybfMfc-eaJ9oKVDZKx-VGUr6szNoTbvsLTzpEaJ3oW_LZTklZbz70hDBUt-d/pub?gid=0&single=true&output=csv
    ```
2. code script.py, that: 
    1. request content, save text in a `updated.csv` files that always contains the most recent version of the file
    2. also save requested content in the `backups/` folder, indexing it by `datetime`
3. create the shell script crontab will call, that must: 
    1. have a `#!/bin/bash` line, that identifies which shell are we using 
    2. activate the venv, passing the **complete path** to env's activate
        You can discover the complete path with `pwd`
    3. execute python script, passng the **complete path** of the script. 
    4. exit the venv
4. Set execute permissions on the shell script
    ```bash 
    chmod +x cron_script.sh
    ```
5. add the script to crontab: 
    ```bash
    crontab -e
    ```
    ```
    * * * * *  complete/path/to/script/script.sh
    ```