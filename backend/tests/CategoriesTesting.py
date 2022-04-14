from urllib import response
import pytest
import sys
from flask import Flask
from flask_cors import CORS
import json
from flask_sqlalchemy import SQLAlchemy
sys.path.append('..')
from app import app, db, DB_URI
from models.categories import CategoriesClass
#from categories import CategoriesClass
#from models import *


@pytest.fixture
def test_client():
    CORS(app)
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
    testing_client = app.test_client()
    ctx = app.app_context()
    ctx.push()

    yield testing_client
    ctx.pop


@pytest.fixture()
def init_database(db):
    yield db
    db.drop_all()


def test_categories_page(test_client):
    response = test_client.post('http://127.0.0.1:5000/categories', json=dict(categoryname="newcategory"))
    assert response.status_code == 200

    new_blog_response = test_client.post('http://127.0.0.1:5000/postsomething', json=dict(blogdata="testing blogs", categories = ["newcategory"]))
    assert new_blog_response.status_code == 200

    get_all_posts = test_client.get('http://127.0.0.1:5000/categories/newcategory')
    assert get_all_posts.status_code == 200
    assert get_all_posts.json["posts"][-1]["blogdata"] == "testing blogs"
    post_id = get_all_posts.json["posts"][-1]["id"]

    
    changing_category_response = test_client.put('http://127.0.0.1:5000/categories/newcategory', json=dict(categoryname="changedcategory"))
    assert changing_category_response.status_code == 200

    changing_blog_response = test_client.put('http://127.0.0.1:5000/categories/changedcategory/' + str(post_id), json=dict(blogdata="changedblogpost",categories=[]))
    assert changing_blog_response.status_code == 200

    get_response = test_client.get('http://127.0.0.1:5000/categories')
    assert get_response.status_code == 200
    assert get_response.json["categories"][-1]['categoryname'] == 'changedcategory'

    deleting_post =test_client.delete('http://127.0.0.1:5000/posts/' + str(post_id))
    assert deleting_post.status_code == 200

    deleting_category = test_client.delete('http://127.0.0.1:5000/categories/changedcategory')
    assert deleting_category.status_code == 200

    
    

#def test_request_example(client):
#    response = client.get("/posts")
#    assert b"<h2>Hello, World!</h2>" in response.data
