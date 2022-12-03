from cmath import sqrt
import googlemaps

# TODO set as environment variable
GOOGLE_API_KEY = "AIzaSyCjz6CWyd29cNaI7mLbPzDbhlBR_aIpLp4"


def makeRequest():
    """
    Make https requests to Google API

    Method prepares url parameters, drops None values, and gets default
    values. Finally makes request using protocol assigned to client and
    returns data.

    :param url: url part - specifies API endpoint
    :param parameters: dictionary of url parameters
    :param result_key: key in output where result is expected
    """
    # TODO: implement make request
    ...


def serializeParameters(parameters):
    """
    Serialize parameters from python native types to match that specified in google api docs

    parameters: dictionary of query parameters
    """
    serializedParam = {}
    for key, value in parameters.items():
        if isinstance(value, bool):
            serializedParam[key] = 'true' if value else 'false'
        elif isinstance(value, dict):
            serializedParam[key] = "|".join(
                ("%s:%s" % (k, v) for k, v in value.items()))
        elif isinstance(value, (list, tuple)):
            serializedParam[key] = "|".join(value)
    return serializedParam


def encodeAddress(address: str):
    gmap = googlemaps.Client(key=GOOGLE_API_KEY)
    geocode = gmap.geocode(address)
    return geocode


def calcDistance(geocode1, geocode2):
    return sqrt((geocode1[0] - geocode2[0]) ** 2 + (geocode1[1] - geocode2[1]) ** 2)


def findNearbyAddress(geocode, geocodeList, distance):
    nearbyGeocodes = []
    for cand in geocodeList:
        if calcDistance(geocode, cand) <= distance:
            nearbyGeocodes.append(cand)
    return nearbyGeocodes
