import unittest


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("class will execute only 1 before all the tests")

    @classmethod
    def tearDownClass(cls):
        print("it will execute only after all the tests")


    def test_add(self):
        print("test1")

    def test_sub(self):
        print("test2")