from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockForm
from djangocontrib import messages



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


def add_stock(request):
    if request.method == 'POST':
        form = StockForm(request.POST or None)

    if form.is_valid():
        form.save()
        message.success(request, ("Stock Has Been Added!"))
        return redirect('add_stock')

    else:

        ticker = Stock.objects.all()
        return render(request, 'add_stock.html', {'ticker': ticker})
