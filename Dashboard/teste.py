
 #importando biblioteca
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash 
from dash import  dcc, html, Input, Output




#################################################################################   DESEMPENHO ENEM ########################################################################################
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
        else:
            return (fig)

#################################################################################  DESEMPENHO PISA #########################################################################################
def pisa(opcao):
    #entrada de dados
    df = pd.read_excel("tab geral.XLSX")
    fileiras = df.values.tolist()
    values = fileiras[50]
    anos = [2009, 2012, 2015, 2018]
    #isolando valores 
    read = (values[1:5])
    math = (values[6:10])
    scie = (values[11:15])


    #gráfico geral
    fig = go.Figure()
    fig.add_trace(go.Scatter(x = anos, y = read, name = 'Leitura'))
    fig.add_trace(go.Scatter(x = anos, y = math, name = 'Matemática'))
    fig.add_trace(go.Scatter(x = anos, y = scie, name = 'Ciência'))

    fig.update_yaxes(title='Performance', showgrid=True, gridwidth=1, gridcolor='lightgrey', showline=True, linewidth=1, linecolor='black')
    fig.update_xaxes(title='Anos', showgrid=True, gridwidth=1, gridcolor='lightgrey', showline=True, linewidth=1, linecolor='black')
    fig.update_layout(title='Dados de performance em leitura, matemática e ciência por Pisa - 2009 a 2018', autosize = False, width = 800, height = 500)

    #gráfico leitura 
    fig_l = go.Figure()
    fig_l.add_trace(go.Scatter(x = anos, y = read, name = 'Leitura'))
    fig_l.update_yaxes(title='Performance', showgrid=True, gridwidth=1, gridcolor='lightgrey', showline=True, linewidth=1, linecolor='black')
    fig_l.update_xaxes(title='Anos', showgrid=True, gridwidth=1, gridcolor='lightgrey', showline=True, linewidth=1, linecolor='black')
    fig_l.update_layout(title='Dados de performance em leitura por: Pisa - 2009 a 2018', autosize = False, width = 800, height = 500)

    #gráfico matemática 
    fig_m = go.Figure()
    fig_m.add_trace(go.Scatter(x = anos, y = math, name = 'Matemática'))
    fig_m.update_yaxes(title='Performance', showgrid=True, gridwidth=1, gridcolor='lightgrey', showline=True, linewidth=1, linecolor='black')
    fig_m.update_xaxes(title='Anos', showgrid=True, gridwidth=1, gridcolor='lightgrey', showline=True, linewidth=1, linecolor='black')
    fig_m.update_layout(title='Dados de performance em matemática por: Pisa - 2009 a 2018', autosize = False, width = 800, height = 500)

    #gráfico ciência 
    fig_s = go.Figure()
    fig_s.add_trace(go.Scatter(x = anos, y = scie, name = 'Matemática'))
    fig_s.update_yaxes(title='Performance', showgrid=True, gridwidth=1, gridcolor='lightgrey', showline=True, linewidth=1, linecolor='black')
    fig_s.update_xaxes(title='Anos', showgrid=True, gridwidth=1, gridcolor='lightgrey', showline=True, linewidth=1, linecolor='black')
    fig_s.update_layout(title='Dados de performance em ciência por: Pisa - 2009 a 2018', autosize = False, width = 800, height = 500)

    #escolha do usuário.
    while True:
        answer = opcao
        if answer == '1':
            return(fig)
        elif answer == '2':
            return(fig_l)
        elif answer == '3':
            return(fig_m)
        elif answer == '4':
            return(fig_s)
        else:
            return(fig)


#################################################################################  MATRICULA PANDEMIA #########################################################################################

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

