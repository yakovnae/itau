from itau import simulator

def simulate(t,arrivals):
	print("service time=" + str(t))
	x = simulator()
	arrivals = x.get_poison_arrival(t,arrivals,0)
	service_time_V = [5,4,1]
	for i in service_time_V:
		service_time = i
		min_num_of_services = x.calculate_min_num_of_services(service_time,arrivals)
		unused_services = x.calculate_unused_services(min_num_of_services,arrivals,service_time)
		print("min_services=" + str(min_num_of_services) + "  unused_services=" + str(unused_services))

simulate(.1,1000)
print("")
simulate(.5,1000)


