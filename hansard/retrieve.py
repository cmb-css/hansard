import json
import requests
import time

from bs4 import BeautifulSoup
from pathlib import Path
from requests.exceptions import HTTPError


BASE_URL = 'https://hansard.parliament.uk'
SLEEP_TIME = 60


def retrieve(search_term, outdir, start_date, end_date, page=1):
    finished = False
    i = page
    debates = 0
    repeated = 0
    errors = 0
    while not finished:
        args = {'searchTerm': search_term,
                'startDate': start_date,
                'endDate': end_date,
                'partial': True,
                'page': i}
        args_str = '&'.join('{}={}'.format(key, args[key]) for key in args)
        url = '{}/search/Contributions?{}'.format(BASE_URL, args_str)
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'lxml')
    
            results = soup.find_all('a', class_='card card-calendar')
            if len(results) == 0:
                finished = True
    
            for result in results:
                uparts = result['href'].split('/')
                if len(uparts) > 4 and uparts[3] == 'debates':
                    debate = {'url': '{}{}'.format(BASE_URL, result['href']),
                              'house': uparts[1],
                              'date': uparts[2],
                              'code': uparts[4]}

                    filepath = '{}/{}_{}.json'.format(outdir,
                                                      debate['date'],
                                                      debate['code'])

                    if Path(filepath).exists():
                        repeated += 1
                    else:
                        txt_url = '{}/debates/GetDebateAsText/{}'.format(
                            BASE_URL, debate['code'])
            
                        try:
                            response = requests.get(txt_url)
                            response.raise_for_status()
                            text = response.content.decode('utf-8')
                            debate['text'] = text

                            with open(filepath, 'w', encoding='utf-8') as f:
                                json.dump(
                                    debate, f, ensure_ascii=False, indent=4)
                            debates += 1
                        except Exception as e:
                            print('HTTP error occurred: {}'.format(e))
                            print(debate['url'])
                            errors += 1
                else:
                    print('ERROR #1')
                    print(result['href'])
                    errors += 1

            print('page {}; debates: {}; repeated: {}; errors: {}'.format(
                i, debates, repeated, errors))
            i += 1
        except HTTPError as http_err:
            print('HTTP error occurred: {}'.format(http_err))
            print(url)
            print('Going to sleep for {} seconds...'.format(SLEEP_TIME))
            time.sleep(SLEEP_TIME)
    print('done.')
