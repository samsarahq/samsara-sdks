import samsara_test
import csv
import time
import datetime

with open('token', 'r') as f:
    token = f.read()
# Create an ApiClient with an API access `token`. You can provide your access token to the variable `token` below.
client = samsara_test.ApiClient(header_name='Authorization', header_value='Bearer {token}'.format(token=token))

# Create an instance of the Api
api = samsara_test.VehiclesApi(api_client=client)

# Get Vehicle Locations
cursor = None
has_next_page = True
with open('most_recent_vehicle_locations.csv', 'w') as f:
    fieldnames = ['time', 'id', 'name', 'latitude', 'longitude', 'heading', 'speed', 'reverse_geocoded_address']
    csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
    csv_writer.writeheader()
    while has_next_page:
        response = api.get_vehicle_locations(after=cursor)
        for vehicle in response.data:
            row = {}
            row['time'] = vehicle.location.time
            row['id'] = vehicle.id
            row['name'] = vehicle.name
            row['latitude'] = vehicle.location.latitude
            row['longitude'] = vehicle.location.longitude
            row['heading'] = vehicle.location.heading
            row['speed'] = vehicle.location.speed
            row['reverse_geocoded_address'] = vehicle.location.reverse_geo.formatted_location
            csv_writer.writerow(row)
        cursor = response.pagination.end_cursor
        has_next_page = response.pagination.has_next_page

# Get Vehicle Locations Feed
cursor = None
has_next_page = True
with open('vehicle_location_feed_over_5_min.csv', 'w') as f:
    fieldnames = ['time', 'id', 'name', 'latitude', 'longitude', 'heading', 'speed', 'reverse_geocoded_address']
    csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
    csv_writer.writeheader()
    t_end = time.time() + 5 * 60
    while time.time() < t_end:
        response = api.get_vehicle_locations_feed(after=cursor)
        for vehicle in response.data:
            for location_event in vehicle.locations:
                row = {}
                row['time'] = location_event.time
                row['id'] = vehicle.id
                row['name'] = vehicle.name
                row['latitude'] = location_event.latitude
                row['longitude'] = location_event.longitude
                row['heading'] = location_event.heading
                row['speed'] = location_event.speed
                row['reverse_geocoded_address'] = location_event.reverse_geo.formatted_location
                csv_writer.writerow(row)
        cursor = response.pagination.end_cursor
        has_next_page = response.pagination.has_next_page
        if has_next_page == False:
            time.sleep(5)

# Get Vehicle Locations History
tz_offset = time.timezone if time.daylight==0 else time.altzone
start_time = (datetime.date.today() - datetime.timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%S") + time.strftime("%z")
end_time = datetime.date.today().strftime("%Y-%m-%dT%H:%M:%S") + time.strftime("%z")
cursor = None
has_next_page = True
with open('vehicle_location_history_yesterday.csv', 'w') as f:
    fieldnames = ['time', 'id', 'name', 'latitude', 'longitude', 'heading', 'speed', 'reverse_geocoded_address']
    csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
    csv_writer.writeheader()
    while has_next_page:
        response = api.get_vehicle_locations_history(start_time=start_time, end_time=end_time, after=cursor)
        for vehicle in response.data:
            for location_event in vehicle.locations:
                row = {}
                row['time'] = location_event.time
                row['id'] = vehicle.id
                row['name'] = vehicle.name
                row['latitude'] = location_event.latitude
                row['longitude'] = location_event.longitude
                row['heading'] = location_event.heading
                row['speed'] = location_event.speed
                row['reverse_geocoded_address'] = location_event.reverse_geo.formatted_location
                csv_writer.writerow(row)
        cursor = response.pagination.end_cursor
        has_next_page = response.pagination.has_next_page
