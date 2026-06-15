import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from .models import UserProfile

# create your views here.
def home_view( request ):
    return render(request, 'home.html')

def userprofile_view(request):
    return HttpResponse("<h1>User profile</h1")

@csrf_exempt
def register(request):
    if request.method == 'POST':
        # 1. transforma o JSON do bruno em um adicionario python
        data = json.loads(request.body)

        #2. cria o user padrão do Django (criptografando a senha)
        new_user = User.objects.create_user(
            username = data['Username'],
            password = data ['password'],
            email = data['email']
        )

        #3. cria o userprofie vinculando ao user criado acima
        new_user_profile = UserProfile.object.create(
            user = new_user,
            birthdate = data['birthdate']

        )

        return JsonResponse(
            {
                'status': 'Sucesso',
                'message': 'usuario criado!',
            }, status=201
        )

    return JsonResponse(
        {
            'erro': 'metodo não permitido'
        }, status=405
    )