from flask import jsonify
from app import db
from models.connections import *
from models.categories import *


class PostsClass(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    blogPost = db.Column(db.String(140), unique=True)
    def __repr__(self):
        return '<PostsClass %r>' % self.blogPost


def query_all_posts():
    return PostsClass.query.all()


def get_post_from_id(postID):
    return PostsClass.query.filter(PostsClass.id==postID).first()


def get_post_categories(postID):
    response = []
    for i in ConnectionsClass.query.filter(ConnectionsClass.blogID==postID).all():
        response.append(i.categoryID)
    return response


def add_post(blogdata, categories=[]):
    new_post = PostsClass(blogPost=blogdata)
    db.session.add(new_post)

    if len(categories) > 0:
        for i in categories:
            categoryID = get_category_from_name(i).id
            create_connection(categoryID,new_post.id)
    
    db.session.commit()
    return jsonify(msg="Post created")


def delete_post(postID):

    db.session.delete(get_post_from_id(postID))
    db.session.commit()
    delete_connections_for_post(postID)

    return jsonify(msg="Post successfully deleted")


def change_post(newdata, postID, categories):

    changed_post = get_post_from_id(postID)

    if changed_post:
        changed_post.blogPost = newdata
        category_ids = []
        print(categories)
        for category in categories:                       #create connections that don't exist yet
            if not get_category_from_name(category):
                return {"msg":"category named %s doesnt exist" % category}
            categoryID = get_category_from_name(category).id

            if not verify_connection(categoryID,postID):
                create_connection(categoryID,postID)

            category_ids.append(categoryID)
        deleting_list = list(set(get_post_categories(postID)) - set(category_ids))

        for category in deleting_list:
            db.session.delete(verify_connection(category, postID))
        db.session.commit()

        return jsonify(msg="Post successfully changed")

    return jsonify(msg="this post does not seem to exist")