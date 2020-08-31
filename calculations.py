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

    for x in dates:
        temporary = []
        for y in objects:
            if y['FIRST_SEARCH'] == x:
                temporary.append(y['PRICE'])
                # print('DAY: ', x, 'PRICE: ', y['PRICE'])
        prices.append(temporary)
    # print(prices, '\n')
    count = 0
    for x in prices:
        avg = sum(x)/len(x)
        print(f'On day {dates[count]} car with that specification cost on average {round(avg, 2)}PLN')
        count += 1

    flatten = [item for items in prices for item in items]
    overall_avg = sum(flatten)/len(flatten)
    print(f"Based on the past and current data the average price for car with that specification is: {round(overall_avg, 2)}PLN")

