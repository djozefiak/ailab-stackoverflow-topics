from lxml import etree as et
from tqdm import tqdm
import multiprocessing as mp
import pymongo
import sys, signal, os

from import_modules.constants import POSTS_SIZE
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

def handler(signum, frame):
	pbar.write(f"\nStopping worker <{os.getpid()}>")
def init_worker():
	signal.signal(signal.SIGINT, handler)
def update(*args):
	pbar.update()

def work(arg):
	try:
		posts.insert_one(attrib_to_dict(et.fromstring(arg).attrib))
	except pymongo.errors.DuplicateKeyError:
		#pbar.write(f"Conflict: Document with Id <{elem.attrib.get('Id')}> already exists in database!")
		pass

if __name__ == "__main__":
	pool = mp.Pool(4, init_worker)
	try:
		for event, elem in et.iterparse("stack_exchange_data_dump/Posts.xml", tag="row"):
			pool.apply_async(work, args=(et.tostring(elem),), callback=update) 
			elem.clear()
		pool.close()
	except KeyboardInterrupt:
		pbar.write(f"\nAborting: Imported {pbar.n} items of {pbar.total} total items.")
		pool.terminate()
	finally:
		pbar.close()
		pool.join()
