import unittest
def get_price(riceKg, distance):
    
    if riceKg <= 0 or riceKg >= 1000 or distance <= 0 or distance >= 50:
        return -1

    price = 0.0
    if riceKg > 0 and riceKg < 50:
        price = 18000 * riceKg
    elif riceKg >= 50 and riceKg < 100:
        price = 17000 * riceKg
    elif riceKg >= 100 and riceKg < 1000:
        price = 16000 * riceKg
    
    if distance < 10:
        price = price / 1.25
    
    return price

class TestMethods(unittest.TestCase):
    def test1(self):
        self.assertEqual(get_price(500, 0), -1)

    def test2(self):
        self.assertEqual(get_price(500, 0.1), 6400000)

    def test3(self):
        self.assertEqual(get_price(500, 1), 6400000)

    def test4(self):
        self.assertEqual(get_price(500, 25), 8000000)

    def test5(self):
        self.assertEqual(get_price(500, 49), 8000000)

    def test6(self):
        self.assertEqual(get_price(500, 49.9), 8000000)

    def test7(self):
        self.assertEqual(get_price(500, 50), -1)

    def test8(self):
        self.assertEqual(get_price(0, 25), -1)

    def test9(self):
        self.assertEqual(get_price(0.1, 25), 1800)

    def test10(self):
        self.assertEqual(get_price(1, 25), 18000)

    def test11(self):
        self.assertEqual(get_price(999, 25), 15984000)

    def test12(self):
        self.assertEqual(get_price(999.9, 25), 15998400)

    def test13(self):
        self.assertEqual(get_price(1000, 25), -1)

if __name__ == '__main__':
    unittest.main()