
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash 
from dash import dcc, html, Input, Output


################################################################################# DESEMPENHO ENEM ########################################################################################

def coluna(coluna_escolhida):
  df = pd.read_excel('desempenho geral enem.xlsx')

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
    values = fileiras[50] # amarzenando linha corespondete ao Brasil
    anos = [2009, 2012, 2015, 2018] # lista correspondente ao anos da base de dados 
    #isolando valores correspondentes as colunas de cada ano
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

    answer = opcao #parametro recebido pela função

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

def filtra_grafico(df, estado_escolhido = 'Todos'): # Função que recebe o df e uma opcção, estado e retorna o valor total
    df_lists = df.values.tolist() # Criar uma lista com o df

    data = [0, 0]
    data2 = ["Público", "Privado"]

    

    for df_list in df_lists: # Ciclo que cria uma lista de dois números inteiros com a quantidade de alunos nas redes publicas e privadas
        if estado_escolhido == 'Todos' or df_list[0]==estado_escolhido: 
            data[0] += df_list[1]
            data[1] += df_list[2]

    return pd.DataFrame(data = list(zip(data2, data)), columns = ["Nome", "Valor"]) # Retornar o dataframe formatato com os valores do ciclo de forma organizada

fig = px.pie(filtra_grafico(df), values="Valor", names="Nome") # Grafico de pizza com a quantidade de alunos de alunos 

opcoes = list(df['Estado ']) # Cria uma lista de estados da base de dados
opcoes.append('Todos') # No final da lista vai ter a soma de todos os estados

#################################################################################   DESPESAS EDU #########################################################################################
def despesas(opcao):
  dados = pd.read_csv("Despesas pelo Inep.csv",encoding='latin1',sep=";")  #armazendo banco de dados

  dados_array = dados.values #tranformar o df em uma lista 

  print(dados_array)

  mes = []
  for linha in dados_array:
      mes.append(linha[0])
  #trabalhando dados e tranformando em lista

  ano = []
  for x in range(len(mes)):
      anos = mes[x]
      ano.append(anos[4:])#armazena apenas a informação do ano 
      #Adequando lista para poder trabalhar melhor no python

  lista_anos = []
  for x in ano:
      if x not in lista_anos:# remover repetições
          lista_anos.append(x)
  lista_anos.reverse()

  #criando uma nova lista de anos


 #somatoria dos valores liquidos de cada ano
  Empenhado_ano = []
  for y in range(len(lista_anos)):
    total = 0
    for x in range(len(dados['MÃªs Ano'])):
      if lista_anos[y] in dados['MÃªs Ano'][x]:
        total += float(((dados['Valor Empenhado'][x]).replace(".",'').replace(',','.')))
    Empenhado_ano.append(total)
    
  
  

  Pago_ano = []
  for y in range(len(lista_anos)):
    total = 0
    for x in range(len(dados['MÃªs Ano'])):
      if lista_anos[y] in dados['MÃªs Ano'][x]:
        total += float(((dados['Valor Pago'][x]).replace(".",'').replace(',','.')))
    Pago_ano.append(total)
    

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
  fig_p.update_layout(title='Dados sobre valores pagos e previstos para a educação pelo INEP', autosize = False, width = 1200, height = 500)


  fig_e = go.Figure()

  fig_e.add_trace(go.Scatter (x = lista_anos, y = Empenhado_ano, name = 'Valor empenhado'))

  fig_e.update_yaxes(title='Valores', showgrid=True, gridwidth=1, gridcolor='lightgrey', showline=True, linewidth=1, linecolor='black')
  fig_e.update_xaxes(title='Anos', showgrid=True, gridwidth=1, gridcolor='lightgrey', showline=True, linewidth=1, linecolor='black')
  fig_e.update_layout(title='Dados sobre valores pagos e previstos para a educação pelo INEP', autosize = False, width = 1200, height = 500)

  resposta = opcao

  while True:
    if resposta == '1':
        return (fig)
    elif resposta == '2':
        return (fig_p)
    elif resposta == '3':
        return (fig_e)
    else:
        return (fig)


