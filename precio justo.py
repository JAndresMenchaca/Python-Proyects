import random
from PIL import Image
from io import BytesIO
from speak_listen import listen, speak
from requests_html import HTMLSession


def main():
    # speak("Bienvenido al precio justo, vamos a intentar adivinar el precio de algunos productos")
    session = HTMLSession()
    main = session.get("https://www.lavineteca.com/")

    categories = main.html.find(".mo_ma_level_1")
    category = random.choice(categories)
    print(category.attrs["title"])

    product_page = session.get(category.attrs["href"])
    products =product_page.html.find(".product_img_link")
    product = random.choice(products)

    product_name = product.attrs["title"]  # Nombre del producto
    print(product_name)

    img_src = product.find(".front-image  ", first=True).attrs['src']
    img_download = session.get(img_src, verify=False)
    image = Image.open(BytesIO(img_download.content))
    image.show()


if __name__ == "__main__":
    main()