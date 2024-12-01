import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Данные для примера
data = pd.DataFrame({
    "Актив": ["Акция A", "Акция B", "Акция C", "Облигация A", "Облигация B"],
    "Доходность": [5.2, 3.8, 7.1, 2.5, 3.1],
    "Тип": ["Акции", "Акции", "Акции", "Облигации", "Облигации"],
    "Цена": [100, 200, 150, 120, 180]
})

# Инициализация Dash приложения
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Dashboard: Управление инвестициями", style={"textAlign": "center"}),

    # Фильтрация по диапазону бюджета
    html.Label("Выберите диапазон бюджета:"),
    dcc.RangeSlider(
        id='budget-slider',
        min=50, max=500, step=10,
        marks={50: "$50", 500: "$500"},
        value=[100, 300]
    ),

    # Выпадающий список для выбора типа инвестиций
    html.Label("Выберите тип инвестиций:"),
    dcc.Dropdown(
        id='investment-type',
        options=[
            {'label': 'Все', 'value': 'Все'},
            {'label': 'Акции', 'value': 'Акции'},
            {'label': 'Облигации', 'value': 'Облигации'}
        ],
        value='Все',
        multi=False
    ),

    # Диаграмма с долями активов
    html.Label("Доли активов:"),
    dcc.Graph(id='pie-chart'),

    # Линейный график доходности
    html.Label("Доходность активов:"),
    dcc.Graph(id='line-chart'),

    # Форма обратной связи
    html.Label("Оставьте отзыв:"),
    dcc.Textarea(
        id='feedback-text',
        placeholder="Напишите ваш отзыв здесь...",
        style={"width": "100%", "height": "100px"}
    ),
    html.Button("Отправить", id='submit-feedback', n_clicks=0),
    html.Div(id='feedback-output', style={"marginTop": "20px", "color": "green"})
])

# Обновление графика долей активов
@app.callback(
    Output('pie-chart', 'figure'),
    [Input('budget-slider', 'value'),
     Input('investment-type', 'value')]
)
def update_pie_chart(budget_range, investment_type):
    filtered_data = data[(data["Цена"] >= budget_range[0]) & (data["Цена"] <= budget_range[1])]
    if investment_type != "Все":
        filtered_data = filtered_data[filtered_data["Тип"] == investment_type]
    fig = px.pie(filtered_data, names='Актив', values='Цена', title="Распределение активов")
    return fig

# Обновление графика доходности
@app.callback(
    Output('line-chart', 'figure'),
    [Input('budget-slider', 'value'),
     Input('investment-type', 'value')]
)
def update_line_chart(budget_range, investment_type):
    filtered_data = data[(data["Цена"] >= budget_range[0]) & (data["Цена"] <= budget_range[1])]
    if investment_type != "Все":
        filtered_data = filtered_data[filtered_data["Тип"] == investment_type]
    fig = px.line(filtered_data, x='Актив', y='Доходность', title="Доходность активов")
    return fig

# Обработка обратной связи
@app.callback(
    Output('feedback-output', 'children'),
    [Input('submit-feedback', 'n_clicks')],
    [Input('feedback-text', 'value')]
)
def handle_feedback(n_clicks, feedback_text):
    if n_clicks > 0 and feedback_text:
        return "Спасибо за ваш отзыв!"
    return ""

if __name__ == '__main__':
    app.run_server(debug=True)
