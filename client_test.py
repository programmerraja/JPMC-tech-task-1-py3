import unittest
from client3 import getDataPoint ,getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote),((quote["stock"],quote['top_bid']['price'],quote['top_ask']['price'],(quote['top_bid']['price']+
quote['top_ask']['price'])/2)))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote),((quote["stock"],quote['top_bid']['price'],quote['top_ask']['price'],(quote['top_bid']['price']+
quote['top_ask']['price'])/2)))


  """ ------------ Add more unit tests ------------ """
  #normal prices testing for get_ratio function 
  def test_getRatio(self):
    prices=[121.2,121.68,119.2,121.68,117.7,119.1,120.09,118.8,120.45,145.56,0,34.4]
    for i in range(0,len(prices),2):
       self.assertEqual((prices[i]/prices[i+1]) ,getRatio(prices[i],prices[i+1]))

  #testing  get_ratio function if none is return when divide by zero  
  def test_getRatio_zeroDivisionError(self):
       self.assertEqual(None ,getRatio(121.1,0))
       


if __name__ == '__main__':
    unittest.main()
