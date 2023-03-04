from flask_restx import Resource, Namespace, fields
from flask import request, session
from ..types.post import Post
from ..types.utils import parse_json

api = Namespace("posts", "Operations related to item posts")

POST_JSON = api.model('Post', {
    "pid": fields.String(description="Post ID", required=True),
    "aid": fields.String(description="Address ID"),
    "uid": fields.String(description="User ID"),
    "title": fields.String(description="Title of the post"),
    "descr": fields.String(description="Description of the post"),
    "condition": fields.String(description="Condition of the item", enum=['new', 'like new', 'good', 'fair', 'poor']),
    "list_dt": fields.DateTime(description="Date the item was listed"),
    "price": fields.Float(description="Price of the item", min=0),
    "sold": fields.Boolean(description="Whether the item has been sold"),
})

PID_JSON = api.model('PostID', {
    "pid": fields.String(description="Post ID", required=True),
})

GET_RESPONSE = api.model('PostGetResponse', {
    "Type": fields.String(description="Type of response"),
    "Title": fields.String(description="Title of response"),
    "Data": fields.Raw(description="Data of response"),
})


class Posts(Resource):
    def __init__(self, api=None, *args, **kwargs):
        super().__init__(api, *args, **kwargs)

    @api.produces(['application/json'])
    @api.marshal_with(GET_RESPONSE)
    def get(self):
        """
        Returns a list of all existing posts
        """
        data = parse_json(Post.find_all())
        formatted_data = {}
        for post in data:
            formatted_data[post['pid']] = post

        return {
            'Type': 'Data',
            'Title': 'List of posts',
            'Data': formatted_data
        }

    @api.expect(POST_JSON)
    @api.response(201, 'Post created successfully')
    @api.response(500, 'Error saving post')
    @api.response(415, 'Content-Type not supported!')
    @api.produces(['text/plain'])
    def post(self):
        """
        Creates a new post
        """
        # For creating a new post
        content_type = request.headers.get('Content-Type')
        if content_type == 'application/json':
            json = request.json
        else:
            return 'Content-Type not supported!', 415

        # Parse pid, aid, uid, title, descr, condition, price, sold from json
        try:
            post = Post.from_json(json)
            cookie_user_id = session.get("user_id")

            if cookie_user_id is None:
                return "User not logged in", 401

            if cookie_user_id != post.uid:
                return "User does not own post", 401

            post.save()
            return "Post created successfully", 201
        except Exception as e:
            return f'Error saving post: {e}', 500

    @api.expect(POST_JSON)
    @api.response(201, 'Post updated successfully')
    @api.response(500, 'Error updating post')
    @api.response(415, 'Content-Type not supported!')
    @api.produces(['text/plain'])
    def put(self):
        """
        Updates a post
        """
        # For updating a new post
        content_type = request.headers.get('Content-Type')
        if content_type == 'application/json':
            json = request.json
        else:
            return 'Content-Type not supported!', 415

        # Parse pid, aid, uid, title, descr, condition, price, sold from json
        try:
            post = Post.from_json(json)
            cookie_user_id = session.get("user_id")

            if cookie_user_id is None:
                return "User not logged in", 401

            if cookie_user_id != post.uid:
                return "User does not own post", 401

            post.save()
            return "Post updated successfully", 201
        except Exception as e:
            return f'Error updating post: {e}', 500

    @api.expect(PID_JSON)
    @api.response(201, 'Post deleted successfully')
    @api.response(500, 'Error deleting post')
    @api.response(415, 'Content-Type not supported!')
    @api.produces(['text/plain'])
    def delete(self):
        """
        Deletes a post
        """
        # For deleting a new post
        content_type = request.headers.get('Content-Type')
        if content_type == 'application/json':
            json = request.json
        else:
            return 'Content-Type not supported!', 415

        # Parse pid, aid, uid, title, descr, condition, price, sold from json
        try:

            post = Post.find_one(filters={'pid': json['pid']})
            cookie_user_id = session.get("user_id")

            if cookie_user_id is None:
                return "User not logged in", 401

            if cookie_user_id != post['uid']:
                return "User does not own post", 401

            Post.delete_one({'pid': json['pid']})
            return "Post deleted successfully", 201
        except Exception as e:
            return f'Error deleting post: {e}', 500
