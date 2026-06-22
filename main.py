import requests
from send_message import Message

LAT = 25.23996269215846
LONG = 51.49126674249541

response = requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status()

longitude = response.json()['iss_position']['longitude']
latitude = response.json()['iss_position']['latitude']

iss_coordinates = (float(longitude), float(latitude))
my_coordinates = LAT, LONG
difference = (iss_coordinates[0] - my_coordinates[0], iss_coordinates[1] - my_coordinates[1])

print("ISS Coordinates:", iss_coordinates)
print("My Coordinates:", my_coordinates)
print("Difference:", difference)
if difference[0] > -5 < 5 and difference[1] > -5 < 5:
    print("The ISS is over you!")
    send = Message()
    send.send_email()
else:
    print("The ISS is not over you yet.")