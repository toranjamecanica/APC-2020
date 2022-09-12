
import pandas as pd #importando biblioteca
import plotly.express as px
import dash 
from dash import dcc
from dash  import html

def grafico():
  dados = pd.read_csv("Despesas pelo Inep.csv",encoding='latin1',sep=";")  #armazendo banco de dados

  dados_array = dados.values
  mes = []
  for linha in dados_array:
      mes.append(linha[0])
  #trabalhando dados e tranformando em lista

  ano = []
  for x in range(len(mes)):
      anos = mes[x]
      ano.append(anos[4:])
      #Adequando lista para poder trabalhar melhor no python

  lista_anos = []
  for x in ano:
      if x not in lista_anos:
          lista_anos.append(x)
  lista_anos.reverse()
  lista_anos[:]
  #criando uma nova lista de anos

  Empenhado_ano = []
  for y in range(len(lista_anos)):
    total = 0
    for x in range(len(dados['MÃªs Ano'])):
      if lista_anos[y] in dados['MÃªs Ano'][x]:
        total += float(((dados['Valor Empenhado'][x]).replace(".",'').replace(',','.')))
    Empenhado_ano.append(total)
    
  Empenhado_ano[:]
  #somatoria dos valores liquidos de cada ano

  Pago_ano = []
  for y in range(len(lista_anos)):
    total = 0
    for x in range(len(dados['MÃªs Ano'])):
      if lista_anos[y] in dados['MÃªs Ano'][x]:
        total += float(((dados['Valor Pago'][x]).replace(".",'').replace(',','.')))
    Pago_ano.append(total)
    
  Pago_ano[:]
  #somatoria de todos os valores de cada ano

  fig = px.line(x = lista_anos, y=[Pago_ano,Empenhado_ano],labels={'x':'Anos','y':'Valor Total'},title="Despesas da educação no Brasil", markers=True , template='plotly_dark')

  return fig
  #plotando o gráfico

#cria o dash para fazer o layout
app = dash.Dash(__name__)

#definimos o layout com html.Div (Separa a página em pedacinhos)
app.layout = html.Div([
    #H1 é para o título da página.
    html.H1("Apresentação grupo H"),

        #separamos mais uma parte para cada gráfico
        html.Div(children=[
            dcc.Graph(figure=grafico()),
        ]),

])


app.run_server()