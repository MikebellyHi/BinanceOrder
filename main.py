import requests
from config import API_KEY, API_SECRET
from random import randint
import time
import hmac
import urllib
import hashlib


class OrderBinance:
    def __init__(self, volume, number, amountDif, side, priceMin, priceMax, pair):
        self.API_KEY = API_KEY
        self.API_SECRET = API_SECRET
        self.volume = volume
        self.number = number
        self.amountDif = amountDif
        self.side = side
        self.priceMin = priceMin
        self.priceMax = priceMax
        self.prices = [randint(self.priceMin, self.priceMax) for _ in range(self.number)]
        volumes = [randint((volume / number) - amountDif, volume / number) if i % 2 == 0 else randint(volume / number, (volume / number) + amountDif) for i in range(number - 1)]
        volumes.append(volume - sum(volumes))
        self.volumes = volumes
        self.pair = pair.upper()
        self.headers = {'X-MBX-APIKEY': self.API_KEY}

    def create_orders(self):
        for i in range(len(self.prices)):

            # quantity - количество покупаемой криптовалюты, его мы высчитываем исходя из объема нашей quote/base криптовалюты и цены покупки
            quantity = self.volumes[i] / self.prices[i]

            order = {
                "symbol": self.pair,
                "side": "SELL",
                "type": "LIMIT",
                "timeInForce": "GTC",
                "quantity": round(quantity, 2),
                "price": self.prices[i],
                "timestamp": str(time.time_ns() // 1000000),
                "recvWindow": 15000
            }

            # Кодируем наш запрос ниже

            order['signature'] = hmac.new(bytes(self.API_SECRET, 'utf-8'), msg=bytes(urllib.parse.urlencode(order), 'utf-8'),
                                          digestmod=hashlib.sha256).hexdigest().upper()

            response = requests.post('https://api.binance.com/api/v3/order/test', params=order, headers=self.headers)
            if response.status_code == 200:
                # Binance-API возвращает пустой словарик при удачном размещении тестового ордера, мы проверяем этот словарь на "пустоту" т.к. status_code может быть "200" и при возникновении ошибок
                if len(response.json()) == 0:
                    print(response.json(), 'Ордер успешно размещен', sep='\n')
            else:
                print('Не удалось разместить ордер', response.json(), sep='\n')


if __name__ == '__main__':
    input_data = {
        "volume": 10000.0,  # Объем в долларах
        "number": 5,  # На сколько ордеров нужно разбить этот объем
        "amountDif": 50.0,
        # Разброс в долларах, в пределах которого случайным образом выбирается объем в верхнюю и нижнюю сторону
        "side": "SELL",  # Сторона торговли (SELL или BUY)
        "priceMin": 200.0,  # Нижний диапазон цены, в пределах которого нужно случайным образом выбрать цену
        "priceMax": 300.0  # Верхний диапазон цены, в пределах которого нужно случайным образом выбрать цену
    }
    volume = float(input_data['volume'])
    number = int(input_data['number'])
    amountDif = float(input_data['amountDif'])
    side = input_data['side']
    priceMin = float(input_data['priceMin'])
    priceMax = float(input_data['priceMax'])
    pair = 'bnbusdt'
    obj = OrderBinance(volume, number, amountDif, side, priceMin, priceMax, pair)
    obj.create_orders()