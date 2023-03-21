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

write_api = client.write_api(write_options=SYNCHRONOUS)
data = influxdb_client.Point("measurement").tag("building", "Trade Center").field("temperature", 40)
write_api.write(bucket=bucket, org=org, record=data)