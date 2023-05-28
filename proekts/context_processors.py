import requests
from .models import Balance


def nav(request):
    context = {}
    if request.user.is_authenticated:
        response = requests.get('https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5').json()

        # Check if the response is not empty and contains the necessary data
        if response and len(response) >= 2:
            usd_buy = float(response[1].get('buy', 0))
            usd_sell = float(response[1].get('sale', 0))
            eur_buy = float(response[0].get('buy', 0))
            eur_sell = float(response[0].get('sale', 0))

            user_balance = Balance.objects.get(user=request.user)

            context = {
                'usd_buy': usd_buy,
                'usd_sell': usd_sell,
                'eur_buy': eur_buy,
                'eur_sell': eur_sell,
                'user_balance': user_balance,
            }
    return context
