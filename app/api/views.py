import pandas as pd

from .base import db, fetch_collection


def eval_unit_price(item):
    factor = 1
    item['tam_ref'] = item['un']
    if item['un'] == 'g':
        factor = 1e-3# 1 g = 10^-3 kg
        item['tam_ref'] = 'kg'
    item['preco_un'] = item['preco']/(item['tam_emb']*factor)
    return item


def get_lojas():
    return fetch_collection(db, 'loja')


def get_marcas(produto):
    return fetch_collection(db, 'marca')


def get_precos(produto):
    docs = fetch_collection(db, 'preco', filter={'produto': produto})
    docs = [ eval_unit_price(doc) for doc in docs if doc['produto'] == produto ]
    return docs


def get_produtos():
    return fetch_collection(db, 'produto')
