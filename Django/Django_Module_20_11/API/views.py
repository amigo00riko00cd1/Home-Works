from django.http import JsonResponse
from .models import*
import random
import sys
def prediction(request):

    count_moment = Moment.objects.count()
    count_prediction = Prediction.objects.count()

    ran_moment = random.randint(0, count_moment - 1)
    ran_prediction = random.randint(0, count_prediction - 1)

    moment = Moment.objects.all()[ran_moment]
    prediction = Prediction.objects.all()[ran_prediction]

    full = FullPrediction.objects.create(moment=moment.content, prediction=prediction.content)
    full.save()

    return JsonResponse({"prediction" : f"{full.moment} {full.prediction}"})


def random_number(request):
    start = int(request.GET.get("start", -sys.maxsize - 1))
    end = int(request.GET.get("end", sys.maxsize))
    size_kit = int(request.GET.get("kit", 1))
    numbers = []
    for r in range(0, size_kit):
        numbers.append(random.randint(start, end))

    if len(numbers) > 1:
        return JsonResponse({"numbers" : numbers})
    
    return JsonResponse({"number" : numbers[0]})
