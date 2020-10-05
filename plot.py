import matplotlib.pyplot as plt
from calculations import dates_present, boundaries, avg_daily_price, avg_weekly_price
from matplotlib.ticker import FormatStrFormatter


def add_ten_dates(dates):
    """
    :param dates: list of all dates to be segregated
    :return: list of lists of 10 dates inside each internal one or the remaining dates if there was no 10
    """
    ten_dates = []
    count = 0
    temp = []
    for date in dates:
        if count < 10:
            temp.append(date)
            count += 1
        else:
            cp = temp.copy()
            ten_dates.append(cp)
            temp.clear()
            count = 0
        if date is dates[-1]:
            cp = temp.copy()
            ten_dates.append(cp)
            temp.clear()
    return ten_dates


def plot_daily_graph():
    plt.style.use('ggplot')
    fig, ax = plt.subplots(figsize=(10, 4))

    formatter = FormatStrFormatter('%1.2f PLN')
    ax.yaxis.set_major_formatter(formatter)

    plt.bar(dates_present, avg_daily_price, color="orangered")
    plt.savefig('daily.png', bbox_inches='tight')


def plot_weekly_graph():
    plt.style.use('ggplot')
    fig, ax = plt.subplots(figsize=(10, 4))

    formatter = FormatStrFormatter('%1.2f PLN')
    ax.yaxis.set_major_formatter(formatter)

    plt.bar(boundaries, avg_weekly_price, color="turquoise")
    plt.savefig('weekly.png', bbox_inches='tight')
    plt.show()
