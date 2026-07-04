# # NOTAS DE ESTUDOS 


# import streamlit as st
# import pandas as pd
# from sklearn.linear_model import LinearRegression


# st.header('ANALISE DE NOTAS - PREVENDO')


# estudos = pd.DataFrame({
# 'notas':[1,2,4,6,8,10,2,8],
# 'horas':[2,4,5,7,9,10,1,6]
# })


# st.line_chart(estudos, x = 'horas', y= 'notas')
# modelo_escola = LinearRegression() 
# modelo_escola.fit(estudos[['horas']], estudos['notas'])


# h_estudo = st.slider('horas de estudos', 0,12,5)
# # h_estudo2 = st.text_input('horas de estudos')
# nota_final = modelo_escola.predict([[h_estudo]])
# print(nota_final)


# st.metric(f'sua nota seria' ,f'{min(nota_final[0], 10.0):.1f}')


import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.header("Previsão de Vendas")

# Dados: [Investimento em Marketing] -> Faturamento
dados_vendas = pd.DataFrame({
    'investimento': [100, 200, 300, 400, 500, 600],
    'faturamento': [1200, 2500, 3200, 4800, 5100, 6300]
})

# 1. Exibir o gráfico de dispersão
st.scatter_chart(dados_vendas, x='investimento', y='faturamento')

# 2. Criar e treinar o modelo de Regressão Linear
modelo_vendas = LinearRegression()
modelo_vendas.fit(dados_vendas[['investimento']], dados_vendas['faturamento'])

# 3. Criar o controle interativo para o usuário definir o valor do investimento
investimento_usuario = st.slider('Investimento em Marketing ($)', 0, 1000, 300)

# 4. Realizar a previsão baseada no valor escolhido no slider
previsao_faturamento = modelo_vendas.predict([[investimento_usuario]])

# 5. Exibir o faturamento previsto de forma destacada
st.metric('Faturamento Previsto', f'$ {previsao_faturamento[0]:,.2f}')
