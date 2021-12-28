from cart.services import Cart
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST


def cart_detail(request):
    return render(request, 'cart/detail.html', {'cart': Cart(request)})


@require_POST
def cart_add(request):
    Cart(request).add(request.POST.get('product'))
    return JsonResponse({'success': True})


@require_POST
def cart_delete(request):
    Cart(request).delete(request.POST.get('product'))
    return JsonResponse({'success': True})
