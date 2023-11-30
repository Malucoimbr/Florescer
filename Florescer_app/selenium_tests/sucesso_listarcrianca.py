from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurações do WebDriver (no exemplo, estou usando o Chrome)
driver = webdriver.Chrome()

# Maximiza a janela do navegador (opcional)
driver.maximize_window()

# 1. Clicar em login do header
driver.get("http://127.0.0.1:8000")
login_header = driver.find_element(By.XPATH, "/html/body/div/nav/div/div/ul/li[6]/a")
login_header.click()

# 2. Clicar em login rosa
login_rosa = driver.find_element(By.XPATH, "/html/body/section/div/div/div/div/div/div[1]/div/form/div[3]/button")
login_rosa.click()

# 3. Acionar o dropdown de crianças
dropdown_criancas = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/nav/div/div/ul/li[2]/a")))
ActionChains(driver).move_to_element(dropdown_criancas).perform()

# 4. Clicar em listar crianças
listar_crianca_xpath = "/html/body/div/nav/div/div/ul/li[2]/ul/li[2]/a"
listar_crianca = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, listar_crianca_xpath)))
listar_crianca.click()


# 16. Conferir se o texto "O Cadastro foi bem sucedido!" aparece na tela
try:
    table_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/main/section/div/table"))
    )
    print("Teste passou! A tabela de listagem de crianças está presente na página.")
except:
    print("Teste falhou! A tabela de listagem de crianças não foi encontrada ou não está presente.")
    
# Fechar o navegador no final do teste (opcional)
driver.quit()