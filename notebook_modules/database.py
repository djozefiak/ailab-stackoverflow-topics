import pymongo

class Database:
	def __init__(self, uri="mongodb://localhost:27017/"):
		try:
			self.client = pymongo.MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=3000)
			self.client.server_info() # force connection
			print("Success: Connected to local database!")
		except pymongo.errors.ServerSelectionTimeoutError:
			self.client = None
			print("Error: Failed to connect to database!")
