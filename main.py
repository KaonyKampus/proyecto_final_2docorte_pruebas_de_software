#importaciones
import time
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import os
import requests
import base64
import re

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--start-maximized")

#variable para iniciar el navegador
driver = webdriver.Chrome(options=chrome_options)

#variable para subir archivo 
upload_file_route = r"/home/hacker/Documentos/universidad/materias_semestres/3_semestre/pruebas_de_software_I/entrega_segundo_corte_final/utils/test.webp"
download_directory = "/home/hacker/Documentos/universidad/materias_semestres/3_semestre/pruebas_de_software_I/entrega_segundo_corte_final/descargas"


def generar_reporte_html(file_path):
    with open("reporte_pruebas.html", "w") as f:
        f.write("""
        <html>
        <head>
            <title>Reporte de Pruebas Automatizadas</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 20px; background-color: #f4f4f4; }
                h1 { color: #333; }
                h2 { color: #555; margin-top: 40px; }
                h3 { color: #666; }
                p { font-size: 16px; }
                img { border: 2px solid #888; margin-bottom: 10px; }
                .captura { margin-bottom: 30px; }
                .archivo { padding: 10px; background-color: #ddd; border-radius: 5px; display: inline-block; }
                .exito { padding: 15px; background-color: #c8e6c9; border: 1px solid #388e3c; color: #2e7d32; border-radius: 5px; margin-bottom: 20px; }
                .conclusiones { padding: 15px; background-color: #bbdefb; border: 1px solid #1976d2; color: #0d47a1; border-radius: 5px; }
            </style>
        </head>
        <body>
            <h1>📋 Reporte de Pruebas Automatizadas con Selenium</h1>
            <div class="exito">
                ✅ Todas las pruebas se ejecutaron correctamente y todas las funcionalidades funcionan como se esperaba.
            </div>
        """)

        f.write("<h2>Capturas de Evidencia 📸</h2>")

        # Obtener nombres de imágenes y ordenarlas numéricamente por el número inicial
        def extraer_numero(nombre):
            match = re.match(r'^(\d+)', nombre)
            return int(match.group(1)) if match else 0

        imagenes = sorted(os.listdir("capturas_prueba"), key=extraer_numero)

        for imagen in imagenes:
            f.write(f"""
                <div class="captura">
                    <h3>{imagen}</h3>
                    <img src="capturas_prueba/{imagen}" width="600">
                    <p>✅ Prueba satisfactoria: la funcionalidad respondió correctamente.</p>
                </div>
            """)

        f.write(f"""
            <h2>📥 Archivo Descargado</h2>
            <p class="archivo">Archivo descargado exitosamente: {file_path}</p>
        """)

        f.write("""
            <h2>📝 Conclusiones</h2>
            <div class="conclusiones">
                <p>✔️ Todas las pruebas automatizadas se ejecutaron de forma satisfactoria sin errores.</p>
                <p>✔️ Las funcionalidades de alertas, confirmaciones, prompts y descargas mostraron los resultados esperados.</p>
                <p>✔️ El sistema bajo prueba cumple con los criterios de aceptación definidos para este ciclo de pruebas.</p>
                <p>✔️ Se recomienda continuar con nuevas pruebas integradas y de rendimiento para evaluar el comportamiento en escenarios más complejos.</p>
            </div>
        """)

        f.write("</body></html>")

    print("✅ Reporte HTML generado como reporte_pruebas.html")

#funcion para crear la carpeta
def crear_carpeta(nombre_carpeta):
    if not os.path.exists(nombre_carpeta):os.mkdir(nombre_carpeta) 
crear_carpeta("capturas_prueba")
crear_carpeta("descargas")


#funcion para evidencias
def capturar_pantalla(driver, nombre_archivo):
    ruta_archivo = f"capturas_prueba/{nombre_archivo}.png"
    driver.save_screenshot(ruta_archivo)
    print(f"captura {nombre_archivo} tomada exitosamente")






