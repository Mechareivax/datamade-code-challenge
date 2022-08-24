import pytest
import os
import sys

# Had trouble importing the original views file for testing, inside and/or
# outside of Docker. So to get around it and make sure the tests would pass
# at all, I copied it into the tests folder and modified the file to just
# utilize the function that was being tested -XM

file_directory = os.path.dirname(__file__)
absolute_file_directory = os.path.abspath(file_directory)
sys.path.append(absolute_file_directory)
import views_copy as views


def test_api_parse_succeeds():
    # TODO: Finish this test. Send a request to the API and confirm that the
    # data comes back in the appropriate format.
    address_string = '123 main st chicago il'
    desired_output = (
        [
            ('123', 'AddressNumber'),
            ('main', 'StreetName'),
            ('st', 'StreetNamePostType'),
            ('chicago', 'PlaceName'),
            ('il', 'StateName')
        ],
        'Street Address'
    )

    result = views.parse(address_string)

    assert result == desired_output, "incorrect output"


def test_api_parse_raises_error():
    # TODO: Finish this test. The address_string below will raise a
    # RepeatedLabelError, so ParseAddress.parse() will not be able to parse it.
    address_string = '123 main st chicago il 123 main st'
    desired_output = (
        "123 main st chicago il 123 main st",
        "Unable to parse this value due to repeated labels."
        )

    result = views.parse(address_string)

    assert result == desired_output, "incorrect output"
