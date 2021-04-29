import requests
from bs4 import BeautifulSoup


def list_company(companys):
    companys_information = []
    for company in companys:
        companys_information.append(get_company_information(company))
    return companys_information


def get_company_information(company_code):
    URL = f"https://finance.naver.com/item/main.nhn?code={company_code}"
    results = requests.get(URL)
    soup = BeautifulSoup(results.text, "html.parser")
    company_names = soup.find(
        "div", {"class": "wrap_company"}).find("a").string
    stock_price = soup.find("em", {"class": "no_down"}).find(
        "span", {"class": "blind"}).string
    return {
        'company': company_names,
        'stock_price': stock_price
    }

