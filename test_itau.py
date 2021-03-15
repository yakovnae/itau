# Unit tests for itau.py

import unittest
import numpy
from itau import simulator

class test_simulator(unittest.TestCase):
	def test_get_poison_arrival(self):
		lambda1 = 0.1
		n_arrivals = 10000
		s = simulator()
		arrivals = s.get_poison_arrival(lambda1,n_arrivals,0)
		#print("hello")
		self.assertEqual(len(arrivals), n_arrivals)
		diff = []
		for i in range(1,len(arrivals)-1):
			diff += [arrivals[i] - arrivals[i-1]]
		self.assertTrue(numpy.abs(numpy.mean(diff) - 1/lambda1) <1)

	def test_calculate_min_num_of_services(self):
		s = simulator()
		service_time = 4

		arrivals = [0,1,2]
		self.assertEqual(s.calculate_min_num_of_services(service_time,arrivals),3)

		arrivals = [0,1,2,3]
		self.assertEqual(s.calculate_min_num_of_services(service_time,arrivals),4)

		arrivals = [0,1,2,3,4,5,6,7]
		self.assertEqual(s.calculate_min_num_of_services(service_time,arrivals),4)

	def test_calculate_unused_services(self):
		s = simulator()
		service_time = 4

		arrivals = [0,2,3,4,5]
		self.assertEqual(s.calculate_unused_services(4,arrivals,service_time),1)

		arrivals = [0,2,4,5,7,8]
		self.assertEqual(s.calculate_unused_services(4,arrivals,service_time),3)


if __name__ == '__main__':
    unittest.main(verbosity=2)