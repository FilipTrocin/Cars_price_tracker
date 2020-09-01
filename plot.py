import matplotlib.pyplot as plt
from calculations import dates_present, avg_daily_price


def plot_bar_show():
    plt.style.use('classic')
    plt.bar(dates_present, avg_daily_price)
    plt.xlabel('DATE')
    plt.ylabel('PRICE')
    plt.show()
