import matplotlib.pyplot as plt
from calculations import dates_present, avg_daily_price
from matplotlib.ticker import FormatStrFormatter


def plot_bar_show():
    plt.style.use('ggplot')
    fig, ax = plt.subplots()

    formatter = FormatStrFormatter('%1.2f PLN')
    ax.yaxis.set_major_formatter(formatter)

    plt.bar(dates_present, avg_daily_price, color="orangered")
    plt.xlabel('DATE')
    plt.ylabel('PRICE')
    plt.show()
