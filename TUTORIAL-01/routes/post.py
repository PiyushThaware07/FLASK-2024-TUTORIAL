from flask import Blueprint, redirect, url_for

# Create a Blueprint for post-related routes
post_bp = Blueprint("post", __name__)

@post_bp.route("/post")
def post():
    return "posts"



@post_bp.route("/post/<int:postId>")
def postById(postId):
    return f"Post by {postId}"



@post_bp.route("/technology")
def technologyPosts():
    return "These are the technology posts"



@post_bp.route("/space")
def spacePosts():
    return "These are the space posts"



@post_bp.route("/post/<string:type>")
def postByType(type):
    # Check if the type corresponds to specific routes
    if type == "technology":
        return redirect(url_for("post.technologyPosts"))
    elif type == "space":
        return redirect(url_for("post.spacePosts"))
    else:
        return f"No posts found for type: {type}", 404
