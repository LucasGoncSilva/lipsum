from django.shortcuts import render


# Create your views here.
def handle403(request: object, *args, **kwargs) -> object:
    return render(request, 'err/error_template.html', {
        'code': 403,
        'message1': 'Você não tem autorização para proseguir.',
        'message2': 'Retorne para onde estava ou vá para a homepage.',
    })


def handle404(request: object, *args, **kwargs) -> object:
    return render(request, 'err/error_template.html', {
        'code': 404,
        'message1': 'O endereço requisitado não foi encontrado.',
        'message2': 'Retorne para onde estava ou vá para a homepage.',
    })


def handle500(request: object, *args, **kwargs) -> object:
    return render(request, 'err/error_template.html', {
        'code': 500,
        'message1': 'Ocorreu um problema com o servidor.',
        'message2': 'Informe o problema para a equipe do site.',
    })
