import matplotlib.pyplot as plt
from calculations import dates_present, boundaries, avg_daily_price, avg_weekly_price
from matplotlib.ticker import FormatStrFormatter


def plot_bar_show():
    plt.style.use('ggplot')
    fig, ax = plt.subplots()

    formatter = FormatStrFormatter('%1.2f PLN')
    ax.yaxis.set_major_formatter(formatter)

    plt.bar(dates_present, avg_daily_price, color="orangered")
    plt.title('Daily Prices')
    plt.xlabel('DATE')
    plt.ylabel('PRICE')
    plt.savefig('daily.png', )
    plt.show()


def weekly_bar_show():
    plt.style.use('ggplot')
    fig, ax = plt.subplots()

    formatter = FormatStrFormatter('%1.2f PLN')
    ax.yaxis.set_major_formatter(formatter)

    plt.bar(boundaries, avg_weekly_price, color="turquoise")  # PRABABLE ISSUE WITH BOUNDARIES FORMAT AS IT IS PROVIDED AS A LIST
    plt.title('Weekly Prices')
    plt.xlabel('DATE')
    plt.ylabel('PRICE')
    plt.savefig('weekly.png')
    plt.show()
