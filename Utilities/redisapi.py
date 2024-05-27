import redis
import sys
import requests
import os

import json
import sys
from datetime import timedelta

import httpx
import redis
from fastapi import FastAPI, Request



def redis_connect() -> redis.client.Redis:
    try:
        client = redis.Redis(
            host="localhost",
            port=6379,
            password="ubuntu",
            db=0,
            socket_timeout=5,
        )
        ping = client.ping()
        if ping is True:
            return client
    except redis.AuthenticationError:
        print("AuthenticationError")
        sys.exit(1)


client = redis_connect()
client.set("testkey", "somevalue")

def printkeys():
    for key in client.scan_iter():
        print(key)
#print(client.get("testkey"))

baseurl = 'https://www.weatherunion.com/gw/weather/external/v0'
apipath1 = '/get_weather_data'

#print(baseurl+apipath1)
#print(os.path.join(baseurl, apipath1))
def get_weather_data_from_api(lat: float, long: float):
    api_key = '76ceffcebbe16ce71f53c308a29d2f82'
    baseurl='https://www.weatherunion.com/gw/weather/external/v0'
    apipath1='/get_weather_data'

    url = baseurl+apipath1

    header = {'x-zomato-api-key':api_key}

    parameters = {'latitude': lat, 'longitude': long}

    response = requests.get(url, headers=header, params=parameters)

    #print(response.json())
    return response.json()

#get_weather_data_from_api(12.912372, 77.638121)



def get_weather_from_cache(key: str) -> str:
    """Data from redis."""

    val = client.get(key)
    return val


def set_weather_to_cache(key: str, value: str) -> bool:
    """Data to redis."""

    state = client.setex(
        key,
        timedelta(seconds=60),
        value=value,
    )
    return state

def getkey(latitude:float, longitude:float):
    #trucate to three decimal places
    lat = '%.2f'%(latitude)
    long = '%.2f' % (longitude)

    return (lat+"d"+long)
def route_optima(lat:float, long:float) -> dict:

    #create identifier key
    coordinates = getkey(lat, long)
    # First it looks for the data in redis cache
    data = get_weather_from_cache(key=coordinates)
    print(f"cached data : {data}")
    # If cache is found then serves the data from cache
    if data is not None:
        data = json.loads(data)
        data["cache"] = True
        return data

    else:
        # If cache is not found then sends request to the MapBox API
        data = get_weather_data_from_api(lat, long)

        # This block sets saves the respose to redis and serves it directly
        if data.get("status") == "200":
            print(f" Code = {data.get('status')}")
            data["cache"] = False
            data = json.dumps(data)
            state = set_weather_to_cache(key=coordinates, value=data)
            print(f"State = {state}")
            printkeys()
            if state is True:
                return json.loads(data)
        return data

#print (getkey(12.912372, 77.638121))





app = FastAPI()


@app.get("/weather/")
def view(request: Request) -> dict:
    """This will wrap our original route optimization API and
    incorporate Redis Caching. You'll only expose this API to
    the end user."""

    # coordinates = "90.3866,23.7182;90.3742,23.7461"
    params = request.query_params
    lat = float(params['latitude'])
    long = float(params['longitude'])
    #print(params)
    return route_optima(lat, long)