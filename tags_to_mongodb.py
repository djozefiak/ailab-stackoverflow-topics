from lxml import etree as et
from tqdm import tqdm
import pymongo
import sys

from import_modules.constants import TAGS_SIZE
from import_modules.tags import attrib_to_dict

try:
	client = pymongo.MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=3000)
	client.server_info() # force connection
except pymongo.errors.ServerSelectionTimeoutError:
	print("Error: Failed to connect to database!")
	sys.exit(-1)

# database
stackoverflow = client["stackoverflow"]

# collection
tags = stackoverflow["tags"]

pbar = tqdm(total=TAGS_SIZE, ascii=True, unit='items', mininterval=0.1)

if __name__ == "__main__":
	try:
		for event, elem in et.iterparse("stack_exchange_data_dump/Tags.xml", tag="row"):
			try:
				tags.insert_one(attrib_to_dict(elem.attrib))
			except pymongo.errors.DuplicateKeyError as e:
				pbar.write(f"Conflict: Document with Id <{elem.attrib.get('Id')}> already exists in database!")
			elem.clear()
			pbar.update(1)
		pbar.close()
	except KeyboardInterrupt:
		pbar.write(f"Aborting: Imported {pbar.n} items of {pbar.total} total items.")
		pbar.close()
