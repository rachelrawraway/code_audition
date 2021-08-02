"""
Tests for the asteroid_tracker script.
"""

import json
import math

import pytest
import responses

from asteroid_tracker import API_URL, calculate_statistics

from tests import fixtures


@responses.activate
def test_2021_01_01_to_2021_01_02_success_200():
    """
    Test a successful run with fixture data for 2021-01-01 to 2021-01-02.
    """

    # Define expected values

    start_date = '2021-01-01'
    end_date = '2021-01-02'

    num_asteroids = 31
    num_potentially_hazardous_asteroids = 3

    largest_diameter_meters = 469.399494
    nearest_miss_kms = 237201.814200094

    # Setup response mock

    url = API_URL % (start_date, end_date)

    responses.add(
        responses.GET,
        url,
        body=json.dumps(fixtures.API_RESPONSE_2021_01_01_TO_2021_01_02_SUCCESS),
        status=200,
        content_type='application/json',
    )

    # Calculate statistics

    stats = calculate_statistics(start_date, end_date)

    assert stats['start_date'] == start_date
    assert stats['end_date'] == end_date

    assert stats['num_asteroids'] == num_asteroids
    assert stats['num_potentially_hazardous_asteroids'] == num_potentially_hazardous_asteroids

    assert math.isclose(stats['largest_diameter_meters'], largest_diameter_meters, abs_tol=0.00001)
    assert math.isclose(stats['nearest_miss_kms'], nearest_miss_kms, abs_tol=0.00001)



@responses.activate
def test_invalid_date_fail_400():
    """
    Test a failed run that uses an invalid date.
    """

    # Define expected values

    start_date = 'bananas'
    end_date = '2016-05-11'

    # Setup response mock

    url = API_URL % (start_date, end_date)

    responses.add(
        responses.GET,
        url,
        body=json.dumps(fixtures.API_RESPONSE_400_ERROR),
        status=400,
        content_type='application/json',
    )

    # Calculate statistics

    stats = calculate_statistics(start_date, end_date)

    assert 'error' in stats
    assert stats['error']['code'] == 400
    assert stats['error']['type'] == 'BAD_REQUEST'
    assert stats['error']['message'] == 'Date Format Exception - Expected format (yyyy-mm-dd) - The Feed date limit is only 7 Days'
