from bs4 import BeautifulSoup
import requests as req


def pars(url):
    html = req.get(url)
    soup = BeautifulSoup(html.text, 'lxml')
    prise = soup.find('div', class_='Product_Price__container__1uqb8 product-price').find('span').text
    img = soup.find("img", class_='ali-kit_Image__image__1jaqdj Product_Gallery__img__9bm18')

    print(prise)
    print(img['src'])
    return img['src'], prise


