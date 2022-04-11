
from flask import Blueprint, request
from models.categories import *
from models.connections import *
from models.posts import *
import json
from app import db

categories = Blueprint('categories',__name__)

@categories.route('/categories', methods=['GET'])
def categories_index():

    json_list = []

    for category in query_all_categories():
        json_list.append({"categoryname":category.categoryname, "id":category.id})
    return json.dumps({"categories":json_list})


@categories.route('/categories', methods=['POST'])
def add_category():

    if request.is_json:
        categoryname = request.get_json()["categoryname"]

        if len(categoryname) > 15 or " " in categoryname:
            return json.dumps({"msg":"category name didnt fit the requirements"})

        return json.dumps(add_category(categoryname))
    return json.dumps({"msg":"Request data wasn't in application/json"})


@categories.route('/categories/<name>', methods=['DELETE'])
def remove_category(name):

    if delete_category(name) == "success":

        return json.dumps({"msg":"object deleted"})
    return json.dumps({"msg":"object doesnt exist"})


@categories.route('/categories/<name>', methods=['PUT'])
def change_category(name):
    if request.is_json:
        
        return json.dumps(change_category(name, request.get_json["categoryname"]))
    return json.dumps({"msg":"Request data wasn't in application/json"})
    

@categories.route('/categories/<categoryname>', methods=['GET'])
def list_posts(categoryname):
    if get_category_from_name(categoryname):
        ConnectionsList = get_connections_from_categories(get_category_from_name(categoryname).id)
        posts_list = []

        for connection in ConnectionsList:
            blogpost = get_post_from_id(connection.blogID)
            posts_list.append({"blogpost":blogpost.blogPost, "blogID":blogpost.id})

        return json.dumps({"posts":posts_list})
    return json.dumps({"msg":"This category does not exist"})

