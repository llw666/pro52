from django.shortcuts import render

# Create your views here.
def register(request):
    name = request.POST.get('name')
    age = request.POST.get('age')

    user = Users()
    user.name = name
    user.age = age
    user.save()
    data = {msg:"ok",status:200}
    return JsonResponse(data=data)
