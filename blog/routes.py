from flask import Blueprint, request, jsonify
from flasgger import swag_from
from .models import Post
from . import db

blog_bp = Blueprint("blog", __name__)

@blog_bp.route("/")
def home():
    return "Welcome to the Blog API!"

@blog_bp.route('/posts', methods=['POST'])
@swag_from({
    'tags': ['Posts'],
    'description': 'Create a new blog post',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'properties': {
                    'title': {'type': 'string'},
                    'content': {'type': 'string'}
                },
                'required': ['title', 'content']
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Post created successfully',
            'schema': {
                'properties': {
                    'message': {'type': 'string'},
                    'post': {'type': 'object'}
                }
            }
        },
        400: {'description': 'Bad Request'}
    }
})
def create_post():
    data = request.get_json()
    if not data or not data.get("title") or not data.get("content"):
        return jsonify({"error": "Title and content are required"}), 400

    new_post = Post(title=data["title"], content=data["content"])
    db.session.add(new_post)
    db.session.commit()
    return jsonify({"message": "Post created successfully", "post": new_post.to_dict()}), 201


@blog_bp.route('/posts', methods=['GET'])
@swag_from({
    'tags': ['Posts'],
    'description': 'Get all blog posts',
    'responses': {
        200: {
            'description': 'A list of posts',
            'schema': {
                'type': 'array',
                'items': {'type': 'object'}
            }
        }
    }
})
def get_posts():
    posts = Post.query.all()
    return jsonify([post.to_dict() for post in posts]), 200


@blog_bp.route('/posts/<int:id>', methods=['GET'])
@swag_from({
    'tags': ['Posts'],
    'description': 'Get a single post by ID',
    'parameters': [{'name': 'id', 'in': 'path', 'type': 'integer', 'required': True}],
    'responses': {200: {'description': 'Post data'}}
})
def get_post(id):
    post = Post.query.get_or_404(id)
    return jsonify(post.to_dict()), 200


@blog_bp.route('/posts/<int:id>', methods=['PUT'])
@swag_from({
    'tags': ['Posts'],
    'description': 'Update a blog post',
    'parameters': [
        {'name': 'id', 'in': 'path', 'type': 'integer', 'required': True},
        {
            'name': 'body',
            'in': 'body',
            'schema': {
                'properties': {
                    'title': {'type': 'string'},
                    'content': {'type': 'string'}
                }
            }
        }
    ],
    'responses': {200: {'description': 'Post updated'}}
})
def update_post(id):
    post = Post.query.get_or_404(id)
    data = request.get_json()
    post.title = data.get("title", post.title)
    post.content = data.get("content", post.content)
    db.session.commit()
    return jsonify({"message": "Post updated successfully", "post": post.to_dict()}), 200


@blog_bp.route('/posts/<int:id>', methods=['DELETE'])
@swag_from({
    'tags': ['Posts'],
    'description': 'Delete a blog post',
    'parameters': [{'name': 'id', 'in': 'path', 'type': 'integer', 'required': True}],
    'responses': {200: {'description': 'Post deleted'}}
})
def delete_post(id):
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return jsonify({"message": "Post deleted successfully"}), 200
