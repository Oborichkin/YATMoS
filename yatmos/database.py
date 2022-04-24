import motor.motor_asyncio

MONGO_DETAILS = "mongodb://root:example@localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.yatmos

projects = database.get_collection("projects")
