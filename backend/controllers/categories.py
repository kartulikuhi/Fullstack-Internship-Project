
from flask import Blueprint, request, jsonify, make_response
from models.categories import *
from models.connections import *
from models.posts import *

from app import db

categories = Blueprint('categories',__name__)

@categories.route('/categories', methods=['GET'])
def categories_index():

    json_list = []

    for category in query_all_categories():
        json_list.append({"categoryname":category.categoryname, "id":category.id})
    return make_response(jsonify(categories=json_list),200)


@categories.route('/categories', methods=['POST'])
def new_category():

    if request.is_json:
        categoryname = request.get_json()["categoryname"]

        if len(categoryname) > 15 or " " in categoryname:
            return make_response(jsonify(msg="category name didnt fit the requirements"),400)

        return add_category(categoryname)
    return make_response(jsonify(msg="Request data wasn't in application/json"),400)


@categories.route('/categories/<name>', methods=['DELETE'])
def remove_category(name):

    return delete_category(name)


@categories.route('/categories/<name>', methods=['PUT'])
def change_category(name):

    if request.is_json:
        newname = request.get_json()["categoryname"]
        if newname != '' and len(newname) < 16 and newname.isalpha() and " " not in newname:
            return alter_category(name, newname)
    return make_response(jsonify(msg="Request data wasn't in application/json"),400)
    

@categories.route('/categories/<categoryname>', methods=['GET'])
def list_posts(categoryname):
    if get_category_from_name(categoryname):
        ConnectionsList = get_connections_from_categories(get_category_from_name(categoryname).id)
        posts_list = []

        for connection in ConnectionsList:
            blogpost = get_post_from_id(connection.blogID)
            posts_list.append({"blogdata":blogpost.blogdata,"id":blogpost.id, "categories":get_post_categories(blogpost.id)})

        return make_response(jsonify(posts=posts_list),200)
    return make_response(jsonify(msg="This category does not exist"),400)

