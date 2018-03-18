"""Retrieve stops and departures info from REST service."""


import requests


API_BASE = "https://public-transport-api.herokuapp.com"
REGION = "tallinn"


def get_nearby_stops(api_base, lat, lng):
    """
    Get nearby stops.

    :param api_base: Base URL that the endpoint gets appended to
    :param lat: Latitude
    :param lng: Longitude
    :return: List of all nearby stops
    """
    api = api_base + "/stops/" + str(lat) + "/" + str(lng)
    data = requests.get(api).json()
    list_by_distance = sorted(data, key=lambda k: int(k['distance'].replace(" m", "")))
    return list_by_distance


def get_nearest_stop(api_base, lat, lng):
    """
    Get nearest stop.

    :param api_base: Base URL that the endpoint gets appended to
    :param lat: Latitude
    :param lng: Longitude
    :return: Nearest stop
    """
    api = api_base + "/stops/" + str(lat) + "/" + str(lng)
    data = requests.get(api).json()
    if data == []:
        return None
    minDistance = min(data, key=lambda x: int(x['distance'].replace(" m", "")))
    return minDistance


def get_next_departures(api_base, region, stop_id):
    """
    Get next departures from stop.

    :param api_base: Base URL that the endpoint gets appended to
    :param region: Region
    :param stop_id: Stop ID
    :return: List of next departures from stop
    """
    api = api_base + "/departures/" + str(region) + "/" + str(stop_id)
    departures = requests.get(api).json()
    if departures == {}:
        return {}
    return departures["departures"]


def get_next_departure(api_base, region, stop_id):
    """
    Get next departure from stop.

    :param api_base: Base URL that the endpoint gets appended to
    :param region: Region
    :param stop_id: Stop ID
    :return: Next departure from stop
    """
    api = api_base + "/departures/" + str(region) + "/" + str(stop_id)
    departures = requests.get(api).json()
    if departures["departures"] == []:
        return None
    return departures["departures"][0]


if __name__ == '__main__':
    print(get_nearby_stops(API_BASE, 59.3987144, 24.668044))
    print(get_nearest_stop(API_BASE, 59.3987144, 24.668044))
    print(get_next_departures(API_BASE, REGION, get_nearest_stop(API_BASE, 59.3977111, 24.660198)["id"]))
    print(get_next_departure(API_BASE, REGION, get_nearest_stop(API_BASE, 59.3977111, 24.660198)["id"]))
