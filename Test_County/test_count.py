import unittest
from PythonApplication1 import country_s

class Test_c_s(unittest.TestCase):

    def test_c_s(self):
        p = country_s('Russian', 'Moscow')
        self.assertEqual(p,'Moscow-Russian' )

if __name__ == '__main__':
    unittest.main()
