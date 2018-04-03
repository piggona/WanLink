from django.shortcuts import render
from .models import *
import sys


# Create your views here.

def getProfile(request):
    if request.method == "POST":  # 前端下面的用户表单提交了
        item = request.POST.get("")
        return render(request, "gotoform.html", {'it': item})
    elif request.method == "GET":
        banner_title = Banner.objects.all()
        service = Service.objects.all()
        service_image = ServiceImage.objects.all()
        product = Product.objects.all()
        product_image = ProductImage.objects.all()
        document = Document.objects.all()

        return render(request, "frontPage.html", {'Banner_title': banner_title, 'Service': service,
                                                  'Service_image': service_image, 'Product_Image': product_image,
                                                  'Document': document})


def open(request):
    return render(request, "gotoform.html", {})
