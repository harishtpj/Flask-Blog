import sqlite3
from flask import Flask, render_template

def connectdb():
    conn = sqlite3.connect('blog.db')
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)

@app.route("/")
def index():
    db = connectdb()
    data = db.execute("Select * from posts").fetchall()
    db.close()
    return render_template("index.html", posts = data)

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8080, debug = True)