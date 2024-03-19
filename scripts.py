from pymongo_database import MongoTibiaDB
import json
from time import perf_counter

client = MongoTibiaDB.initialize()


def get_item_price(item_name, server_name):
    """get last sell offer and buy offer"""

    sort = list({
        'time' : -1
    }.items())

    query = {
        'item_name' : item_name,
        'server_name' : server_name,
        'sell_offer' : {'$ne' : None}
    }

    data = MongoTibiaDB.find_one('items', query, sort=sort, limit=1)



    return {
        'item_name' : item_name,
        'server_name' : server_name,
        'buy_offer' : data['buy_offer'],
        'sell_offer' : data['sell_offer']
    }


def get_item_list(client):
    """get list of all items"""
    data = MongoTibiaDB.get_indexes('items')
    print(data)



if __name__ == '__main__':

    get_item_list(client)