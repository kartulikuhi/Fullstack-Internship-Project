
from app import db

class ConnectionsClass(db.Model):
    __tablename__ = 'connections'
    id = db.Column(db.Integer, primary_key=True)
    blogID = db.Column(db.Integer, unique=True)
    categoryID = db.Column(db.Integer, unique=True)
    def __repr__(self):
        return '<PostsClass %r %r>' % (self.blogID, self.categoryID)

def get_connections_from_categories(categoryID):
    return ConnectionsClass.query.filter(ConnectionsClass.categoryID==categoryID).all()


def verify_connection(categoryID,blogID):
    return ConnectionsClass.query.filter(ConnectionsClass.blogID == blogID, ConnectionsClass.categoryID == categoryID).first()


def create_connection(categoryID,blogID):
    db.session.add(ConnectionsClass(blogID=blogID, categoryID=categoryID))
    db.session.commit()



def delete_connections_for_post(postID):
    for post in ConnectionsClass.query.filter(ConnectionsClass.blogID==postID).all():
        db.session.delete(post)
    db.session.commit()


def delete_connections_for_category(categoryID):
    for category in ConnectionsClass.query.filter(ConnectionsClass.categoryID==categoryID).all():
        db.session.delete(category)
    db.session.commit()
