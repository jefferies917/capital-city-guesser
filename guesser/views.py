from django.shortcuts import render
import requests
import random


def index(request):
    # Collect country names for randomiser
    response = requests.get('https://countriesnow.space/api/v0.1/countries/capital').json()
    countries_list = []
    countries_obj = response.get('data', [])

    if request.method == 'GET':
        for country in countries_obj:
            countries_list.append(country.get('name', ''))
    
        # Pick random country and save in session
        chosen_country = random.choice(countries_list)
        request.session['country'] = chosen_country
        return render(request, 'index.html', {'data': countries_list, 'country': chosen_country})

    if request.method == 'POST':
        # Retrieve country from session
        chosen_country = request.session['country']

        answer = request.POST.get('answer')

        guess_correct = False
        for country in countries_obj:
            if country.get('name') == chosen_country:
                correct_answer = country.get('capital')
                if country.get('capital') == answer:
                    guess_correct = True
        
        if guess_correct == True:
            return render(request, 'correct.html', {'country': chosen_country, 'capital': answer})
        else:
            return render(request, 'incorrect.html', {'country': chosen_country, 'capital': answer, 'correct_answer': correct_answer})
