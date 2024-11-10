import unittest
from addition import addition
class test_add(unittest.TestCase):
  def testadd(self):
    result = addition.add(1,1)
    self.assertequal(result,2)
if __name__ == "__main__":
  unittest.main()
