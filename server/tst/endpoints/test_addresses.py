from ...src.endpoints.addresses import Addresses

class TestPosts:
    def test_query(self):
        return # TODO: setup testing local db
        # Test with a valid query
        addr = Addresses()
        response = addr.get()
        assert response['Type'] == 'Data'
        assert response['Title'] == 'List of addresses'
        assert response['Data'] != None