################################################################################### APROVAÇÃO ENSINO MEDIO ###################################################################
datafrane = pd.read_excel('Base taxa de aprovação ensino médio - 5 anos.xlsx')


# Listas criadas
Lista_ano = [2017,2018,2019,2020,2021]
Lista_reg = ['Brasil', 'Norte', 'Nordeste', 'Centro-Oeste', 'Sudeste', 'Sul']


def s1(y):#Recebe um valor correspondente a uma linha e retorna o valor da série 
  s1= datafrane['1 Série'].tolist()
  s1=s1[y]
  return(s1)
def s2(y):
  s2= datafrane['2 Série'].tolist()
  s2=s2[y]
  return(s2)
def s3(y):
  s3= datafrane['3 Série'].tolist()
  s3=s3[y]
  return(s3)
def s4(y):
  s4= datafrane['4 Serie'].tolist()
  s4=s4[y]
  return(s4)

# criando listas vazias
values = []
values1 = []
values2 = []
values3 = []
values4 = []
values5 = []

#calculando a média de cada unidade geográfica
for media in datafrane.values.tolist():
  if media[1] == "Brasil":
    values.append(round(sum(media[2:]) / 4, 1))
    values.reverse()
  elif media[1] == "Norte":
    values1.append(round(sum(media[2:]) / 4, 1))
    values1.reverse()
  elif media[1] == "Nordeste":
    values2.append(round(sum(media[2:]) / 4, 1))
    values2.reverse()
  elif media[1] == "Centro-Oeste":
    values3.append(round(sum(media[2:]) / 4, 1))
    values3.reverse()
  elif media[1] == "Sudeste":
    values4.append(round(sum(media[2:]) / 4, 1))
    values4.reverse()
  elif media[1] == "Sul":
    values5.append(round(sum(media[2:]) / 4, 1))
    values5.reverse()

#Gera uma tabela pra cada região com os dadas correpondentes e a media aritimética

# tabela geral do Brasil
Brasil={'Ano':Lista_ano, '1º série':[s1(0), s1(6), s1(12), s1(18), s1(24)], '2º série':[s2(0), s2(6), s2(12), s2(18), s2(24)], '3º série':[s3(0), s3(6), s3(12), s3(18), s3(24)], '4º série':[s4(0), s4(6), s4(12), s4(18), s4(24)], 'Média Brasil':values}
Brasil=pd.DataFrame(Brasil, index=[1,2,3,4,5])


# tabela região Norte
Norte={'Ano':Lista_ano, '1º série':[s1(1), s1(7), s1(13), s1(19), s1(25)], '2º série':[s2(1), s2(7), s2(13), s2(19), s2(25)], '3º série':[s3(1), s3(7), s3(13), s3(19), s3(25)], '4º série':[s4(1), s4(7), s4(13), s4(19), s4(25)], 'Média Norte':values1}
Norte=pd.DataFrame(Norte, index=[1,2,3,4,5])

# tabela região Nordeste
Nordeste={'Ano':Lista_ano, '1º série':[s1(2), s1(8), s1(14), s1(20), s1(26)], '2º série':[s2(2), s2(8), s2(14), s2(20), s2(26)], '3º série':[s3(2), s3(8), s3(14), s3(20), s3(26)], '4º série':[s4(2), s4(8), s4(14), s4(20), s4(26)], 'Média Nordeste':values2}
Nordeste=pd.DataFrame(Nordeste, index=[1,2,3,4,5])


# tabela região Centro-Oeste
Centro_Oeste={'Ano':Lista_ano, '1º série':[s1(3), s1(9), s1(15), s1(21), s1(27)], '2º série':[s2(3), s2(9), s2(15), s2(21), s2(27)], '3º série':[s3(3), s3(9), s3(15), s3(21), s3(27)], '4º série':[s4(3), s4(9), s4(16), s4(21), s4(27)], 'Média Centro_Oeste':values3}
Centro_Oeste=pd.DataFrame(Centro_Oeste, index=[1,2,3,4,5])


