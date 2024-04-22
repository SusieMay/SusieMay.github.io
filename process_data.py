from django.shortcuts import render

def process_data(request):
    # Pobierz wybrane opcje z formularza
    selected_options = request.GET.getlist('selected_options')

    # Wyświetl wybrane opcje
    context = {
        'selected_options': selected_options,
    }
    return render(request, 'process_data.html', context)
