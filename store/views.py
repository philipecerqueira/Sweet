import sys
from datetime import date
from io import BytesIO

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import HttpResponse
from django.shortcuts import render
from PIL import Image as Img
from PIL import ImageDraw

from .models import Category, Image, Product


def addProducts(request):
    if request.method == 'GET':
        categorys = Category.objects.all()
        return render(request, 'addProducts.html', {'categorys': categorys})
    elif request.method == 'POST':
        name = request.POST.get('name')
        category_id = request.POST.get('category_id')
        quantity = request.POST.get('quantity')
        priceSell = request.POST.get('priceSell')
        priceBuy = request.POST.get('priceBuy')

        product = Product(name=name,
            category_id=category_id,
            quantity=quantity,
            priceSell=priceSell,
            priceBuy=priceBuy,
        )
        product.save()

        for file in request.FILES.getlist('images'):
            imgName = f'{date.today()} - {product.id}.jpg'

            openImage = Img.open(file)
            openImage = openImage.convert('RGB')
            openImage = openImage.resize((300,300))
            draw = ImageDraw.Draw(openImage)
            draw.text((20, 280), "Sweet", (255,255,255))
            output = BytesIO()
            openImage.save(output, format='JPEG', quality=100)
            output.seek(0)
            finalImg = InMemoryUploadedFile(output,
                'ImageField',
                imgName,
                'image/JPEG',
                sys.getsizeof(output),
                None
            )

            img = Image(image = finalImg, product=product)
            img.save()

        return HttpResponse('Foi')