# tabela região Sudeste
Sudeste={'Ano':Lista_ano, '1º série':[s1(4), s1(10), s1(16), s1(22), s1(28)], '2º série':[s2(4), s2(10), s2(16), s2(22), s2(28)], '3º série':[s3(4), s3(10), s3(16), s3(22), s3(28)], '4º série':[s4(4), s4(10), s4(16), s4(22), s4(28)], 'Média Sudeste':values4}
Sudeste=pd.DataFrame(Sudeste, index=[1,2,3,4,5])


# tabela região Sul
Sul={'Ano':Lista_ano, '1º série':[s1(5), s1(11), s1(17), s1(23), s1(29)], '2º série':[s2(5), s2(11), s2(17), s2(23), s2(29)], '3º série':[s3(5), s3(11), s3(17), s3(23), s3(29)], '4º série':[s4(5), s4(11), s4(17), s4(23), s4(29)], 'Média Sul':values5}
Sul=pd.DataFrame(Sul, index=[1,2,3,4,5])



def aprovacao(opcao):
    if opcao == '1':
        figbr=px.line(Brasil, y=['1º série', '2º série', '3º série', '4º série', 'Média Brasil'], x =['2017','2018','2019','2020','2021'], title= 'Taxa de Aprovação: Brasil', markers=True)
        figbr.update_yaxes(title='Taxa de Aprovação')
        figbr.update_xaxes(title='Ano')
        return figbr
    elif opcao == '2':
        figno=px.line(Norte, y=['1º série', '2º série', '3º série', '4º série', 'Média Norte'], x =['2017','2018','2019','2020','2021'], title= 'Taxa de Aprovação: Norte', markers=True)
        figno.update_yaxes(title='Taxa de Aprovação')
        figno.update_xaxes(title='Ano')
        return figno
    elif opcao == '3':
        figne=px.line(Nordeste, y=['1º série', '2º série', '3º série', '4º série', 'Média Nordeste'], x =['2017','2018','2019','2020','2021'], title= 'Taxa de Aprovação: Nordeste', markers=True)
        figne.update_yaxes(title='Taxa de Aprovação')
        figne.update_xaxes(title='Ano')
        return figne
    elif opcao == '4':
        figco=px.line(Centro_Oeste, y=['1º série', '2º série', '3º série', '4º série', 'Média Centro_Oeste'], x =['2017','2018','2019','2020','2021'], title= 'Taxa de Aprovação: Centro-Oeste', markers=True)
        figco.update_yaxes(title='Taxa de Aprovação')
        figco.update_xaxes(title='Ano')
        return figco
    elif opcao == '5':
        figse=px.line(Sudeste, y=['1º série', '2º série', '3º série', '4º série', 'Média Sudeste'], x =['2017','2018','2019','2020','2021'], title= 'Taxa de Aprovação: Sudeste', markers=True)
        figse.update_yaxes(title='Taxa de Aprovação')
        figse.update_xaxes(title='Ano')
        return figse
    elif opcao == '6':
        figsu=px.line(Sul, y=['1º série', '2º série', '3º série', '4º série', 'Média Sul'], x =['2017','2018','2019','2020','2021'], title= 'Taxa de Aprovação: Sul', markers=True)
        figsu.update_yaxes(title='Taxa de Aprovação')
        figsu.update_xaxes(title='Ano')
        return figsu
    else: 
        figbr=px.line(Brasil, y=['1º série', '2º série', '3º série', '4º série', 'Média Brasil'], x =['2017','2018','2019','2020','2021'], title= 'Taxa de Aprovação: Brasil', markers=True)
        figbr.update_yaxes(title='Taxa de Aprovação')
        figbr.update_xaxes(title='Ano')
        return figbr



 ############################################################################################################ DASH #############################################################################################################

