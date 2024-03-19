from flask import Flask, render_template, request
import json
from scripts import get_item_price

app = Flask(__name__)

@app.get("/home")
@app.get("/")
def index():
    return render_template('index.html')


@app.get("/market_view")
def market_view():
    server_list = ['Antica', 'Bona', 'Harmonia', 'Inabra', 'Secura']

    return render_template('market_view.html', server_list=server_list)


@app.get("/imbuement_calculator")
def imbuement_calculator():
    server_list = ['Antica', 'Bona', 'Harmonia', 'Inabra', 'Secura']
    
    with open('imbuements.json') as file:
        imbu_data = json.load(file)

    imbu_list = list(imbu_data)
    return render_template('imbuement_calculator.html', server_list=server_list, imbu_list=imbu_list)


@app.route("/_update_dropdown")
def update_dropdown():

    selected_imbu = request.args.get('selected_imbu', type=str)
    with open('imbuements.json') as file:
        imbu_data = json.load(file)
    return list(imbu_data[selected_imbu]["Imbuement Power"])

@app.route("/_result")
def result():

    selected_name = request.args.get('selected_imbu', type=str)
    selected_power = request.args.get('selected_power', type=str)
    selected_server = request.args.get('selected_server', type=str)

    with open('imbuements.json') as file:
        imbu_data = json.load(file)
        imbu_data = imbu_data[selected_name]

    desc = imbu_data["Description"]
    items = imbu_data["Imbuement Power"][selected_power]["Items"]
    amount = imbu_data["Imbuement Power"][selected_power]["Amount"]
    imbu_price = 0
    response = {'items': []}
    for idx, (item, quantity) in enumerate(items.items()):
        item_price = get_item_price(item, selected_server)['sell_offer']
        imbu_price += int(quantity) * int(item_price)
        response['items'].append((item, quantity, item_price))

    response['imbu_price'] = imbu_price
    response['description'] = desc
    response['amount'] = amount
    return response


if __name__ == '__main__':
    app.debug = True
    app.run(debug = True)
