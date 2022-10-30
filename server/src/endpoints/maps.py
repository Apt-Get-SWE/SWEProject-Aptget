from cmath import sqrt
import math
import googlemaps
from datetime import datetime
from flask import redirect, request, url_for
from flask_restx import Resource

GOOGLE_API_KEY = "AIzaSyCjz6CWyd29cNaI7mLbPzDbhlBR_aIpLp4" #TODO set as environment variable

def encodeAddress(address: str):
    gmap = googlemaps.Client(key=GOOGLE_API_KEY)
    geocode = gmap.geocode(address)
    return geocode

def calcDistance(addr1, addr2):
    return sqrt((addr1[0]-addr2[0])**2 + (addr1[1]-addr2[1])**2)

def findNearbyAddress(address, addressList, distance):
    nearbyAddress = []
    for addr in addressList:
        if calcDistance(address, addr) <= distance:
            nearbyAddress.append(addr)
    return nearbyAddress

    




