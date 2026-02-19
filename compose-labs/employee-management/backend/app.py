from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
import os
import sys

app = Flask(__name__)

# Load config from environment variables
MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME", "employee_management")
SECRET_KEY = os.getenv("SECRET_KEY", "default-secret")

app.config["SECRET_KEY"] = SECRET_KEY

# Fail fast if Mongo URI is missing
if not MONGO_URI:
    print("❌ MONGO_URI is not set", file=sys.stderr)
    sys.exit(1)

# MongoDB connection (with timeout)
try:
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    client.server_info()  # Force connection check
except Exception as e:
    print(f"❌ MongoDB connection failed: {e}", file=sys.stderr)
    sys.exit(1)

db = client[DATABASE_NAME]
employees_collection = db.employees


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        role = request.form.get("role")

        if name and role:
            employees_collection.insert_one({
                "name": name,
                "role": role
            })

        return redirect(url_for("index"))

    employees = list(employees_collection.find())
    return render_template("index.html", employees=employees)


@app.route("/delete/<id>")
def delete_employee(id):
    employees_collection.delete_one({"_id": ObjectId(id)})
    return redirect(url_for("index"))


if __name__ == "__main__":
    debug_mode = os.getenv("FLASK_DEBUG", "false").lower() == "true"
    app.run(host="0.0.0.0", port=5000, debug=debug_mode)