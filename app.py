

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from time import sleep
import openpyxl


#1 - Navegar até o site https://contabilidade-devaprender.netlify.app/
driver = webdriver.Chrome()
driver.get('https://contabilidade-devaprender.netlify.app/')
sleep(5)

#3 - Digitar a senha

#Pegando o XPATH dos campos de login
#2 - Digitar e-mail 
email = driver.find_element(By.XPATH,"//input[@id='email']")
sleep(2)
email.send_keys('test@gmail.com')

#3 - Digitar a senha
senha = driver.find_element(By.XPATH,"//input[@id='senha']")
sleep(2)
senha.send_keys('passwordtesting')

#4 - clicar em entrar
botao_entrar = driver.find_element(By.XPATH,"//button[@id='Entrar']").click()
sleep(10)


#5 - Clicar em cada campo e preencher as informações extraida da planilha "empresas.xlsx"
empresas = openpyxl.load_workbook('./empresas.xlsx')
pagina_empresas = empresas['dados empresas']

#Pegando dados das colunas da planilha
for linha in pagina_empresas.iter_rows(min_row=2, values_only=True, max_row=2):
    nome_empresa, email, telefone, endereco, cnpj, area_atuacao, quantidade_funcionario, data_fundacao = linha

    driver.find_element(By.ID, 'nomeEmpresa').send_keys(nome_empresa)
    sleep(1)
    driver.find_element(By.ID, 'emailEmpresa').send_keys(email)
    sleep(1)
    driver.find_element(By.ID, 'telefoneEmpresa').send_keys(telefone)
    sleep(1)
    driver.find_element(By.ID, 'enderecoEmpresa').send_keys(endereco)
    sleep(1)
    driver.find_element(By.ID, 'cnpj').send_keys(cnpj)
    sleep(1)
    driver.find_element(By.ID, 'areaAtuacao').send_keys(area_atuacao)
    sleep(1)
    driver.find_element(By.ID, 'numeroFuncionarios').send_keys(quantidade_funcionario)
    sleep(1)
    driver.find_element(By.ID, 'dataFundacao').send_keys(data_fundacao)
    sleep(1)
  

#6 - Clicar em cadastrar
cadastrar = driver.find_element(By.ID, 'Cadastrar').click()
sleep(3)
# O processo de repetição vai ser com base na quantiade de casdatros a serem realizados
