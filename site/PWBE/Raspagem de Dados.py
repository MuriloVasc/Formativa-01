from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)

from selenium.webdriver.common.by import By


navegador.get("file:///Z:/TI/DESENVOLVIMENTO%20DE%20SISTEMAS/IDSI/ALUNOS/Murilo%20e%20Otavio/site/Home.html")

navegador.implicitly_wait(3)


dados0 = navegador.find_element(By.CLASS_NAME, "produto")
dados1 = navegador.find_elements(By.TAG_NAME, "slide")
dados2 = navegador.find_elements(By.CSS_SELECTOR, "div.slides")
dados3 = navegador.find_elements(By.ID,"produtos")
dados4 = navegador.find_elements(By.XPATH, "/html/body/section[4]")
dados5 = navegador.find_elements(By.LINK_TEXT, "Tabela de Preços")[0].text
dados6 = navegador.find_elements(By.NAME, "slide")[0].tag_name

print(dados0.get_attribute("outerHTML"))
print(dados1)
print(dados2)
print(dados3)
print(dados4)
print(dados5)
print(dados6)

