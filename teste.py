
from cProfile import label
import pandas as pd #importando biblioteca
import plotly.express as px
import plotly.graph_objects as go
import dash 
from dash import dcc
from dash  import html

df = pd.read_excel('desempenho geral enem.xlsx')
df.head(5)

def coluna(coluna_escolhida):
  tabela = df.values.tolist()
  col = []
  for cont in range(len(tabela)):
    col.append(tabela[cont][coluna_escolhida])
  return(col)

def enem(opcao):
        # Função feita para gerar um gráfico geral e outros 6 separadamente
    #gráfico geral
    fig = go.Figure()
    fig.add_trace(go.Scatter(x = coluna(0), y = coluna(1), name = 'Média Ling.'))
    fig.add_trace(go.Scatter(x = coluna(0), y = coluna(2), name = 'Média C.H.'))
    fig.add_trace(go.Scatter(x = coluna(0), y = coluna(3), name = 'Média C.N.'))
    fig.add_trace(go.Scatter(x = coluna(0), y = coluna(4), name = 'Média Mat.'))
    fig.add_trace(go.Scatter(x = coluna(0), y = coluna(5), name = 'Média Red.'))
    fig.add_trace(go.Scatter(x = coluna(0), y = coluna(6), name = 'Total'))

    fig.update_yaxes(title='Média', showgrid=True, gridwidth=1, gridcolor='lightgrey', showline=True, linewidth=1, linecolor='black')
    fig.update_xaxes(title='Anos', showgrid=True, gridwidth=1, gridcolor='lightgrey', showline=True, linewidth=1, linecolor='black')
    fig.update_layout(title='Média no Enem x Ano', autosize = False, width = 800, height = 500)

    #gráfico de Linguagens
    fig_l = go.Figure()
    fig_l.add_trace(go.Scatter(x = coluna(0), y = coluna(1), name = 'Média Ling.'))
    fig_l.update_yaxes(title='Média', showgrid=True, gridwidth=1, gridcolor='lightgrey', showline=True, linewidth=1, linecolor='black')
    fig_l.update_xaxes(title='Anos', showgrid=True, gridwidth=1, gridcolor='lightgrey', showline=True, linewidth=1, linecolor='black')
    fig_l.update_layout(title='Média no Enem em Linguagens x Ano', autosize = False, width = 800, height = 500)

    #gráfico de Ciências Humanas
    fig_ch = go.Figure()
    fig_ch.add_trace(go.Scatter(x = coluna(0), y = coluna(2), name = 'Média C.H.'))
    fig_ch.update_yaxes(title='Média', showgrid=True, gridwidth=1, gridcolor='lightgrey', showline=True, linewidth=1, linecolor='black')
    fig_ch.update_xaxes(title='Anos', showgrid=True, gridwidth=1, gridcolor='lightgrey', showline=True, linewidth=1, linecolor='black')
    fig_ch.update_layout(title='Média no Enem em Ciências Humanas x Ano', autosize = False, width = 800, height = 500)

    #gráfico de Ciências da Natureza
    fig_cn = go.Figure()
    fig_cn.add_trace(go.Scatter(x = coluna(0), y = coluna(3), name = 'Média C.N.'))
    fig_cn.update_yaxes(title='Média', showgrid=True, gridwidth=1, gridcolor='lightgrey', showline=True, linewidth=1, linecolor='black')
    fig_cn.update_xaxes(title='Anos', showgrid=True, gridwidth=1, gridcolor='lightgrey', showline=True, linewidth=1, linecolor='black')
    fig_cn.update_layout(title='Média no Enem em Ciências da Natureza x Ano', autosize = False, width = 800, height = 500)

    #gráfico de Matemática
    fig_m = go.Figure()
    fig_m.add_trace(go.Scatter(x = coluna(0), y = coluna(4), name = 'Média Mat.'))
    fig_m.update_yaxes(title='Média', showgrid=True, gridwidth=1, gridcolor='lightgrey', showline=True, linewidth=1, linecolor='black')
    fig_m.update_xaxes(title='Anos', showgrid=True, gridwidth=1, gridcolor='lightgrey', showline=True, linewidth=1, linecolor='black')
    fig_m.update_layout(title='Média no Enem em Matemática x Ano', autosize = False, width = 800, height = 500)

    #gráfico de Redação
    fig_r = go.Figure()
    fig_r.add_trace(go.Scatter(x = coluna(0), y = coluna(5), name = 'Média Red.'))
    fig_r.update_yaxes(title='Média', showgrid=True, gridwidth=1, gridcolor='lightgrey', showline=True, linewidth=1, linecolor='black')
    fig_r.update_xaxes(title='Anos', showgrid=True, gridwidth=1, gridcolor='lightgrey', showline=True, linewidth=1, linecolor='black')
    fig_r.update_layout(title='Média no Enem em Redação x Ano', autosize = False, width = 800, height = 500)

    #gráfico Total
    fig_t = go.Figure()
    fig_t.add_trace(go.Scatter(x = coluna(0), y = coluna(6), name = 'Total'))
    fig_t.update_yaxes(title='Média', showgrid=True, gridwidth=1, gridcolor='lightgrey', showline=True, linewidth=1, linecolor='black')
    fig_t.update_xaxes(title='Anos', showgrid=True, gridwidth=1, gridcolor='lightgrey', showline=True, linewidth=1, linecolor='black')
    fig_t.update_layout(title='Média Total no Enem x Ano', autosize = False, width = 800, height = 500)

    # A interação funciona de forma que o usuário consiga escolher qual gráfico ele quer visualizar separadamente, utilizando os números de 1 a 7 para chamá-los.
    #Interação com o usuário
    while True:
        answer = opcao
        if answer == '1':
            return(fig)
        elif answer == '2':
            return(fig_l)
        elif answer == '3':
            return(fig_ch)
        elif answer == '4':
            return(fig_cn)
        elif answer == '5':
            return(fig_m)
        elif answer == '6':
            return(fig_r)
        elif answer == '7':
            return(fig_t)
        elif answer == 'sair':
            break
        else:
            print('Escolha uma opção válida.')


app = dash.Dash(__name__)

app.layout = html.Div([

    dcc.Dropdown(id="Competencia",options=[
                                {"label":"Media Ling.","value":"Média Ling."},
                                {"label":"Media C.H.","value":"Média C.H."},
                                {"label":"Media C.N.","value":"Média C.N."},]
    )

])

        