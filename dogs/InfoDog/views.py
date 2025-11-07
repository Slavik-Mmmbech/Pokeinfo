from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    '''Функция для создания главной страницы'''
    return render(request, 'index.html')

def get_breeds(request):
    response = requests.get('https://dog.ceo/api/breeds/list/all')

    if response.status_code == 200:
        data = response.json()
        breeds_list = list(data['message'].keys())
        
        context = {'breeds_list': breeds_list}
    else:
        context = 'Произошла ошибка, попробуйте позже.'

    return render(request, 'breeds_list.html', context)

def get_dog_images(request):
    if request.method == 'POST':
        dog_images = []
        selected_breeds = []
        
        breeds_input = request.POST.get('breeds', '')
        selected_breeds = [breed.strip() for breed in breeds_input.split(',') if breed.strip()]
        
        for breed in selected_breeds:
            api_url = f'https://dog.ceo/api/breed/{breed}/images/random'
            response = requests.get(api_url)
            
            if response.status_code == 200:
                data = response.json()
                dog_images.append(data['message'])
            else:
                dog_images.append(None)

        breeds_with_images = zip(selected_breeds, dog_images)
        context = {'breeds_with_images': breeds_with_images}
        
    else:
        context = {'breeds_with_images': None}
    
    return render(request, 'dog_images.html', context)