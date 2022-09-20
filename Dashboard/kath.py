from dash import Dash, html, dcc, Input, Output
import dash
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

df = pd.read_excel('Estudantes.xlsx')

def filtra_grafico(df, estado_escolhido = 'todos'):
    df_lists = df.values.tolist()

    data = [0, 0]
    data2 = ["Público", "Privado"]

    for df_list in df_lists:
        if estado_escolhido == 'todos' or df_list[0]==estado_escolhido:
            data[0] += df_list[1]
            data[1] += df_list[2]

    return pd.DataFrame(data = list(zip(data2, data)), columns = ["Nome", "Valor"])

fig = px.pie(filtra_grafico(df), values="Valor", names="Nome")

opcoes = list(df['Estado '])
opcoes.append('todos')

app.layout = html.Div(children=[
    html.H1(children='Número de estudantes matriculados'),

    html.Div(children='''
        Gráfico para a comparação do número de alunos por estado
    '''),
    dcc.Dropdown(opcoes, value = 'todos', id='lista de Estados'),
    dcc.Graph(
        id='gráfico dos Estados',
        figure=fig
    )
])
@app.callback(
    Output('gráfico dos Estados', 'figure'),
    Input('lista de Estados', 'value')
)
def update_output(value):
    if value == 'todos':
        fig = px.pie(filtra_grafico(df), values="Valor", names="Nome")
        return fig
    else:
        tabelafiltrada = filtra_grafico(df, value)
        fig = px.pie(tabelafiltrada, values= 'Valor', names='Nome')
        return fig

if __name__ == '_main_':
    app.run_server(debug=True)