from itertools import islice
from lxml import etree as et
from tqdm import tqdm
import pymongo
import sys

from import_modules.constants import POSTS_SIZE, CHUNK_SIZE
from import_modules.posts import attrib_to_dict

try:
	client = pymongo.MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=3000)
	client.server_info() # force connection
except pymongo.errors.ServerSelectionTimeoutError:
	print("Error: Failed to connect to database!")
	sys.exit(-1)

# database
stackoverflow = client["stackoverflow"]

# collection
posts = stackoverflow["posts"]

pbar = tqdm(total=POSTS_SIZE, ascii=True, unit='items', mininterval=1)

def chunks(iterable, chunksize):
	it = iter(iterable)
	while (chunk := tuple(islice(it, chunksize))):
		yield chunk

if __name__ == "__main__":
	try:
		for chunk in chunks(et.iterparse("stack_exchange_data_dump/Posts.xml", tag="row"), CHUNK_SIZE):
			try:
				elements = []
				for _, elem in chunk:
					elements.append(attrib_to_dict(elem.attrib))
					elem.clear()
				posts.insert_many(elements, ordered=False)
			except pymongo.errors.BulkWriteError:
				# skip element
				pass
			finally:
				pbar.update(len(chunk))
	except KeyboardInterrupt:
		pbar.write(f"\nAborting: Imported {pbar.n} items of {pbar.total} total items.")
		pbar.close()
