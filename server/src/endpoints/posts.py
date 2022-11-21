from flask_restful import Resource
from flask import request
from ..types.post import Post
from ..types.utils import parse_json

class Posts(Resource):
    def get(self):
        data = parse_json(Post.find_all())
        formatted_data = {}
        for post in data:
            formatted_data[post['pid']] = post

        return {
            'Type' : 'Data',
            'Title' : 'List of posts',
            'Data' : formatted_data
        }

    def post(self):
        # For creating a new post
        content_type = request.headers.get('Content-Type')
        if content_type == 'application/json':
            json = request.json
        else:
            return 'Content-Type not supported!', 415

        # Parse pid, aid, uid, title, descr, condition, price, sold from json
        post = Post.from_json(json)
        try:
            post.save()
            return "Post created successfully", 201
        except Exception as e:
            return f'Error saving post: {e}', 500