import unittest
from addition import Add  
class TestAdd(unittest.TestCase):
    def test_add(self):
        add_instance = Add()  
        result = add_instance.add(1, 1)
        self.assertEqual(result, 2)  
if __name__ == "__main__":
    unittest.main()
