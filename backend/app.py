from flask import Flask, redirect
from environment.config import DB_URI
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

with app.app_context():
    from controllers import posts, categories

app.register_blueprint(categories.categories)
app.register_blueprint(posts.posts)

@app.route('/')
def home():
    return redirect('/categories')
    

if __name__ == '__main__':
    app.run(debug=True)