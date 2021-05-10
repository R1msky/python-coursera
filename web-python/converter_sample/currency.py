from bs4 import BeautifulSoup
from decimal import Decimal
import requests


def convert(amount, cur_from, cur_to, date, requests):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp', {'date_req': date})
    soup = BeautifulSoup(response.content, 'xml')
    if cur_from == 'RUR':
        val_from = (Decimal(1), 1)
    else:
        val_from = (Decimal(soup.find('CharCode', text=cur_from).find_next_sibling('Nominal').string),
                    Decimal(soup.find('CharCode', text=cur_from).find_next_sibling('Value').string.replace(',', '.')))

    val_to = (Decimal(soup.find('CharCode', text=cur_to).find_next_sibling('Nominal').string),
              Decimal(soup.find('CharCode', text=cur_to).find_next_sibling('Value').string.replace(',', '.')))

    result = (amount * val_from[1]) / val_from[0] / (val_to[1] / val_to[0])

    return result.quantize(Decimal('.0001'))  # не забыть про округление до 4х знаков после запятой


if __name__ == '__main__':
    convert(Decimal('1000.1000'), 'RUR', 'JPY', '17/02/2005', requests)