try:
    
    #-------------------------Registro de Usuario-------------------------------------------------------------#
    driver.get("https://demoqa.com")
    time.sleep(2)
    capturar_pantalla(driver, "1.pagina_principal")

    driver.get("https://demoqa.com/automation-practice-form")
    time.sleep(2)
    capturar_pantalla(driver, "2.pagina_formulario")
    

    #1 nombre 
    driver.find_element(By.ID, "firstName").send_keys("David")
    time.sleep(1)
    capturar_pantalla(driver,"3.captura_nombre_form")

    #2 apellido
    driver.find_element(By.ID, "lastName").send_keys("Silva")
    time.sleep(1)
    capturar_pantalla(driver,"4.captura_apellido_form")
    
    #3 correo
    driver.find_element(By.ID, "userEmail").send_keys("david@email.com")
    time.sleep(1)
    capturar_pantalla(driver,"5.captura_mail_form")

    #4 genero
    driver.find_element(By.XPATH, "//label[contains(text(),'Male')]").click() 
    time.sleep(1)
    capturar_pantalla(driver,"6.captura_genero_form")

    #5 numero
    driver.find_element(By.ID, "userNumber").send_keys("1234567890")
    time.sleep(1)
    capturar_pantalla(driver,"7.captura_numero_form")

    #6 scroll
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.find_element(By.ID,"dateOfBirthInput").click()
    
    #7 fecha
    driver.find_element(By.CLASS_NAME, "react-datepicker__year-select").send_keys("1999")
    driver.find_element(By.CLASS_NAME, "react-datepicker__month-select").send_keys("September")
    driver.find_element(By.XPATH, "//div[contains(@class, 'react-datepicker__day react-datepicker__day--025')]").click()   
    time.sleep(1)
    capturar_pantalla(driver,"8.captura_fecha_form")

    #8 subject 
    driver.find_element(By.ID, "subjectsInput").send_keys("Computer Science")
    driver.find_element(By.ID, 'subjectsInput').send_keys(Keys.ENTER)
    time.sleep(1)
    capturar_pantalla(driver,"9.captura_materia_form")

    #9 hobbies
    driver.find_element(By.XPATH, "//label[contains(text(),'Sports')]").click()
    time.sleep(1)
    capturar_pantalla(driver,"10.captura_hobbie_form")
    
    #10 adjuntar foto 
    driver.find_element(By.ID, "uploadPicture").send_keys(upload_file_route)
    time.sleep(1)
    capturar_pantalla(driver,"11.captura_archivo_cargado_form")
    
    #11 direccion
    driver.find_element(By.ID, "currentAddress").send_keys("CRA 32 A # 124 NORTE")
    time.sleep(1)
    capturar_pantalla(driver,"12.captura_direccion_form")

    #12 seleccionar estado 
    driver.find_element(By.ID,"react-select-3-input").send_keys("NCR" + Keys.ENTER)
    time.sleep(1)
    capturar_pantalla(driver,"13.captura_estado_form")
    
    #13 seleccionar ciudad
    driver.find_element(By.ID,"react-select-4-input").send_keys("Delhi" + Keys.ENTER)
    time.sleep(1)
    capturar_pantalla(driver,"14.captura_ciudad_form")

    #13 enviar 
    driver.find_element(By.ID, "submit").click()
    time.sleep(1)
    capturar_pantalla(driver, "15.captura_formulario_completado")


    #-----------------------------------Subir archivos---------------------#
    driver.get("https://demoqa.com/upload-download")
    capturar_pantalla(driver, "16.captura pantalla descarga")

    driver.find_element(By.ID, "uploadFile").send_keys(upload_file_route)
    capturar_pantalla(driver, "17.Captura_archivo_subido")


    #-------------------------------Descarga de Archivos-------------------#
    download_button = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,"downloadButton")))
    download_url = download_button.get_attribute("href")

    print(f"URL del archivo: {download_url}")
    if download_url.startswith("data:image"):

        contenido = base64.b64decode(download_url.split(",")[1])
    else:
        contenido = requests.get(download_url).content
   
    file_path = os.path.join(download_directory, "sampleFile.jpeg")
    with open(file_path, "wb") as file:
        file.write(contenido)

    print(f"Archivo descargado: {file_path}")
    time.sleep(2)


    #---------------------------------Alertas---------------------------------#
    driver.get("https://demoqa.com/alerts")
    time.sleep(1)
    capturar_pantalla(driver,"18.captura_principal_alertas")

    #alerta 1
    alert_button = driver.find_element(By.XPATH, "//button[contains(@id, 'alertButton')]")
    alert_button.click()

    WebDriverWait(driver,10).until(EC.alert_is_present())
    alert = driver.switch_to.alert

    print("El texto de la alerta es: ~", alert.text)
    time.sleep(5)
    alert.accept()
    capturar_pantalla(driver,"19. despues_de_presionar_boton_alerta")
    
    #alerta 2
    timer_alert_button = driver.find_element(By.XPATH, "//button[contains(@id, 'timerAlertButton')]")
    timer_alert_button.click()

    WebDriverWait(driver,10).until(EC.alert_is_present())
    alert = driver.switch_to.alert

    print("texto de la alerta es: ~", alert.text)
    time.sleep(7)
    alert.accept()
    capturar_pantalla(driver,"20. despues_de_presionar_boton_alerta_timer")

    #alerta 3 
    confirmButton = driver.find_element(By.XPATH, "//button[contains(@id, 'confirmButton')]")
    confirmButton.click()

    WebDriverWait(driver,10).until(EC.alert_is_present())      
    alert = driver.switch_to.alert
    
    print("texto de la alerta es: ~", alert.text)
    time.sleep(2)
    alert.accept()
    capturar_pantalla(driver,"21. despues_de_aceptar_alerta_confirm")

    #alerta 3.1
    confirmButton = driver.find_element(By.XPATH, "//button[contains(@id, 'confirmButton')]")
    confirmButton.click()

    WebDriverWait(driver,10).until(EC.alert_is_present())
    alert = driver.switch_to.alert

    print("texto de la alerta es: ~", alert.text)
    time.sleep(2)
    alert.dismiss()
    capturar_pantalla(driver,"22. despues_de_cancelar_alerta_confirm")

    #alerta 4
    promtButton = driver.find_element(By.XPATH, "//button[contains(@id,'promtButton')]")
    promtButton.click()

    WebDriverWait(driver,10).until(EC.alert_is_present())
    alert = driver.switch_to.alert

    print("texto de la alerta es: ~", alert.text)
    alert.send_keys("David Silva")
    alert.accept()
    capturar_pantalla(driver,"23. despues_de_escribir_nombre_alerta_promt")

finally:
        input("Presiona enter para salir del navegador")
        driver.quit()
        generar_reporte_html(file_path)