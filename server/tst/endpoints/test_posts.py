from ...src.endpoints.posts import Posts

class TestPosts:
    def test_query(self):
        # Test with a valid query
        posts = Posts()
        response = posts.get()
        assert response['Type'] == 'Data'
        assert response['Title'] == 'List of posts'
        assert response['Data'] != None