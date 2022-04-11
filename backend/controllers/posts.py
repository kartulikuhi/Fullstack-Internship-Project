from flask import Blueprint, request
from models.posts import *
from models.connections import *
from models.categories import *

import json
from app import db

posts = Blueprint('posts',__name__)

@posts.route('/postsomething', methods=["POST"])
def createpost():
    if request.is_json:
        postdata = request.get_json()["postdata"]

        if postdata and len(postdata) <= 140:
            return(add_post(postdata,request.get_json()["categories"]))

        return({"msg":"The post doesnt fit the requirements"})
    return json.dumps({"msg":"Request data wasn't in application/json"})



@posts.route('/posts/<postid>', methods=["GET","PUT","DELETE"])
@posts.route('/categories/<categoryname>/<postid>', methods=["GET","PUT","DELETE"])
def manage_posts(postid,categoryname=None):
    if categoryname:

        categoryID = get_category_from_name(categoryname).id


        if verify_connection(categoryID, postid):

            if request.method == 'GET':
                blogpost = get_post_from_id(postid)
                categories = get_post_categories(postid)
                return json.dumps({"post_data":blogpost.blogPost, "id":blogpost.id, "categories":categories})


            if request.method == 'DELETE':
                return json.dumps(delete_post(postid))


            if request.method == 'PUT':
                postdata = request.get_json()["postdata"]

                if postdata and len(postdata) <= 140:
                    return change_post(postdata, postid, request.get_json()["categories"])

                return({"msg":"The post doesnt fit the requirements"})
                    
            
            
        
        return json.dumps({"msg":"No such post in this category"})


    



@posts.route('/posts', methods=['GET'])
def get_all_posts():
    posts = []
    for post in query_all_posts():
        posts.append({"post_data":post.blogPost,"id":post.id, "categories":get_post_categories(post.id)})
    return json.dumps({"posts":posts})

