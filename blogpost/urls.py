from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path 
from posts.views import homepage, post, about, search, postlist, allposts , tags_list, contact_us , thank_you 
from posts import views 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name = 'homepage'),
    path('post/<slug>/', post, name = 'post'),
    path('about/', about,name = 'about' ),
    path('search/', search, name = 'search'),
    path('postlist/<slug>/', postlist, name = 'postlist'), 
    path('posts/', allposts, name = 'allposts'),
    path('tags/', tags_list, name='tags_list'),
    path('contact/', contact_us, name='contact_us'),
    path('thank_you/', views.thank_you, name='thank_you'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