app = dash.Dash(__name__) # Cria o ambiente do dash

app.layout = html.Div([ # dividir o dash em blocos

    html.H1("Apresentação grupo H"),



        html.H3(
            children='''Gráfico para a comparação do número de alunos por estado '''),

        dcc.Dropdown(opcoes, value = 'Todos', id='lista de Estados'), # Dcc(Dash Core Components), componentes visuai como dropdowns e graficos
        dcc.Graph(
            id='gráfico dos Estados', # Nome do gráfico
            figure=fig # Gráfico
        ),


        html.H3(children='Dados sobre o desempenho dos candidatos do Enem nos últimos 10 anos'),#cabeçalho do grafico


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
            
            html.Div(id='graf_enem'#reserva um bloco para colocar o grafico posteriomente
            ),


        html.H3(children='Desempenho do Brasil no PISA nos ano de 2009, 2012, 2015 e 2018'),



            dcc.Dropdown(id="Materia",options=[{"label":"Geral","value":"1"},
                                            {"label":"Leitura","value":"2"},
                                            {"label":"Matemática","value":"3"},
                                            {"label":"Ciências","value":"4"},
                                            ],
            
            placeholder='Selecione a Matéria'
            ),

            html.Div(id='graf_pisa'),


        html.H3(children='Valores líquidos e valores pagos na educação pelo Inep'),


            dcc.Dropdown(id="Valores",options=[{"label":"Geral","value":"1"},
                                            {"label":"Valor pago","value":"2"},
                                            {"label":"Valor empenhado","value":"3"}
            ],
            placeholder='Selecione Um valor'
            ),

            html.Div(id='graf_valores'),


        html.H3(children='Taxa de rendimento acadêmico no Brasil - Taxa Aprovação - INEP'),
    
            dcc.Dropdown(id="regioes",options=[{"label":"Brasil","value":"1"},
                                            {"label":"Norte","value":"2"},
                                            {"label":"Nordeste","value":"3"},
                                            {"label":"Centro-Oeste","value":"4"},
                                            {"label":"Sudeste","value":"5"},
                                            {"label":"Sul","value":"6"}
                                        ],

            placeholder='Selecione a Região'
            ),
            
            html.Div(id='graf_apro'
            ),

  
])



@app.callback(
    Output('gráfico dos Estados', 'figure'),
    Input('lista de Estados', 'value')
)
def update_output(value):
    if value == 'Todos':
        fig = px.pie(filtra_grafico(df), values="Valor", names="Nome")
        return fig
    else:
        tabelafiltrada = filtra_grafico(df, value)
        fig = px.pie(tabelafiltrada, values= 'Valor', names='Nome')
        return fig





@app.callback(
    Output('graf_enem','children'),#MAnda os gaficos gerados pela função update_output pro bloco graf_enem
    Input('Competencia','value'))#recebe os valores do dropdown

def update_output(value): #recebe um parametro do input
    return dcc.Graph(figure=enem(value))# chama a função que jera os graficos e retorna para o Output




@app.callback(Output('graf_pisa','children'),Input('Materia','value'))

def update_output(value):
    
    return dcc.Graph(figure=pisa(value))




@app.callback(Output('graf_valores','children'),Input('Valores','value'))

def update_output(value):
    
    return dcc.Graph(figure=despesas(value))


@app.callback(Output('graf_apro','children'),Input('regioes','value'))

def update_output(value):
    return dcc.Graph(figure=aprovacao(value))


app.run_server()


df = pd.read_excel("tab geral.XLSX")
fileiras = df.values.tolist()
values = fileiras[50] # amarzenando linha corespondete ao Brasil
anos = [2009, 2012, 2015, 2018] # lista correspondente ao anos da base de dados 
    #isolando valores correspondentes as colunas de cada ano
read = (values[1:5]) 
math = (values[6:10])
scie = (values[11:15])

