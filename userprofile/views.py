import json
from django.shortcuts import responsse
from django.http import HttpResponse
from djando.import
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
nwe_user = user.objects.create_user(
    username = data['Usernme],' \
  password = data ['password],
    email = data['email]
)
    #3. cria o userprofie vinculando ao user criado acima
    new_user_profile = userprofile.object.create(
        user = new_user ,
        birthdate = data['birthdate']

    )

    return jsonResponse(
        {
            'status': 'Sucesso',
            'message': 'usuario criado!',
        }, status=201
    )
    return jsonResponse(
        { 'erro': 'metodo não permitido' 
         status=405
    )