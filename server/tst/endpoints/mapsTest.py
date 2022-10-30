import pytest
from ...src.endpoints.maps import calcDistance

def calcDistanceTest():
    addr1 = (823.12, 923.17)
    addr2 = (-221.4, 2.97)
    result = calcDistance(addr1, addr2)
    assert result == 1384.557572078532

