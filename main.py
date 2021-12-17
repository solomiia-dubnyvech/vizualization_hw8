from chart_builder import *
from source import *


def task():
    country_map = load_map()
    agg_data = load_data()
    selection = get_selection()

    layered_bar = build_grouped_bar(agg_data, selection)
    stacked_bar = build_stacked_bar(agg_data, selection)
    country_chart = build_background(country_map) + build_map(country_map, selection)

    chart = country_chart & layered_bar | stacked_bar
    return add_title(chart, 'Зміна структури ВДВ у розрізі регіонів за 2017 рік порівняно з 2010 роком')


if __name__ == '__main__':
    alt.data_transformers.disable_max_rows()
    task().show()
