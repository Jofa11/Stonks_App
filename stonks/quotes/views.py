from django.shortcuts import render


def home(request):
    import requests
    import json

    if request.method == 'POST':
        ticker = request.POST['ticker']

        api_request = requests.get(
            "https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_d8c04f5d4e1c4b39b7fcc939f540a081")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."
        return render(request, 'home.html', {'api': api})

    else:
        return render(request, 'home.html', {'ticker': "Enter a Ticker Symbol Above..."})


def about(request):
    return render(request, 'about.html', {})
