from ..db import mongodb_engine as engine

db = engine.get_database('purchaseapp')


def fetch_collection(db, col, filter={}):
    cursor = db[col].find(filter)
    docs = list(cursor)
    for doc in docs:
        doc['_id'] = str(doc['_id'])
    return docs


def extend_doc(doc):
    # Variedade do produto
    if doc['marca'] is None:
        a = doc['produto']
    else:
        a = doc['marca']

    if doc['quantidade'].is_integer():
        b = int(doc['quantidade'])
    else:
        b = doc['quantidade']

    c = doc['unidade']

    doc['variedade'] = f'{a} {b} {c}'

    # Preço de referência
    if doc['unidade'] == 'UN':
        factor = 10
        unit = '10 un'
    elif doc['unidade'] == 'KG':
        factor = 1
        unit = 'kg'
    elif doc['unidade'] == 'G':
        factor = 1e3
        unit = 'kg'
    elif doc['unidade'] == 'L':
        factor = 1
        unit = 'L'
    elif doc['unidade'] == 'ML':
        factor = 1e3
        unit = 'L'
    else:
        factor = 0
        unit = None
    doc['preco_ref'] = doc['preco']*factor/doc['quantidade']
    doc ['unidade_ref'] = unit

    return doc
