import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

bucket = "storage"
org = "youtube"
token = "OKcaTy6TQDjvksxWS5dNV4hcy4gmFQMrX3pAqnxqMf3IoMGI7pvoxJoUCmR0v19bQYUWYr2QDb506CQgWQBocQ=="
url = "http://localhost:8086"

client = influxdb_client.InfluxDBClient(
    url = url,
    token = token,
    org = org
)

query_api = client.query_api()
query = 'from(bucket:"storage")\
|> range(start: -10m)\
|> filter(fn:(r) => r._measurement == "measurement")\
|> filter(fn:(r) => r.building == "Trade Center")\
|> filter(fn:(r) => r._field == "temperature")'

result = query_api.query(org=org, query=query)

results = []

for table in result:
    for record in table.records:
        results.append((record.get_field(), record.get_value()))

print(results)