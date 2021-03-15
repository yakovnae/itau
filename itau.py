import random
import math
class simulator:

	def get_poison_arrival(self, _lambda, num_arrivals, offset):
		t = offset
		arrivals = [float(offset)]
		for i in range(num_arrivals-1):
			p = random.random()
			inter_arrival =  -math.log(1.0 - p)/_lambda #time between 2 arrivals
			t = t + inter_arrival
			arrivals = arrivals + [t]
		return arrivals

	def calculate_min_num_of_services(self,service_time,arrivals):
		q = []
		max=0
		for i in arrivals:
			q = [s for s in q if i-s<service_time]
			q = q + [i]
			if len(q) > max:
				max = len(q)
		return max

	def calculate_unused_services(self,num_of_services,arrivals,service_time):
		q1 = []
		q2 = []
		sum = 0
		for i in arrivals:
			q1 = [s for s in q1 if i-s<service_time]

			old_q2 = len(q2)
			q2 = [s for s in q2 if i-s<service_time]
			new_q2 = len(q2)
			sum = sum + old_q2 - new_q2

			q1 = q1 + [i]

			if len(q1) <= num_of_services:
				for j in range(len(q1)+len(q2),num_of_services):
					q2 = q2 + [i]

			if len(q1)+len(q2) > num_of_services:
				q2.pop(0)
		return sum


