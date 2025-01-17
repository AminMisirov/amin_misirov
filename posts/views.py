from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from .models import Category, Post, Author, Tag, Message
from .forms import ContactForm

# Author modelini istifadəçi ilə əlaqələndirmək
def get_author(user):
    qs = Author.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None

# Homepage funksiyası
def homepage(request):
    categories = Category.objects.all()[0:3]
    featured = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-timestamp')[0:3]
    context = {
        'object_list': featured,
        'latest': latest,
        'categories': categories,
    }
    return render(request, 'homepage.html', context)

# Post səhifəsi
def post(request, slug):
    post = Post.objects.get(slug=slug)
    latest = Post.objects.order_by('-timestamp')[:3]
    context = {
        'post': post,
        'latest': latest,
    }
    return render(request, 'post.html', context)

# About səhifəsi
def about(request):
    return render(request, 'about_page.html')

# Axtarış funksiyası
def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)
        ).distinct()
    context = {
        'object_list': queryset
    }
    return render(request, 'search_bar.html', context)

# Post siyahısını göstərmək
def postlist(request, slug):
    category = Category.objects.get(slug=slug)
    posts = Post.objects.filter(categories__in=[category])
    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'post_list.html', context)

# Bütün postları göstərmək
def allposts(request):
    posts = Post.objects.order_by('-timestamp')
    context = {
        'posts': posts,
    }
    return render(request, 'all_posts.html', context)

# Tag-ların siyahısı
def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'tags_list.html', {'tags': tags})

# Kontakt səhifəsi və formu
def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            Message.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            return redirect('thank_you')  # Mesaj uğurla göndərildikdən sonra
    else:
        form = ContactForm()

    return render(request, 'contact_us.html', {'form': form})

# Thank you səhifəsi
def thank_you(request):
    return render(request, 'thank_you.html')