#################################################################################   DESPESAS EDU #########################################################################################
def despesas(opcao):
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

  fig = go.Figure()

  fig.add_trace(go.Scatter (x = lista_anos, y = Pago_ano, name = 'Valor pago'))
  fig.add_trace(go.Scatter (x = lista_anos, y = Empenhado_ano, name = 'Valor empenhado'))


  fig.update_yaxes(title='Valores', showgrid=True, gridwidth=1, gridcolor='lightgrey', showline=True, linewidth=1, linecolor='black')
  fig.update_xaxes(title='Anos', showgrid=True, gridwidth=1, gridcolor='lightgrey', showline=True, linewidth=1, linecolor='black')
  fig.update_layout(title='Dados sobre valores pagos e previstos para a educação pelo INEP', autosize = False, width = 1200, height = 500)


  fig_p = go.Figure()

  fig_p.add_trace(go.Scatter (x = lista_anos, y = Pago_ano, name = 'Valor pago'))

  fig_p.update_yaxes(title='Valores', showgrid=True, gridwidth=1, gridcolor='lightgrey', showline=True, linewidth=1, linecolor='black')
  fig_p.update_xaxes(title='Anos', showgrid=True, gridwidth=1, gridcolor='lightgrey', showline=True, linewidth=1, linecolor='black')
  fig_p.update_layout(title='Dados sobre valores pagos e previstos para a educação pelo INEP', autosize = False, width = 800, height = 500, template='plotly_dark')


  fig_e = go.Figure()

  fig_e.add_trace(go.Scatter (x = lista_anos, y = Pago_ano, name = 'Valor empenhado'))

  fig_e.update_yaxes(title='Valores', showgrid=True, gridwidth=1, gridcolor='lightgrey', showline=True, linewidth=1, linecolor='black')
  fig_e.update_xaxes(title='Anos', showgrid=True, gridwidth=1, gridcolor='lightgrey', showline=True, linewidth=1, linecolor='black')
  fig_e.update_layout(title='Dados sobre valores pagos e previstos para a educação pelo INEP', autosize = False, width = 800, height = 500, template='plotly_dark')



  while True:
    if opcao == '1':
        return fig()
    elif opcao == '2':
        return fig_p
    elif opcao == '3':
        return fig_e
    else:
        return fig


  #################################################################################  DASH ##################################################################################

app = dash.Dash(__name__)

app.layout = html.Div([

    html.H1("Apresentação grupo H"),


      

        dcc.Dropdown(id="Competencia",options=[
                                    {"label":"Media Geral.","value":"1"},
                                    {"label":"Media Ling.","value":"2"},
                                    {"label":"Media C.H.","value":"3"},
                                    {"label":"Media C.N.","value":"4"},
                                    {"label":"Media Mat.","value":"5"},
                                    {"label":"Media Red.","value":"6"},
                                    {"label":"Media Total.","value":"7"},
                                    ],

        placeholder='Selecione a Competencia'
        ),
        
        html.Div(id='graf_enem'
        ),

        

       # dcc.Dropdown(id="Anos",options=[{'label':'2019','value':'2019'},
       #                                 {'label':'2020','value':'2020'},
       #                                 {'label':'2021','value':'2021'},
       #                                 {'label':'2022','value':'2022'}]),


       # html.Div(id="graf_pandemia"
        #),
        
        dcc.Dropdown(id="Materia",options=[{"label":"Geral","value":"1"},
                                           {"label":"Leitura","value":"2"},
                                           {"label":"Matemática","value":"3"},
                                           {"label":"Ciências","value":"4"},
                                           ],
        
        placeholder='Selecione a Matéria'
        ),

        html.Div(id='graf_pisa'),


        html.Div(children=[dcc.Graph(figure=despesas(1))]
        ),


       
    

        

])



@app.callback(Output('graf_enem','children'),Input('Competencia','value'))

def update_output(value):
    return dcc.Graph(figure=enem(value))


@app.callback(Output('graf_pisa','children'),Input('Materia','value'))

def update_output2(value):
    
    return dcc.Graph(figure=pisa(value))

app.run_server()

        