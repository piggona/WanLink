from datetime import *
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Admin(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name="昵称", default="name")
    birthday = models.DateField(verbose_name="生日", null=True, blank=True)
    gender = models.CharField(max_length=20, choices=(("male", "男"), ("female", "女")), default="男", verbose_name="性别")
    address = models.CharField(max_length=100, default="")
    mobile = models.CharField(max_length=11, null=True, blank=True)
    Image = models.ImageField(upload_to="image/%Y/%m", default=u"image/default.jpg", verbose_name="图片")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name="验证码")
    email = models.EmailField(max_length=50, verbose_name="邮箱")
    send_type = models.CharField(choices=(("register", "注册"), ("forget", "忘记密码")), max_length=20, verbose_name="传输类型")
    send_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}({1})'.format(self.email, self.code)


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name="标题")
    image = models.ImageField(upload_to="banner/%Y/%m", verbose_name="轮播图", max_length=100)
    url = models.URLField(max_length=200, verbose_name="访问地址")
    index = models.IntegerField(default=100, verbose_name="顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Firm(models.Model):
    FirmId = models.CharField(max_length=20, primary_key=True, verbose_name="公司ID")
    FirmName = models.CharField(max_length=20, verbose_name="公司名称")
    FirmIntro = models.TextField(null=True, blank=True, verbose_name="公司介绍")
    FirmAddr = models.CharField(max_length=50, null=True, verbose_name="公司地址")
    FirmTel = models.CharField(max_length=50, null=True, verbose_name="公司电话")
    FirmEmail = models.EmailField(verbose_name="公司邮箱")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "公司"
        verbose_name_plural = "公司"

    def __str__(self):
        return self.FirmName


class Product(models.Model):
    ProductTypeId = models.CharField(max_length=20, primary_key=True, verbose_name="产品ID")
    ProductTypeName = models.CharField(max_length=20, verbose_name="产品名")
    ProductTypeIntro = models.TextField(null=True, blank=True, verbose_name="产品介绍")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "产品"
        verbose_name_plural = "产品"

    def __str__(self):
        return self.ProductTypeName


def image_directory_path(instance, filename):
    return 'image/image_{0}/{1}'.format(instance.product.ProductTypeName, filename)


class ProductImage(models.Model):
    """""
    产品图片
    """
    product = models.ForeignKey(Product, models.CASCADE)
    image = models.ImageField(upload_to=image_directory_path, verbose_name="产品图片")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "产品图"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.product.ProductTypeName


class Project(models.Model):
    ProjectId = models.CharField(max_length=30, verbose_name="项目ID")
    ProjectName = models.CharField(max_length=20, verbose_name="项目名")
    ProjectIntro = models.TextField(verbose_name="项目介绍", null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "项目"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.ProjectName


def image_directory_path_project(instance, filename):
    return 'image/image_{0}/{1}'.format(instance.project.ProjectName, filename)


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, models.CASCADE)
    image = models.ImageField(upload_to=image_directory_path_project, verbose_name="项目图片")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "项目图"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.project.ProjectName


class Service(models.Model):
    ServiceId = models.CharField(max_length=30, verbose_name="服务Id")
    ServiceName = models.CharField(max_length=20, verbose_name="服务名")
    ServiceIntro = models.TextField(max_length=1000, null=True, blank=True, verbose_name=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "服务"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.ServiceName


def image_directory_path_service(instance, filename):
    return 'image/image_{0}/{1}'.format(instance.service.ServiceName, filename)


class ServiceImage(models.Model):
    service = models.ForeignKey(Service, models.CASCADE)
    image = models.ImageField(upload_to=image_directory_path_service, verbose_name="服务图片")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "服务图"
        verbose_name_plural = verbose_name


def user_directory_path_doc(instance, filename):
    return 'doc/user_{0}/{1}'.format(instance.DocumentName, filename)
    # 其中instance表示使用FileField的那个类的一个实例
    # filename即就是文件上传时的名


def image_directory_path_doc(instance, filename):
    return 'image/image_{0}/{1}'.format(instance.DocumentName, filename)


class Document(models.Model):
    DocumentId = models.CharField(max_length=30, verbose_name="文件ID")
    DocumentName = models.CharField(max_length=20, verbose_name="文档名")
    Document = models.FileField(verbose_name='文件', upload_to=user_directory_path_doc)
    DocumentImage = models.ImageField(upload_to=image_directory_path_doc, default=0, verbose_name="文件图")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "文档"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.DocumentName


def user_directory_path_feedback(instance, filename):
    return 'doc/name_{0}/{1}'.format(instance.AdminDocName, filename)


class FeedBack(models.Model):
    FeedBackId = models.CharField(max_length=30, verbose_name="反馈ID")
    FeedBackHost = models.CharField(max_length=50, verbose_name='反馈来源')
    FeedBackText = models.TextField(verbose_name="反馈文本")
    AdminText = models.TextField(verbose_name="管理员回复文本")
    AdminDocName = models.CharField(max_length=20, verbose_name="文件名", null=True, blank=True)
    AdminDoc = models.FileField(verbose_name="管理员回复文件", null=True, blank=True, upload_to=user_directory_path_feedback)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "反馈"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.FeedBackId


def user_directory_path_message(instance, filename):
    return 'doc/Id_{0}/{1}'.format(instance.messageId, filename)


class UserMessage(models.Model):
    messageId = models.IntegerField(default=0, verbose_name="消息Id")
    user = models.IntegerField(default=0, verbose_name="接收用户")
    message = models.CharField(max_length=200, verbose_name="消息内容")
    ms_file = models.FileField(upload_to=user_directory_path_message, default=0, verbose_name="消息文件")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户消息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.messageId
