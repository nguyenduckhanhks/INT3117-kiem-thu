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
        self.assertEqual(get_price(-10, -10), -1)

    def test2(self):
        self.assertEqual(get_price(-10, 5), -1)

    def test3(self):
        self.assertEqual(get_price(-10, 15), -1)

    def test4(self):
        self.assertEqual(get_price(10, -10), -1)

    def test5(self):
        self.assertEqual(get_price(10, 5), 144000)

    def test6(self):
        self.assertEqual(get_price(10, 15), 180000)

    def test7(self):
        self.assertEqual(get_price(60, -10), -1)

    def test8(self):
        self.assertEqual(get_price(60, 5), 816000)

    def test9(self):
        self.assertEqual(get_price(60, 15), 1020000)

    def test10(self):
        self.assertEqual(get_price(150, -10), -1)

    def test11(self):
        self.assertEqual(get_price(150, 5), 1920000)

    def test12(self):
        self.assertEqual(get_price(150, 15), 2400000)

if __name__ == '__main__':
    unittest.main()