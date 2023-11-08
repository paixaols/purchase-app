from ..db import mongodb_engine as engine

db = engine.get_database('purchaseapp')


def fetch_collection(db, col, filter={}):
    cursor = db[col].find(filter)
    docs = list(cursor)
    for doc in docs:
        doc['_id'] = str(doc['_id'])
    return docs
