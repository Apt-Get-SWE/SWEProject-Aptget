import traceback
from flask_restx import Resource, Namespace, fields
from flask import request, session
from base64 import b64decode
from PIL import Image
from io import BytesIO
from ..types.post import Post
from ..types.utils import parse_json

api = Namespace("posts", "Operations related to item posts")

POST_JSON = api.model('Post', {
    "pid": fields.String(description="Post ID", required=True),
    "aid": fields.String(description="Address ID"),
    "uid": fields.String(description="User ID"),
    "title": fields.String(description="Title of the post"),
    "descr": fields.String(description="Description of the post"),
    "image": fields.String(description="Base64 encoded image of the item"),
    "condition": fields.String(description="Condition of the item", enum=['new', 'like new', 'good', 'fair', 'poor']),
    "price": fields.Float(description="Price of the item", min=0),
    "sold": fields.String(description="Whether the item has been sold"),
})

GET_RESPONSE = api.model('PostGetResponse', {
    "Type": fields.String(description="Type of response"),
    "Title": fields.String(description="Title of response"),
    "Data": fields.Raw(description="Data of response"),
})


class Posts(Resource):
    def __init__(self, api=None, *args, **kwargs):
        super().__init__(api, *args, **kwargs)

    @staticmethod
    def _post_img_to_bytes(base64_img):
        img_data = b64decode(base64_img)
        img = Image.open(BytesIO(img_data))
        image_bytes = BytesIO()
        img.save(image_bytes, format=img.format)
        return image_bytes.getvalue()

    @api.produces(['application/json'])
    @api.doc(params={'aid': 'Address ID for filtering', 'uid': 'User ID for filtering'})
    @api.marshal_with(GET_RESPONSE)
    def get(self):
        """
        Returns a list of all posts that match a certain filter
        """
        # Get address ID from query string
        filters = {}

        aid = request.args.get('aid')
        uid = request.args.get('uid')

        if aid:
            filters['aid'] = aid
        if uid:
            filters['uid'] = uid

        data = parse_json(Post.find_all(filters=filters))
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
            post = Post.from_json(json, isCreate=True)
            cookie_user_id = session.get("user_id")

            if cookie_user_id is None:
                return "User not logged in", 401
            
            post.uid = cookie_user_id # User that creates post is the owner

            img = post.image
            if img:
                img = self._post_img_to_bytes(img)
            post.image = img

            post.save()
            return "Post created successfully", 201
        except Exception as e:
            # format the exception traceback as a string
            error_traceback = traceback.format_exc()
            # return the error message and traceback in the response
            return f"Error saving post: {e}\n{error_traceback}", 500

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

    @api.doc(params={'pid': 'The Post ID'})
    @api.response(201, 'Post deleted successfully')
    @api.response(500, 'Error deleting post')
    @api.response(415, 'Content-Type not supported!')
    @api.produces(['text/plain'])
    def delete(self):
        """
        Deletes a post
        """
        # For deleting a new post
        pid = request.args.get('pid')  # Get the aid from URL parameters
        if not pid:
            return "pid not provided", 400
        if not Post.exists({'pid': pid}):
            return "Post does not exist", 400

        # Parse pid, aid, uid, title, descr, condition, price, sold from json
        try:
            post = Post.find_one(filters={'pid': pid})
            cookie_user_id = session.get("user_id")

            if cookie_user_id is None:
                return "User not logged in", 401

            if cookie_user_id != post['uid']:
                return "User does not own post", 401

            Post.delete_one({'pid': pid})
            return "Post deleted successfully", 201
        except Exception as e:
            return f'Error deleting post: {e}', 500
