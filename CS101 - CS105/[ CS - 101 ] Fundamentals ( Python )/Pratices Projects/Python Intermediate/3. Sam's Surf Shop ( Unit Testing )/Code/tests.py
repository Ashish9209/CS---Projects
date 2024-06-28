
import surfshop
import unittest

class test_surfshop(unittest.TestCase):
  
  def setUp(self):
    self.cart = surfshop.ShoppingCart()

  def test_add_surfboards1(self):
    message1 = self.cart.add_surfboards(quantity = 1)
    self.assertEqual(message1, f"Successfully added 1 surfboard to cart!")
    
  def test_add_surfboards2(self):
    for i in [2, 3, 4]:
      with self.subTest(i=i):
        message2 = self.cart.add_surfboards(i)
        self.assertEqual(message2, f"Successfully added {i} surfboards to cart!")
        self.cart = surfshop.ShoppingCart()

  @unittest.skip
  def test_too_many_boards(self):
    self.assertRaises(surfshop.TooManyBoardsError, self.cart.add_surfboards, 5)
  
  
  def test_locals_discount(self):
    self.cart.apply_locals_discount()
    self.assertTrue(self.cart.locals_discount)

unittest.main()

