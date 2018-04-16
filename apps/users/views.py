from django.http import HttpResponse

from django.shortcuts import render
from .models import *
import sys


# Create your views here.

def getProfile(request):
    if request.method == "POST":  # 前端下面的用户表单提交了
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        text = request.POST['text']

        dt = datetime.now()
        html = "反馈成功提交,过去时间：%s" % (str(dt))
        response = HttpResponse(html)
        response.set_cookie("user_name", name, expires=dt)

        obj = FeedBack.objects.create(FeedBackId=phone, FeedBackHost=name, FeedBackText=text)
        obj.save()
        return response

    elif request.method == "GET":
        banner_title = Banner.objects.all()
        service = Service.objects.all()
        service_image = ServiceImage.objects.all()
        product = Product.objects.all()
        product_image = ProductImage.objects.all()
        document = Document.objects.all()
        support = Support.objects.all()
        feed_back = FeedBack.objects.all()
        company = Firm.objects.all()

        if "user_name" in request.COOKIES:
            user_name = request.COOKIES['user_name']
            return render(request, "frontPage.html", {'Banner_title': banner_title, 'Service': service,
                                                      'Service_image': service_image, 'Product_Image': product_image,
                                                      'Document': document, 'Support': support, 'User_name': user_name,
                                                      'Feed_back': feed_back, 'Company': company})
        return render(request, "frontPage.html", {'Banner_title': banner_title, 'Service': service,
                                                  'Service_image': service_image, 'Product_Image': product_image,
                                                  'Document': document, 'Support': support, 'Feed_back': feed_back,
                                                  'Company': company})


def open(request):
    return render(request, "gotoform.html", {})
