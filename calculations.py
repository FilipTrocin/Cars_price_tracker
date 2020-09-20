from database import establish_connection, show_unique_dates
from UI import user_input
import calendar
import time
from datetime import date

connection = establish_connection()

dates = connection.distinct('FIRST_SEARCH')
dates_present = []  # dates in which car with that specification is present in database
avg_daily_price = []  # Average of daily prices
year_month = []  # date in [[year, month]] format where year and month is unique


def average():
    """
    Function counting an average price of the car with that specification user specified in UI. It shows you prices
    of car with that specification from each particular day, only when the script was running or if the car existed
    on the website on that day
    :return:
    """
    daily_prices = []  # Prices of all the cars with concrete user's specification, present in database
    # List of all cars matching user's criteria and existing in a database in concrete dates the algorithm was running
    cars = []
    for x, y in enumerate(dates):
        cars.extend(connection.find(
            {"MAKE": user_input[0], "MODEL": user_input[1], "YEAR": int(user_input[2]), "ENGINE_TYPE": user_input[3],
             "FIRST_SEARCH": dates[x]}))

    for date in cars:
        if date['FIRST_SEARCH'] not in dates_present:
            dates_present.append(date['FIRST_SEARCH'])

    for x in dates:
        temp = []
        for y in cars:
            if y['FIRST_SEARCH'] == x:
                temp.append(y['PRICE'])
                # print('DAY: ', x, 'PRICE: ', y['PRICE'])
        daily_prices.append(temp)
    # print(daily_prices, '\n')
    count = 0
    for x in daily_prices:
        condition = [item for items in daily_prices for item in items]
        if not condition:
            print('We do not have such a car in our database')
            break
        try:
            avg = sum(x) / len(x)
            avg_daily_price.append(avg)
            print(f'• On day {dates_present[count]} car with that specification cost on average {round(avg, 2)}PLN')
            count += 1
        except ZeroDivisionError:
            pass
    try:
        flatten = [item for items in daily_prices for item in items]
        overall_avg = sum(flatten) / len(flatten)
        print(
            f"Based on the past and current data the average price for car with that specification is: {round(overall_avg, 2)}PLN")
    except ZeroDivisionError:
        pass


def average_weekly():
    """
    Method counting average of all of the car prices from the week
    :return:
    """
    all_dates = []
    for date in show_unique_dates():
        temp = [date[0], date[1]]
        all_dates.append(temp)
    for x in all_dates:
        if x not in year_month:
            year_month.append(x)

    cal = calendar.Calendar()
    for date in year_month:
        to_dates(cal.monthdayscalendar(date[0], date[1]), date[1], date[0])


def to_dates(calendar, month, year):
    """
    :param month: instance of cal.monthdayscalendar(year, month)
    :return:
    """
    month_dates = []
    for week in calendar:
        week_dates = []
        for day in week:
            if day is not 0:
                week_dates.append('{}-{}-{}'.format(year, month, day))
        month_dates.append(week_dates)
    print(month_dates)
