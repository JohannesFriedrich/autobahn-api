"""
    Autobahn App API

    Was passiert auf Deutschlands Bundesstraßen? API für aktuelle Verwaltungsdaten zu Baustellen, Staus und Ladestationen. Außerdem Zugang zu Verkehrsüberwachungskameras und vielen weiteren Datensätzen.   # noqa: E501

    The version of the OpenAPI document: 1.0.1
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland import autobahn
from deutschland.autobahn.model.parking_lorry import ParkingLorry
globals()['ParkingLorry'] = ParkingLorry
from deutschland.autobahn.model.parking_lorries import ParkingLorries


class TestParkingLorries(unittest.TestCase):
    """ParkingLorries unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testParkingLorries(self):
        """Test ParkingLorries"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ParkingLorries()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
