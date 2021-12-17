import altair as alt


def get_selection():
    return alt.selection_single(fields=['region'], on='mouseover', empty='all')


def build_background(country):
    return alt.Chart(country).project().mark_geoshape(fill='lightgray', stroke='white')


def build_map(world, selection):
    return alt.Chart(world).project().mark_geoshape(stroke='white').encode(
        color=alt.condition(selection, alt.value('gold'), alt.value('lightsteelblue')),
        tooltip=alt.Tooltip('region:N'),
    ).add_selection(selection)


def build_stacked_bar(data, selection):
    axis = alt.Axis(labelExpr='datum.value * 100')
    return alt.Chart(data).mark_bar().encode(
        x='year:O',
        y=alt.Y('mean(value):Q', title='Відсотки, %', stack='normalize', scale=alt.Scale(clamp=True), axis=axis),
        color="category:N",
    ).transform_filter(selection)


def build_grouped_bar(data, selection):
    legend = alt.Legend(
        title='Категорії',
        values=['сільське господарство', 'промисловість', 'будівництво', 'послуги', 'державне управління'],
    )

    return alt.Chart(data).mark_bar(align='left', opacity=0.7).encode(
        x=alt.X('mean(value):Q', title='Відсотки, %', stack=None, scale=alt.Scale(domain=(0, 100))),
        y=alt.Y('category:O', title='Категорії'),
        color=alt.Color("year:N", scale=alt.Scale(scheme='set1'), legend=legend),
    ).transform_filter(selection)


def add_title(chart, title):
    return chart.properties(
        title=title,
    ).configure_title(
        fontSize=24,
        font='Courier',
        anchor='middle',
        dy=-30
    )
