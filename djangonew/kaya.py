from django.http import HttpResponse;
import datetime;

def test(request):
    tina = datetime.datetime.now()
    print('test function is called')
    return HttpResponse('<h1>Display test content with time</h1>'+ str(tina))
