import requests
import graphyte
import logging
import time

logging.getLogger().setLevel(logging.INFO)

GRAPHITE_HOST = 'graphite'
PARAMS = ['temp', 'pressure', 'humidity']
SENDER = graphyte.Sender(GRAPHITE_HOST, prefix='parameters')
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'
CITY_ID = '5202009' #Moscow id
API_KEY = '##### Type your api key here #####'
def main():
    for param in PARAMS:
        response = requests.get(BASE_URL + f'?id={CITY_ID}&appid={API_KEY}')
        response = response.json()
        logging.info('Response output: %s', response)
        value = response['main'][param]
        logging.info('Value output: %s', value)
        SENDER.send(param, float(value))


if __name__ == '__main__':
    while True:
        try:
            main()
        except:
            logging.exception("Unhandled exception")
        time.sleep(5)