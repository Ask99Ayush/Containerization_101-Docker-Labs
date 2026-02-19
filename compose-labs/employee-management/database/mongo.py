from pymongo import MongoClient
from bson.objectid import ObjectId
import os
import sys

# Load .env ONLY for local development (safe in Docker too)
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv not installed in production, which is fine

# Read environment variables
MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME", "employee_management")

if not MONGO_URI:
    print("❌ MONGO_URI is not set", file=sys.stderr)
    sys.exit(1)

# Create MongoDB client with timeout
try:
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    client.server_info()  # Force connection check
except Exception as e:
    print(f"❌ MongoDB connection failed: {e}", file=sys.stderr)
    sys.exit(1)

# Select database & collection
db = client[DATABASE_NAME]
employees_collection = db["employees"]

# ========================
# CRUD Helper Functions
# ========================

def get_all_employees():
    """Fetch all employees"""
    return list(employees_collection.find())


def get_employee_by_id(employee_id):
    """Fetch a single employee by ObjectId"""
    return employees_collection.find_one({"_id": ObjectId(employee_id)})


def create_employee(employee_data: dict):
    """Insert a new employee"""
    return employees_collection.insert_one(employee_data)


def update_employee(employee_id, updated_data: dict):
    """Update an existing employee"""
    return employees_collection.update_one(
        {"_id": ObjectId(employee_id)},
        {"$set": updated_data}
    )


def delete_employee(employee_id):
    """Delete an employee"""
    return employees_collection.delete_one(
        {"_id": ObjectId(employee_id)}
    )