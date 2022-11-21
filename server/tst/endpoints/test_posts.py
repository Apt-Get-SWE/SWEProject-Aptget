from ...src.endpoints.posts import Posts

class TestPosts:
    def test_query(self):
        return # TODO: setup testing local db
        # Test with a valid query
        posts = Posts()
        response = posts.get()
        assert response['Type'] == 'Data'
        assert response['Title'] == 'List of posts'
        assert response['Data'] != None

    def test_post(self):
        return # TODO: setup testing local db

        json_data = {
            'pid': '1',
            'uid': '1',
            'aid': '1',
            'title': 'test title',
            'descr': 'test descr',
            'condition': 'new',
            'list_dt': '1668994811',
            'price': '100',
            'sold': False,
        }
        posts = Posts()
        response = posts.post()
        assert response[1] == 201