from cmath import sqrt
import googlemaps

GOOGLE_API_KEY = "AIzaSyCjz6CWyd29cNaI7mLbPzDbhlBR_aIpLp4" #TODO set as environment variable

def encodeAddress(address: str):
    gmap = googlemaps.Client(key=GOOGLE_API_KEY)
    geocode = gmap.geocode(address)
    return geocode

def calcDistance(geocode1, geocode2):
    return sqrt((geocode1[0]-geocode2[0])**2 + (geocode1[1]-geocode2[1])**2)

def findNearbyAddress(geocode, geocodeList, distance):
    nearbyGeocodes = []
    for cand in geocodeList:
        if calcDistance(geocode, cand) <= distance:
            nearbyGeocodes.append(cand)
    return nearbyGeocodes