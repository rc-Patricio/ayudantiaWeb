from django.http import HttpResponse


def vista1(request):
    return HttpResponse("""
        <h1>Página 1</h1>
        <a href='/vista2/'>Ir a Vista 2</a><br>
        <a href='/vista3/'>Ir a Vista 3</a>
    """)

def vista2(request):
    return HttpResponse("""
        <h1>Página 2</h1>
        <a href='/vista1/'>Ir a Vista 1</a><br>
        <a href='/vista3/'>Ir a Vista 3</a>
    """)

def vista3(request):
    return HttpResponse("""
        <h1>Página 3</h1>
        <a href='/vista1/'>Ir a Vista 1</a><br>
        <a href='/vista2/'>Ir a Vista 2</a>
    """)