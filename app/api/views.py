import pandas as pd

from .base import db, extend_doc, fetch_collection


def get_precos(produto):
    docs = fetch_collection(db, 'preco', filter={'produto': produto})
    return [ extend_doc(doc) for doc in docs ]


def get_lojas():
    return fetch_collection(db, 'loja')


def get_marcas(produto):
    return fetch_collection(db, 'marca')


def get_produtos():
    return fetch_collection(db, 'produto')
