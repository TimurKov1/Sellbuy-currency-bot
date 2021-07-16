class Information:
    def __init__(self, currency, bank_site):
        self.banks = currency[::5]
        del currency[::5]

        self.buy_usd = currency[::4]
        self.sell_usd = currency[1::4]

        self.buy_eur = currency[2::4]
        self.sell_eur = currency[3::4]

        self.best_buy_usd = max(self.buy_usd)
        self.best_sell_usd = min(self.sell_usd)
        self.a = self.buy_usd.index(self.best_buy_usd)

        self.best_buy_eur = max(self.buy_eur)
        self.best_sell_eur = min(self.sell_eur)

        self.usd_buy = self.buy_usd.index(self.best_buy_usd)
        self.usd_sell = self.sell_usd.index(self.best_sell_usd)
        self.eur_buy = self.buy_eur.index(self.best_buy_eur)
        self.eur_sell = self.sell_eur.index(self.best_sell_eur)

        self.valute = bank_site
        self.valute_names = self.valute[1::3]
        self.valute_number = self.valute[::3]
        self.valute_price = self.valute[2::3]
        self.valute_country = ['🇦🇺', '🇦🇿', '🇦🇲', '🇧🇾', '🇧🇬', '🇧🇷', '🇭🇺', '🇰🇷', '🇭🇰', '🇩🇰', '🇺🇸', '🇪🇺', '🇮🇳', '🇰🇿', '🇨🇦', '🇰🇬', '🇨🇳', '🇲🇩', '🇹🇲', '🇳🇴', '🇵🇱', '🇷🇴', '🌍', '🇸🇬', '🇹🇯', '🇹🇷', '🇺🇿', '🇺🇦', '🇬🇧', '🇨🇿', '🇸🇪', '🇨🇭', '🇿🇦', '🇯🇵']

    def print_currency(self):
        message = ''
        i = 0
        while i < len(self.buy_usd):
            message += f'\n{self.banks[i]}\nПокупка 🇺🇸 USD: {self.buy_usd[i]}\nПродажа 🇺🇸 USD: {self.sell_usd[i]}\nПокупка 🇪🇺 EUR: {self.buy_eur[i]}\nПродажа 🇪🇺 EUR: {self.sell_eur[i]}\n'
            i += 1

        return message

    def best_course(self):
        message = ''
        message += f'\n\nЛучший курс покупки 🇺🇸 USD:\n{self.banks[self.usd_buy]}: {self.best_buy_usd}\nЛучший курс продажи 🇺🇸 USD:\n{self.banks[self.usd_sell]}: {self.best_sell_usd}\n\nЛучший курс покупки 🇪🇺 EUR:\n{self.banks[self.eur_buy]} {self.best_buy_eur}\nЛучший курс продажи 🇪🇺 EUR:\n{self.banks[self.eur_sell]} {self.best_sell_eur}'

        return message

    def print_usd_eur(self, buy, sell, text):
        message = ''
        i = 0
        while i != len(self.banks):
            message += f'\n\n{self.banks[i]}\n{text}: {buy[i]} / {sell[i]}'
            i += 1

        return message

    def print_best_currency(self, buy, best_buy, sell, best_sell, text):
        message = ''
        message += f'\n\nЛучший курс покупки {text}:\n{self.banks[buy]}: {best_buy}\nЛучший курс продажи {text}:\n{self.banks[sell]}: {best_sell}'

        return message

    def print_CB(self):
        message = ''
        i = 0
        message += 'Курс валют ЦБ\n'
        while i != 34:
            message += f'{self.valute_country[i]} {self.valute_number[i]} {self.valute_names[i]}: {self.valute_price[i]}\n'
            i += 1

        return message

    def print_bank(self, bank):
        if bank in self.banks:
            self.number_banks = self.banks.index(bank)
            message = ''
            message += f'\n{bank}\n🇺🇸 USD: {self.buy_usd[self.number_banks]} / {self.sell_usd[self.number_banks]}\n🇪🇺 EUR: {self.buy_eur[self.number_banks]} / {self.sell_eur[self.number_banks]}'

            return message

        else:
            print('Такого банка нет')