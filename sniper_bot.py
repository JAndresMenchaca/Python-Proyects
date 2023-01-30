from time import sleep
from requests_html import HTMLSession
from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    url = "https://www.lavineteca.com/comic-book/8033-batman-una-muerte-en-la-familia-esenciales-dc.html"

    if request(url):
        navegador(url)


def request(url):
    sesion = HTMLSession()
    while True:
        r = sesion.get(url)
        buy_zone = r.html.find(".product-available")
        buy_zone1 = r.html.find(".product-last-items") #esta es una segunda variable ya que la pagina contiene dos posibles respuestas
        if len(buy_zone) > 0 or len(buy_zone1) > 0:
            print("Hay Stock")
            return True
        else:
            print("El producto no esta disponible")
            sleep(5)


def navegador(url):
    # driver.find_element(By.CLASS_NAME, 'clase').click()
    # driver.find_element(By.ID, 'id').click()
    driver = webdriver.Chrome()
    driver.get(url)
    sleep(5)
    driver.find_element(By.CLASS_NAME, "add_buy_now").click()
    sleep(10)
    elem = driver.find_element(By.CLASS_NAME, 'form-control')
    elem.send_keys("Batman")
    driver.find_element(By.CLASS_NAME, "btn-search").click()
    sleep(30)


if __name__ == "__main__":
    main()