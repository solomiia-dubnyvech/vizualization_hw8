import pandas as pd
import geopandas as gpd


def load_map():
    gdf = gpd.read_file('ukraine.json')
    gdf['region'] = gdf['NAME_1']
    return gdf.loc[:, ['region', 'geometry']]


def load_data():
    df = pd.read_csv('1.4_02.csv')
    return melt(_correct_data(df))


def _correct_data(df: pd.DataFrame):
    def extract_year(x: str):
        return int(x.split(',')[1])

    def extract_region(x: str):
        country = x.split(', ')[0]
        if country == 'Україні':
            return 'Ukraine'
        elif country == 'Вінницька':
            return 'Vinnytsya'
        elif country == 'Волинська':
            return 'Volyn'
        elif country == 'Дніпропетровська':
            return "Dnipropetrovs'k"
        elif country == 'Донецька':
            return "Donets'k"
        elif country == 'Житомирська':
            return "Zhytomyr"
        elif country == 'Закарпатська':
            return 'Transcarpathia'
        elif country == 'Запорізька':
            return 'Zaporizhzhya'
        elif country == 'Івано-Франківська':
            return "Ivano-Frankivs'k"
        elif country == 'Київська':
            return 'Kyiv'
        elif country == 'Кіровоградська':
            return 'Kirovohrad'
        elif country == 'Луганська':
            return "Luhans'k"
        elif country == 'Львівська':
            return "L'viv"
        elif country == 'Миколаївська':
            return 'Mykolayiv'
        elif country == 'Одеська':
            return 'Odesa'
        elif country == 'Полтавська':
            return 'Poltava'
        elif country == 'Рівненська':
            return 'Rivne'
        elif country == 'Сумська':
            return 'Sumy'
        elif country == 'Тернопільська':
            return "Ternopil'"
        elif country == 'Харківська':
            return 'Kharkiv'
        elif country == 'Херсонська':
            return 'Kherson'
        elif country == 'Хмельницька':
            return "Khmel'nyts'kyy"
        elif country == 'Черкаська':
            return 'Cherkasy'
        elif country == 'Чернівецька':
            return 'Chernivtsi'
        elif country == 'Чернігівська':
            return 'Chernihiv'
        elif country == 'м.Київ':
            return 'Kyiv City'

    df['year'] = df['Регіон, рік'].apply(extract_year)
    df['region'] = df['Регіон, рік'].apply(extract_region)
    fields = ['region', 'year', 'сільське господарство', 'промисловість', 'будівництво', 'послуги', 'державне управління']
    return df.loc[:, fields]


def melt(df):
    return pd.melt(
        df,
        id_vars=['region', 'year'],
        var_name='category',
        value_vars=['сільське господарство', 'промисловість', 'будівництво', 'послуги', 'державне управління'],
    )


if __name__ == '__main__':
    data = load_data()
    print(data)
