import datetime
import requests

data_url = ('https://docs.google.com/spreadsheets/d/e/2PACX-1vQ9oKYNQhJ6v85dQ9qsybfMfc-eaJ9oKVDZKx-VGUr6szNoTbvsLTzpEaJ3oW_LZTklZbz70hDBUt-d/pub?gid=0&single=true&output=csv')

response = requests.get(data_url)
csv_content = response.text

with open ('./databases/updated.csv', 'w+', encoding='utf-8') as csv_file: 
    csv_file.write(csv_content)


date = datetime.datetime.now()
backup_path = f'./databases/backups/{date}.csv'

with open (backup_path, 'w+', encoding='utf-8') as backup_file:
    backup_file.write(csv_content)