import unittest
from DemoExample1 import Sample1

# I created 1 class with 2 methods inside that and I created a unit teest in which i called those 2 methods
# let us try to create a new unit test directly in which define logic and see whether you can execute it or not

class MyTestCase(unittest.TestCase):
    def test_addingNumbers(self):
        Sample1.add(self,3,5)

    def test_subNumber(self):
        Sample1.sub(self,5,2)


# if __name__ == '__main__':
#     unittest.main()
