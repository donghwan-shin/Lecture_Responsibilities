import unittest
from client import *


class MyTestCase(unittest.TestCase):
    def test_client(self):
        self.assertTrue(client())
