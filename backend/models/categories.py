from app import db
from flask import make_response, jsonify
from models.connections import ConnectionsClass, delete_connections_for_category


class CategoriesClass(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    categoryname = db.Column(db.String(15), unique=True)
    def __repr__(self):
        return '<CategoriesClass %r %r>' % (self.categoryname,self.id)


def query_all_categories():
    return CategoriesClass.query.all()


def get_category_from_id(categoryID):
    return CategoriesClass.query.filter(CategoriesClass.id==categoryID).first()


def get_category_from_name(categoryname):
    return CategoriesClass.query.filter(CategoriesClass.categoryname==categoryname).first()


def delete_category(categoryname):
    removedCategory = get_category_from_name(categoryname)
    if removedCategory:
        db.session.delete(removedCategory)
        db.session.commit()
        delete_connections_for_category(categoryname)
        return make_response(jsonify(msg="Category deleted successfully"),200)
    return make_response(jsonify(msg="Category doesn't seem to exist"),400)


def add_category(categoryname):
    if not get_category_from_name(categoryname):
        db.session.add(CategoriesClass(categoryname=categoryname))
        db.session.commit()
        return make_response(jsonify(msg="Category created"),200)
    return make_response(jsonify(msg="This category already exists"),400)


def alter_category(categoryname, newname):
    changedCategory = get_category_from_name(categoryname)
    if changedCategory:
        if not get_category_from_name(newname):
            changedCategory.categoryname=newname
            db.session.commit()
            return make_response(jsonify(msg="Category name changed"),200)
        return make_response(jsonify(msg="Category with this name already exists"),400)
    return make_response(jsonify(msg="This category doesn't exist"),400)

