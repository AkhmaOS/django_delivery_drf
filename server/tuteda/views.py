from django.http import HttpResponse, HttpResponseGone
from django.views.generic import RedirectView, TemplateView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView


class HomeView(TemplateView):
    """Рендерит главную страницу"""
    template_name = 'home.html'


class APIRootView(APIView):
    def get(self, request):
        data = {
            'settings': reverse('settings-app', request=request),
            'categories': reverse('category', request=request),
            'products': reverse('products', kwargs={'category_id': '1'}, request=request),
            'product': reverse('product', kwargs={'category_id': '1', 'product_id': '1'}, request=request),
        }
        return Response(data)
