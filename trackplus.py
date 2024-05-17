import socket
import requests
from ip2geotools.databases.noncommercial import DbIpCity
from geopy.distance import distance
def printDetails(ip):
    res = DbIpCity.get(ip, api_key="free")
    print(f"ip address: {res.ip_address}")
    print(f"location: {res.city}, {res.region}, {res.country}")
    print(f"coordinates: (lat: {res.latitude}, lng: {res.longitude})")
ip_add = input("enter ip: ")  # 198.35.26.96
printDetails(ip_add)
def get_distance_from_location(ip, lat, lon):
    res = DbIpCity.get(ip)
    ip_lat, ip_lon = res.latitude, res.longitude
    return distance((ip_lat, ip_lon), (lat, lon)).km
server_ip = input("Server's IP : ")
lat  = float(input("Your Latitude: "))
lng = float(input("Your Longitude: "))

dist = get_distance_from_location(server_ip, lat, lng)
print(f"Distance between the server and your location is {str(dist)}km")