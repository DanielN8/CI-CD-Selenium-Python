from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options

# Configuración inicial
options = Options()
options.add_argument("--headless") # Ejecución sin ventana 
options.add_argument("--no-sandbox") 
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(options=options)    
driver.implicitly_wait(10)

def ejecutar_pruebas():
    try:
        # --- CASO 1: Login Exitoso ---
        print("Ejecutando Caso 1: Login...")
        driver.get("https://saucedemo.com")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        assert "inventory.html" in driver.current_url
        print("✅ Caso 1 completado con éxito.")

        # --- CASO 2: Agregar al Carrito ---
        print("Ejecutando Caso 2: Agregar producto...")
        boton_agregar = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        boton_agregar.click()

        badge_carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        assert badge_carrito == "1"
        print("✅ Caso 2 completado con éxito.")

        # --- CASO 3: Login Fallido (Usuario Bloqueado) ---
        print("Ejecutando Caso 3: Login fallido...")
        driver.delete_all_cookies()  # Limpiar sesión
        driver.get("https://saucedemo.com")
        driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # El mensaje de error usa el atributo data-test="error"
        error_msg = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
        assert "Sorry, this user has been locked out" in error_msg
        print("✅ Caso 3 completado con éxito.")

    except Exception as e:
        print(f"❌ Error durante la ejecución: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    ejecutar_pruebas()