import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import os
import shutil

caminho_destino_local = r"C:/Users/3001003/Downloads"
caminho_final = r"\\172.22.1.45\c$\Projetos\SIMA\Atendimento Presencial\atendimentos.csv"

driver = webdriver.Chrome()

driver.get("URL do site a ser acessado")

username = driver.find_element(By.XPATH, "//*[@id='mat-input-0']")
password = driver.find_element(By.XPATH, "//*[@id='mat-input-1']")
username.send_keys("usuario")
password.send_keys("senha")
login_button = driver.find_element(By.XPATH, "/html/body/app-root/app-login/div/div/mat-card/mat-card-content/form/button")
login_button.click()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/app-root/div/div/app-principal/mat-toolbar/button[3]/span[1]"))
)

save_button = driver.find_element(By.XPATH, "/html/body/app-root/div/div/app-principal/mat-toolbar/button[3]/span[1]")
save_button.click()

save_button = driver.find_element(By.XPATH, "//*[@id='mat-menu-panel-3']/div/div[2]/button")
save_button.click()

print('---------------------------------')
mes = format(datetime.datetime.now().month - 1, "02")
print(mes)
ano = datetime.datetime.now().year
data_inicio = f'01/01/{ano}'
data_final = f'31/{mes}/{ano}'

campo_inicio = driver.find_element(By.XPATH, "//*[@id='mat-input-0']")
campo_inicio.clear()
campo_inicio.send_keys(data_inicio)

campo_fim = driver.find_element(By.XPATH, "//*[@id='mat-input-1']")
campo_fim.clear()
campo_fim.send_keys(data_final)
print('passou daqui 1')
time.sleep(5)

baixar_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/app-root/div/div//mat-card/mat-card-content/form/div/div[5]/button"))
)
baixar_button.click()

downloaded = False
timeout = 300  
start_time = time.time()

while not downloaded and time.time() - start_time < timeout:
    time.sleep(5)  
    files = os.listdir(caminho_destino_local)
    if any(file.endswith('.xls') for file in files):  
        downloaded = True

driver.quit()


df = pd.read_excel(os.path.join(caminho_destino_local, 'relatorio.xls'))

colunas_retirar = ['CPF Solicitante', 'e-Mail Solicitante', 'Fone Solicitante', 'CPF Atendente', 'CPF Usuário Última Alteração', 'Nome Solicitante', 'Nome Atendente']
df = df.drop(columns=colunas_retirar)
df = df.rename(columns={
    'Solicitação': 'DESCRICAO',
    'Status': 'STATUS SOLICITACAO',
    'DT Fila Espera': 'FILA ESPERA',
    'DT Início Atendimento': 'INICIO ATENDIMENTO',
    'DT Fim Atendimento': 'FIM ATENDIMENTO',
    'Observação': 'OBSERVACAO',
    'Nr Procotoco': 'NR PROTOCOLO',
    'Vlr Atribuído': 'NR ATRIBUIDO',
    'DT Retorno Fim Atendimento': 'FIM ATENDIMENTO RETORNO SIMA'
})


caminho_csv_local = os.path.join(caminho_destino_local, 'atendimentos.csv')
df.to_csv(caminho_csv_local, index=False)


shutil.copyfile(caminho_csv_local, caminho_final)
print(f'Arquivo CSV substituído no servidor em {caminho_final}')


arquivos_para_deletar = ['atendimentos.csv', 'relatorio.xls']
for file in arquivos_para_deletar:
    caminho_arquivo = os.path.join(caminho_destino_local, file)
    if os.path.exists(caminho_arquivo):
        os.remove(caminho_arquivo)
        print(f'Arquivo {file} deletado da pasta de downloads')

print('Arquivos baixados foram deletados da pasta de downloads')
