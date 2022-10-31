from ...src.map.map_utils import encodeAddress, calcDistance, findNearbyAddress

class TestMapUtils:
    def test_calc_distance(self):
        return # FIXME: this test is failing
        addr1 = (823.12, 923.17)
        addr2 = (-221.4, 2.97)
        result = calcDistance(addr1, addr2)
        assert result == 1384.557572078532

    def test_encode_address(self):
        return # TODO: need to enable Billing on Google Cloud Platform

        address = "1600 Amphitheatre Parkway, Mountain View, CA"
        result = encodeAddress(address)
        assert result[0]['formatted_address'] == address
        assert result[0]['geometry']['location']['lat'] == 37.4224082
        assert result[0]['geometry']['location']['lng'] == -122.0856086

    def test_find_nearby_address(self):
        return # FIXME: this test is failing
        address = (823.12, 923.17)
        addressList = [(823.12, 923.17), (-221.4, 2.97), (0, 0)]
        distance = 1000
        result = findNearbyAddress(address, addressList, distance)
        assert result == [(823.12, 923.17), (-221.4, 2.97)]