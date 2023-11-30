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

# 4. Clicar em cadastrar voluntario
cadastrar_crianca_xpath = "/html/body/div/nav/div/div/ul/li[2]/ul/li[1]/a"
cadastrar_crianca = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, cadastrar_crianca_xpath)))
cadastrar_crianca.click()

# 5 a 13. Preencher os campos
driver.find_element(By.XPATH, "/html/body/main/section/div/div/form/p[1]/input").send_keys("Maria Silva")
driver.find_element(By.XPATH, "/html/body/main/section/div/div/form/p[2]/input").send_keys("29/11/2018")
driver.find_element(By.XPATH, "/html/body/main/section/div/div/form/p[3]/input").send_keys("F")
driver.find_element(By.XPATH, "/html/body/main/section/div/div/form/p[4]/input").send_keys("50710350")
driver.find_element(By.XPATH, "/html/body/main/section/div/div/form/p[5]/input").send_keys("Rua das Flores, número 35")
driver.find_element(By.XPATH, "/html/body/main/section/div/div/form/p[6]/input").send_keys("Amendoim")
driver.find_element(By.XPATH, "/html/body/main/section/div/div/form/p[7]/input").send_keys("Amanda Silva")
driver.find_element(By.XPATH, "/html/body/main/section/div/div/form/p[8]/input").send_keys("maeteste@gmail.com")
driver.find_element(By.XPATH, "/html/body/main/section/div/div/form/p[9]/input").send_keys("81 95215484")

# 14. Rolar a página para baixo para garantir que o botão esteja visível
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# 15. Submeter o formulário usando JavaScript
submit_script = "document.querySelector('form').submit();"
driver.execute_script(submit_script)

# 16. Conferir se o texto "O Cadastro foi bem sucedido!" aparece na tela
try:
    success_message = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.XPATH, "/html/body/main"), "O Cadastro foi bem sucedido!")
    )
    print("Teste passou! O Cadastro foi bem sucedido.")
except:
    print("Teste falhou! O Cadastro não foi bem sucedido ou o texto esperado não apareceu.")

# Fechar o navegador no final do teste (opcional)
driver.quit()