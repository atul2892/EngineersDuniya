from django.contrib import admin
from django.urls import path
from mainApp import views
from django.conf.urls.static import static 
from django.conf import settings 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogComment/', views.blogComment, name='blogComment'),
    path('',views.homePage),
    path('call-back-details/',views.callBackDetails),
    path('subscribtions/',views.subscribtions),
    path('about/',views.about),
    path('blog-grid/',views.blog),
    path('blog-single-left/<int:id>',views.blogSingle),
    path('contact/',views.contact),
    path('services/',views.services),
    path('website/',views.website),
    path('mobile-app/',views.mobileApp),
    path('graphics-designing/',views.graphicsDesigning),
    path('digital-marketing/',views.digitalMarketing),
    path('seo/',views.seo),
    path('social-media/',views.socialMedia),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
