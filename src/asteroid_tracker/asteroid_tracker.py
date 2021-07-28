"""
This is the memo for Task 1 of the code audition
"""

import logging
import datetime
import json

import requests

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


API_URL = 'https://api.nasa.gov/neo/rest/v1/feed?start_date=%s&end_date=%s&api_key=DEMO_KEY'


def main():
    """
    Main function which takes input arguments and calls relevant functions.
    """

    start_date = None
    end_date = None

    # TODO: Task 1 - Gather user input
    start_date, end_date = input(" ").split()

    # start_date
    # year, month, day = map(int, start_date.split('-'))
    # start_date = datetime.date(year, month, day)
    start_date = start_date.strip()

    # end_date
    # year, month, day = map(int, end_date.split('-'))
    # end_date = datetime.date(year, month, day)
    end_date = end_date.strip()

    stats = calculate_statistics(start_date, end_date)
    # print_statistics(stats)


def calculate_statistics(start_date, end_date):
    """
    Make an API request and calculate statistics.
    """
    print(start_date)
    print(end_date)
    # TODO: Task 2 - Prepare and make the HTTP request
    url = API_URL % (start_date, end_date)
    response = requests.get(url)
    print (response.url)
    # print(response.content)

    json_data = json.loads(response.text)
    # print(json.dumps(json_data, indent = 4))

    # num_asteroids
    keyVal = 'element_count'
    if keyVal in json_data:
        num_asteroids = json_data[keyVal]

    # num_potentially_hazardous_asteroids
    num_potentially_hazardous_asteroids = 0
    count = 0
    name = "true"

    for nearEarthObject in json_data['near_earth_objects']:
        for item in nearEarthObject:
            if item['is_potentially_hazardous_asteroid'] == True:
                count = count + 1
    print(count)


    # min_diameter_meters
    keyVal = 'estimated_diameter'
    dimension = 'meters'
    max = 0
    max_diam = 0
    min_diam = 0
    # print (json_data['near_earth_objects']['2021-01-02'][0][keyVal]['meters']['estimated_diameter_max'])
    # for i in json_data:
    #     if json_data['near_earth_objects'][end_date][i][keyVal]['meters']['estimated_diameter_max'] > max:
    #         max = json_data['near_earth_objects'][end_date][i][keyVal]['meters']['estimated_diameter_max']
    #         max_diam = json_data['near_earth_objects'][end_date][i][keyVal]['meters']['estimated_diameter_max']
    #         min_diam = json_data['near_earth_objects'][end_date][i][keyVal]['meters']['estimated_diameter_min']

    # print (json_data['near_earth_objects'][end_date][0][keyVal]['meters']['estimated_diameter_max'])







    #if response.status_code == 400:
    #     stats = 'error'
    # print_statistics('error') - possible error ^ return statement needed?



    # num_asteroids = 0
    # num_potentially_hazardous_asteroids = 0

    largest_diameter_meters = -1
    nearest_miss_kms = -1

    # TODO: Task 3 - Calculate statistics

    return {
        'start_date': start_date,
        'end_date': end_date,
        'num_asteroids': num_asteroids,
        'num_potentially_hazardous_asteroids': num_potentially_hazardous_asteroids,
        'largest_diameter_meters': largest_diameter_meters,
        'nearest_miss_kms': nearest_miss_kms,
    }


def print_statistics(stats):
    """
    Print the calculated statistics.
    """

    logger.info('')

    if 'error' in stats:
        logger.error('HTTP Error:')
        logger.error('Code: %s', stats['error']['code'])
        logger.error('Type: %s', stats['error']['type'])
        logger.error('Message: %s', stats['error']['message'])

    else:
        logger.info('Displaying asteroid data for period %s - %s' % (stats['start_date'], stats['end_date']))
        logger.info('---------------------------------------------------------------------')
        logger.info('Number of asteroids: %d' % stats['num_asteroids'])
        logger.info('Number of potentially hazardous asteroids: %d' % stats['num_potentially_hazardous_asteroids'])
        logger.info('Largest estimated diameter: %f m' % stats['largest_diameter_meters'])
        logger.info('Nearest miss: %f km' % stats['nearest_miss_kms'])

    logger.info('')


if __name__ == '__main__':
    main()
