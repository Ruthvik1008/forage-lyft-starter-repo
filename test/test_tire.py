import unittest
from datetime import datetime

from ..tire.octoprime import OctoprimeTire

from ..tire.carrigan import Carrigan


class TestCarriganTire(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        usage = [0, 0.1, 0.2, 0.9]

        tire = Carrigan(usage)
        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        usage = [0, 0.1, 0.2, 0.3]

        tire = Carrigan(usage)
        self.assertFalse(tire.needs_service())


class TestOctoprimeTire(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        usage = [1, 1.1, 0.2, 0.8]

        tire = OctoprimeTire(usage)
        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        usage = [0, 0.1, 0.2, 0.3]

        tire = OctoprimeTire(usage)
        self.assertTrue(tire.needs_service())


if __name__ == '__main__':
    unittest.main()
