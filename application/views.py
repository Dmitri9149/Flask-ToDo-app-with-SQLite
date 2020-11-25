from flask import render_template
from application import app

@app.route("/")
def index():
    return render_template("index.html")

    @app.route("/tasks/new/")
def tasks_form():
    return render_template("tasks/new.html")

@app.route("/tasks/", methods=["POST"])
def tasks_create():
    print(request.form.get("name"))
  
    return "hello world!"