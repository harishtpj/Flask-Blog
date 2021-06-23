import sqlite3
from flask import Flask, render_template
from werkzeug.exceptions import abort

def connectdb():
    conn = sqlite3.connect('blog.db')
    conn.row_factory = sqlite3.Row
    return conn

def getpost(id):
    conn = connectdb()
    post = conn.execute(f"Select * from posts where id = {id}").fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

app = Flask(__name__)

@app.route("/")
def index():
    db = connectdb()
    data = db.execute("Select * from posts").fetchall()
    db.close()
    return render_template("index.html", posts = data)

@app.route("/<int:id>")
def post(id):
    data = getpost(id)
    return render_template("post.html", post = data)

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8080, debug = True)