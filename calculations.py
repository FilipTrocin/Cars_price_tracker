from database import establish_connection
from UI import user_input

connection = establish_connection()

dates = connection.distinct('FIRST_SEARCH')


def average():
    """
    Function counting an average price of that car with that specification user specified in UI
    :return:
    """
    prices = []
    objects = []
    for x, y in enumerate(dates):
        objects.extend(connection.find(
            {"MAKE": user_input[0], "MODEL": user_input[1], "YEAR": int(user_input[2]), "ENGINE_TYPE": user_input[3],
             "FIRST_SEARCH": dates[x]}))
    for item in objects:
        prices.append(item['PRICE'])

    avg = sum(prices)/len(prices)
    print(f"Average price of that car with that specification is: {round(avg, 2)}PLN")

