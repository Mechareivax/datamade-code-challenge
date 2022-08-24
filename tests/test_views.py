import pytest
import os
# import views file


def test_api_parse_succeeds(client):
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

    result = views.AddressParse.parse(address_string)

    assert result == desired_output, "incorrect output"


def test_api_parse_raises_error(client):
    # TODO: Finish this test. The address_string below will raise a
    # RepeatedLabelError, so ParseAddress.parse() will not be able to parse it.
    address_string = '123 main st chicago il 123 main st'
    desired_output = (
        "123 main st chicago il 123 main st",
        "Unable to parse this value due to repeated labels."
        )

    result = views.AddressParse.parse(address_string)

    assert result == desired_output, "incorrect output"
