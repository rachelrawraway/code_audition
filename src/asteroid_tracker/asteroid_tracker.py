"""
This is the memo for Task 1 of the code audition
"""

import logging


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

    stats = calculate_statistics(start_date, end_date)

    print_statistics(stats)


def calculate_statistics(start_date, end_date):
    """
    Make an API request and calculate statistics.
    """

    # TODO: Task 2 - Prepare and make the HTTP request


    num_asteroids = 0
    num_potentially_hazardous_asteroids = 0

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
