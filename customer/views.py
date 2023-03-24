from django.shortcuts import render
from django.http.response import JsonResponse

def get_list(request):
    customers = [
        {
            'firstname': 'John',
            'lastname': 'Constantine'
        },
        {
            'firstname': 'Bruce',
            'lastname': 'Wayne'
        },
        {
            'firstname': 'Clark',
            'lastname': 'Kent'
        },
        {
            'firstname': 'JP',
            'lastname': 'Fortuno'
        },
    ]
    return JsonResponse(data=customers, safe=False)

def customer_list(request):
    context = {}
    return render(request, 'customer/index.html',context)
