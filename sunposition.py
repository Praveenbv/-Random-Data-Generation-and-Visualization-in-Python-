import ephem

day = '2025/3/11 16:18:00'
longitude = ephem.degrees('13.013582')
latitude = ephem.degrees('77.581200')

star = ephem.FixedBody()
star._ra = ephem.hours('16:41:42.0')
star._dec = ephem.degrees('36:28:00.0')

observer = ephem.Observer()
observer.date = day
observer.lon = longitude
observer.lat = latitude

star.compute(observer)

print('Observer', observer)
print('RA:', star.ra, 'DEC:', star.dec)
print('AZ:', star.az, 'ALT:', star.alt)
