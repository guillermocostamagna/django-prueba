import datetime

def año_actual(request):
    return {'año': datetime.datetime.now().year}