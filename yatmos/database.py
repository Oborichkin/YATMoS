import os
import asyncio

import motor.motor_asyncio

MONGO_DETAILS = "mongodb://root:example@localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

env = os.environ.get("ENVIRONMENT", "development")

if env == "testing":
    client.get_io_loop = asyncio.get_running_loop

db = client[f"yatmos_{env}"]

projects = db.get_collection("projects")
