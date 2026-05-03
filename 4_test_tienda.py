import pytest
from selenium import webdriver
from login_page import LoginPage  # Usando el modelo POM que creamos antes
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    """Configuración inicial del navegador (Fixture)"""
    options = Options()
    options.add_argument("--headless") # Ejecución sin ventana 
    options.add_argument("--no-sandbox") 
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)    
    yield driver
    driver.quit()

def test_login_fallido(driver):
    """Prueba de usuario bloqueado"""
    driver.get("https://saucedemo.com")
    login = LoginPage(driver)
    login.ingresar_credenciales("locked_out_user", "secret_sauce")
    login.click_login()
    assert "locked out" in login.obtener_error()

def test_login_exitoso(driver):
    """Prueba de login correcto"""
    driver.get("https://saucedemo.com")
    login = LoginPage(driver)
    login.ingresar_credenciales("standard_user", "secret_sauce")
    login.click_login()
    assert "inventory.html" in driver.current_url