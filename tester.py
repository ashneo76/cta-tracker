import ctatracker#, cta.cacherouteinfo

a = ctatracker.BusTracker()
'''
print a.get_time()
print a.get_vehicles(vehicle_ids=['1567'])
print a.get_routes()



print a.get_stops('72','Eastbound')
print a.get_directions('49')

print a.get_predictions(['17404'], top=1)
'''
#from cta.models import *
print a.get_stops('1','Northbound')


#cta.cacherouteinfo.save_routes()