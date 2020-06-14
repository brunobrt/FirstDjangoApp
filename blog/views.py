from django.shortcuts import render

posts = [
    {
        'author': 'Bruno Bartolomasi',
        'title': 'First Blog Post',
        'content': 'This is my fist blog post ever!',
        'date_posted': 'June 13th, 2020'
    },
    {
        'author': 'Bruno R Bartolomasi',
        'title': 'Second Blog Post',
        'content': 'This is my second blog post ever!',
        'date_posted': 'June 14th, 2020'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': about})
