from django.shortcuts import render
from clothing.models import Product
# Create your views here.
def clothing(request):
    pro_image = Product.objects.all()
    return render(request, 'clothing/fashion.html', {'pro_img':pro_image})