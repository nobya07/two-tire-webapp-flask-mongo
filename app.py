from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient
from bson import ObjectId
import os
import json

app = Flask(__name__)

MONGO_URI = os.environ.get("MONGO_URI", "mongodb://mongo:27017/")
client = MongoClient(MONGO_URI)
db = client["myapp"]
collection = db["users"]


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return super().default(o)


@app.route("/")
def index():
    records = list(collection.find())
    for r in records:
        r["_id"] = str(r["_id"])
    return render_template("index.html", records=records)


@app.route("/add", methods=["POST"])
def add():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    if name and email:
        collection.insert_one({"name": name, "email": email, "message": message})

    return redirect(url_for("index"))


@app.route("/delete/<id>", methods=["POST"])
def delete(id):
    collection.delete_one({"_id": ObjectId(id)})
    return redirect(url_for("index"))


@app.route("/api/records")
def api_records():
    records = list(collection.find())
    for r in records:
        r["_id"] = str(r["_id"])
    return jsonify(records)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)