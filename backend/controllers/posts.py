import json
from flask import Blueprint, request, jsonify, make_response
from models.posts import *
from models.connections import *
from models.categories import *


posts = Blueprint('posts',__name__)

@posts.route('/postsomething', methods=["POST"])
def createpost():
    if request.is_json:
        postdata = request.get_json()["postdata"]

        if postdata and len(postdata) <= 140:
            return make_response(add_post(postdata,request.get_json()["categories"]),200)

        return make_response(jsonify(msg="The post doesnt fit the requirements"),400)
    return make_response(jsonify(msg="Request data wasn't in application/json"),400)



@posts.route('/posts/<postid>', methods=["GET","PUT","DELETE"])
@posts.route('/categories/<categoryname>/<postid>', methods=["GET","PUT","DELETE"])
def manage_posts(postid,categoryname=None):

    if categoryname:
        categoryID = get_category_from_name(categoryname).id

        if not verify_connection(categoryID, postid):

            return make_response(jsonify(msg="No such post in this category"),404)
            
                    
    if request.method == 'GET':
        blogpost = get_post_from_id(postid)
        categories = get_post_categories(postid)
        return make_response(jsonify(blog_data=blogpost.blogPost, blogid=blogpost.id, categories=categories),200)


    if request.method == 'DELETE':
        return make_response(jsonify(delete_post(postid)))


    if request.method == 'PUT':
        postdata = request.get_json()["postdata"]

        if postdata and len(postdata) <= 140:
            return make_response(jsonify(change_post(postdata, postid, request.get_json()["categories"])),200)

        return make_response(jsonify(msg="The post doesnt fit the requirements"),400)
        
    


@posts.route('/posts', methods=['GET'])
def get_all_posts():
    posts = []
    for post in query_all_posts():
        posts.append({"post_data":post.blogPost,"id":post.id, "categories":get_post_categories(post.id)})
    return make_response(jsonify(posts=posts),200)

