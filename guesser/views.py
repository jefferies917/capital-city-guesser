from django.shortcuts import render
import requests
import random


def index(request):
    """
    View to check a users capital city guess against countriesnow RESTful API

    returns a render for either a correct or incorrect message to the user
    """
    # Collect country names for randomiser
    response = requests.get('https://countriesnow.space/api/v0.1/countries/capital').json()
    country_list = []
    country_objects = response.get('data', [])

    if request.method == 'GET':
        for country in country_objects:
            country_list.append(country.get('name', ''))
    
        # Pick random country and save in session
        random_country = random.choice(country_list)
        request.session['country'] = random_country
        return render(request, 'index.html', {'data': country_list, 'country': random_country})

    if request.method == 'POST':
        random_country = request.session['country']  # Retrieve country from session
        users_answer = request.POST.get('answer')  # Get users inputted answer

        for country in country_objects:
            if country.get('name', '') == random_country:
                correct_answer = country.get('capital', '')  # Get correct answer
                if correct_answer == users_answer.capitalize():
                    return render(request, 'correct.html', {'country': random_country, 'capital': correct_answer})
        
        return render(request, 'incorrect.html', {'country': random_country, 'capital': users_answer, 'correct_answer': correct_answer})
