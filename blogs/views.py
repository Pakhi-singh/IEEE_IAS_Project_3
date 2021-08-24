from django.shortcuts import render
from .models import BlogPlant, Category

def blog_home(request):
    context = {
        "blogs": BlogPlant.objects.all(),
        "tags": {
        'plant': 'PLANT TALK',
        'gardening': 'GARDENING DIY\'S',
        'styling' : 'PLANTS STYLING',
        'kitchen' : 'KITCHEN GARDENING',
        'developement' : 'SUSTAINABLE DEVELOPEMENT'
        }
    }
    return render(request, "blogs/blog_home.html", context)

def blog_upload(request):
    if request.method == 'POST':
        author = request.POST['author']
        blog_title = request.POST['blog_title']
        blog_content = request.POST['blog_content']
        blog_image = request.POST['blog_image']
        category = request.POST['category']
        blog = BlogPlant.objects.create(author=author, blog_title=blog_title, blog_content=blog_content, blog_image=blog_image, category=category)
        blog.save()
        return render(request, 'blog_upload.html')
    else:
        return render(request, 'blog_upload.html')

def blog_details(request, the_slug):
    blog = BlogPlant.objects.filter(slug=the_slug)

    return render(request, 'blogs/blog_details.html', {'blog': blog[0]})
