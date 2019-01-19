
import CoreLocation
from time import sleep

for i in range(10):
    manager = CoreLocation.CLLocationManager.alloc().init()
    manager.delegate()
    manager.startUpdatingLocation()

    while CoreLocation.CLLocationManager.authorizationStatus() != 3 or manager.location() is None:
        sleep(.1)
    coord = manager.location().coordinate()
    lat, lon = coord.latitude, coord.longitude
    print(lat,lon)
    sleep(5)

