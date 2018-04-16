# _*_ coding: utf-8 _*_
__author__ = 'Kim'
__date__ = '2018/4/3 上午 9:10'

import xadmin
from .models import *
from xadmin import views


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


xadmin.site.register(views.BaseAdminView, BaseSetting)


class GlobalSettings(object):
    site_title = "万林克技术有限公司"
    site_footer = "万林克技术有限公司"
    menu_style = "accordion"


xadmin.site.register(views.CommAdminView, GlobalSettings)


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']  # 显示的数据项
    search_fields = ['code', 'email', 'send_type']  # 可供搜索的项目
    list_filter = ['code', 'email', 'send_type', 'send_type']  # 过滤器包含的项目（选项）


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)


class BannerAdmin(object):
    list_display = ['title', 'image', 'subtitle', 'url', 'index', 'add_time']  # 显示的数据项
    search_fields = ['title', 'image', 'subtitle', 'url', 'index']  # 可供搜索的项目
    list_filter = ['title', 'image', 'subtitle', 'url', 'index', 'add_time']  # 过滤器包含的项目（选项）


xadmin.site.register(Banner, BannerAdmin)


class FirmAdmin(object):
    list_display = ['FirmId', 'FirmName', 'FirmIntro', 'FirmAddr', 'FirmTel', 'FirmEmail', 'add_time']
    search_field = ['FirmId', 'FirmName', 'FirmIntro', 'FirmAddr', 'FirmTel', 'FirmEmail']
    list_filter = ['FirmId', 'FirmName', 'FirmIntro', 'FirmAddr', 'FirmTel', 'FirmEmail', 'add_time']


xadmin.site.register(Firm, FirmAdmin)


class ProductAdmin(object):
    list_display = ['ProductTypeId', 'ProductTypeName', 'ProductTypeIntro', 'add_time']
    search_field = ['ProductTypeId', 'ProductTypeName', 'ProductTypeIntro']
    list_filter = ['ProductTypeId', 'ProductTypeName', 'ProductTypeIntro', 'add_time']


xadmin.site.register(Product, ProductAdmin)


class ProductImageAdmin(object):
    list_display = ['product', 'image', 'add_time']
    search_field = ['product', 'image']
    list_filter = ['product', 'image', 'add_time']


xadmin.site.register(ProductImage, ProductImageAdmin)


class ProjectAdmin(object):
    list_display = ['ProjectId', 'ProjectName', 'ProjectIntro', 'add_time']
    search_field = ['ProjectId', 'ProjectName', 'ProjectIntro']
    list_filter = ['ProjectId', 'ProjectName', 'ProjectIntro', 'add_time']


xadmin.site.register(Project, ProjectAdmin)


class ProjectImageAdmin(object):
    list_display = ['project', 'image', 'add_time']
    search_field = ['project', 'image']
    list_filter = ['project', 'image', 'add_time']


xadmin.site.register(ProjectImage, ProjectImageAdmin)


class ServiceAdmin(object):
    list_display = ['ServiceId', 'ServiceName', 'ServiceIntro', 'add_time']
    search_field = ['ServiceId', 'ServiceName', 'ServiceIntro']
    list_filter = ['ServiceId', 'ServiceName', 'ServiceIntro', 'add_time']


xadmin.site.register(Service, ServiceAdmin)


class ServiceImageAdmin(object):
    list_display = ['service', 'image', 'add_time']
    search_field = ['service', 'image']
    list_filter = ['service', 'image', 'add_time']


xadmin.site.register(ServiceImage, ServiceImageAdmin)


class DocumentAdmin(object):
    list_display = ['DocumentId', 'DocumentName', 'DocumentIntro', 'Document', 'DocumentImage', 'add_time']
    search_field = ['DocumentId', 'DocumentName', 'DocumentIntro', 'Document', 'DocumentImage']
    list_filter = ['DocumentId', 'DocumentName', 'DocumentIntro', 'Document', 'DocumentImage', 'add_time']


xadmin.site.register(Document, DocumentAdmin)


class FeedBackAdmin(object):
    list_display = ['FeedBackId', 'FeedBackHost', 'FeedBackHost', 'FeedBackText', 'AdminText', 'AdminDocName',
                    'AdminDoc', 'add_time']
    search_field = ['FeedBackId', 'FeedBackHost', 'FeedBackHost', 'FeedBackText', 'AdminText', 'AdminDocName',
                    'AdminDoc']
    list_filter = ['FeedBackId', 'FeedBackHost', 'FeedBackHost', 'FeedBackText', 'AdminText', 'AdminDocName',
                   'AdminDoc', 'add_time']


xadmin.site.register(FeedBack, FeedBackAdmin)


class UserMessageAdmin(object):
    list_display = ['messageId', 'user', 'message', 'ms_file', 'add_time']
    search_field = ['messageId', 'user', 'message', 'ms_file']
    list_filter = ['messageId', 'user', 'message', 'ms_file', 'add_time']


xadmin.site.register(UserMessage, UserMessageAdmin)


class SupportAdmin(object):
    list_display = ['SupportId', 'SupportName', 'SupportIntro', 'SupportImage', 'add_time']
    search_field = ['SupportId', 'SupportName', 'SupportIntro', 'SupportImage']
    list_filter = ['SupportId', 'SupportName', 'SupportIntro', 'SupportImage', 'add_time']


xadmin.site.register(Support, SupportAdmin)
