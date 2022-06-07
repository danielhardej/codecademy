import surfshop
import unittest
import datetime

class SurfShopTestCase(unittest.TestCase):
  def setUp(self):
    self.cart = surfshop.ShoppingCart()

  def test_add_surfboard(self):
    self.assertEqual(self.cart.add_surfboards(1), 'Successfully added 1 surfboard to cart!')

  #def test_add_surfboards(self):
  #  self.assertEqual(self.cart.add_surfboards(2), 'Successfully added 2 surfboards to cart!')

  def test_add_surfboards(self):
    for i in range(2, 5):
      with self.subTest(i=i):
        self.assertEqual(self.cart.add_surfboards(i), f'Successfully added {i} surfboards to cart!')
        self.cart = surfshop.ShoppingCart()

  # @unittest.skip
  def test_too_many_boards(self):
    self.assertRaises(surfshop.TooManyBoardsError, self.cart.add_surfboards, 5)

  # @unittest.expectedFailure
  def test_locals_discount(self):
    self.cart.apply_locals_discount()
    self.assertTrue(self.cart.locals_discount)

  def test_checkout_date(self):
    # self.cart.set_checkout_date()
    date = datetime.datetime.now()
    self.assertRaises(surfshop.CheckoutDateError, self.cart.set_checkout_date, date)


unittest.main()
