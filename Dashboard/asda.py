fig = go.Figure()

fig.add_trace(go.Scatter (x = lista_anos, y = Pago_ano, name = 'Valor pago'))
fig.add_trace(go.Scatter (x = lista_anos, y = Empenhado_ano, name = 'Valor empenhado'))


fig.update_yaxes(title='Valores', showgrid=True, gridwidth=1, gridcolor='lightgrey', showline=True, linewidth=1, linecolor='black')
fig.update_xaxes(title='Anos', showgrid=True, gridwidth=1, gridcolor='lightgrey', showline=True, linewidth=1, linecolor='black')
fig.update_layout(title='Dados sobre valores pagos e previstos para a educação pelo INEP', autosize = False, width = 800, height = 500, template='plotly_dark')


########################################################grafico de pagos###########################################################
fig_p = go.Figure()

fig_p.add_trace(go.Scatter (x = lista_anos, y = Pago_ano, name = 'Valor pago'))

fig_p.update_yaxes(title='Valores', showgrid=True, gridwidth=1, gridcolor='lightgrey', showline=True, linewidth=1, linecolor='black')
fig_p.update_xaxes(title='Anos', showgrid=True, gridwidth=1, gridcolor='lightgrey', showline=True, linewidth=1, linecolor='black')
fig_p.update_layout(title='Dados sobre valores pagos e previstos para a educação pelo INEP', autosize = False, width = 800, height = 500, template='plotly_dark')

#########################################################gafico de emoenhados##############################################################

fig_e = go.Figure()

fig_e.add_trace(go.Scatter (x = lista_anos, y = Pago_ano, name = 'Valor empenhado'))

fig_e.update_yaxes(title='Valores', showgrid=True, gridwidth=1, gridcolor='lightgrey', showline=True, linewidth=1, linecolor='black')
fig_e.update_xaxes(title='Anos', showgrid=True, gridwidth=1, gridcolor='lightgrey', showline=True, linewidth=1, linecolor='black')
fig_e.update_layout(title='Dados sobre valores pagos e previstos para a educação pelo INEP', autosize = False, width = 800, height = 500, template='plotly_dark')


opcao = input()

while True:
  if opcao == '1':
    fig.show()
  elif opcao == '2':
    fig_p.show()
  elif opcao == '3':
    fig_e.show()