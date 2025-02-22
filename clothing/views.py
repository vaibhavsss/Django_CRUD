from django.http import JsonResponse
from django.shortcuts import render
from clothing.models import Product
from .forms import ProductForm

def clothing(request):
    pro_image = Product.objects.all()
    form = ProductForm()

    if request.method == "POST" and request.headers.get("X-Requested-With") == "XMLHttpRequest":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            return JsonResponse({
                "success": True,
                "name": product.name,
                "size": product.size,
                "colour": product.colour,
                "price": product.price,
                "image_url": product.image.url
            })
        else:
            return JsonResponse({"success": False, "errors": form.errors})

    return render(request, "clothing/fashion.html", {'pro_img': pro_image, 'form': form})