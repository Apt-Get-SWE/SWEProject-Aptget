import traceback
import logging
from flask_restx import Resource, Namespace, fields
from flask import request, session
from base64 import b64decode
from PIL import Image
from io import BytesIO
from ..types.post import Post
from ..types.address import Address
from ..types.user import User
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
        logging.info(f"Input is {base64_img}")
        if base64_img in ['', None, 'string'] or not isinstance(base64_img, str):
            # flake8: noqa
            base64_img = "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"

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
        load_user = request.args.get('loadUser')

        if aid:
            filters['aid'] = aid

        if uid:
            filters['uid'] = uid
        elif load_user and session.get('user_id'):
            filters['uid'] = session.get('user_id')

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
            current_user = User.find_one(filters={'uid': cookie_user_id})

            if cookie_user_id is None:
                return "User not logged in", 401

            post.uid = cookie_user_id  # User that creates post is the owner
            post.aid = current_user.get("aid")  # User's address is the post's address
            if post.aid is None:
                return "User does not have an address", 400

            img = post.image
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


class MarketPosts(Resource):
    def __init__(self, api=None, *args, **kwargs):
        super().__init__(api, *args, **kwargs)

    @api.doc(params={'zipcode': 'zipcode of the desired search range'})
    @api.produces(['application/json'])
    def get(self):
        """
        This endpoint retrieves all posts associated with a certain zip code. 
        """
        # use zip code to return all associated address, and use the aid's of those address to fetch all posts
        zipcode = request.args.get('zipcode')
        addresses = Address.find_all(filters={'zipcode': zipcode})
        # Extract all the 'aid' values from the 'addresses' list
        aid_list = [addr['aid'] for addr in addresses]

        # Use the '$in' operator to find all posts with matching 'aid' values
        posts_cursor = parse_json(Post.find_all({'aid': {'$in': aid_list}}))

        # Find user associated with each post
        for post in posts_cursor:
            user = User.find_one({'uid': post['uid']})
            if user is None:
                continue
            post['email'] = user['email']
            post['phone'] = user['phone']

        return {"posts": posts_cursor}, 200
