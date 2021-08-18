from django.shortcuts import render


def home(request):
    import requests
    import json 

    # pk_d8c04f5d4e1c4b39b7fcc939f540a081
    api_request = requests.get(
        "https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_d8c04f5d4e1c4b39b7fcc939f540a081")

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error..."

    return render(request, 'home.html', {'api': api})

def about(request):
    return render(request, 'about.html', {})
