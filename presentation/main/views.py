# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    slide = {
        'title': 'The Django Web Framework'
    }
    return render(request, 'main/index.html', {'slide': slide, 'link': 'page_one'})


def page_one(request):
    slide = {
        'title': 'Overview',
        'text': ''
    }
    return render(request, 'main/page.html', {'slide': slide, 'back_link': 'index', 'fwd_link': 'page_two'})


def page_two(request):
    slide = {
        'title': 'Why Python?',
        'text': '<a href="http://localhost:8080/java_source/">Java</a><br>'
                '<a href="http://localhost:8080/c_source/">C</a><br>'
                '<a href="http://localhost:8080/python_source/">Python</a>'
    }
    return render(request, 'main/page.html', {'slide': slide, 'back_link': 'page_one', 'fwd_link': 'page_three'})


def page_three(request):
    slide = {
        'title': 'Views',
        'text': ''
    }
    return render(request, 'main/page.html', {'slide': slide, 'back_link': 'page_two', 'fwd_link': 'page_four'})


def page_four(request):
    slide = {
        'title': 'URL Control',
        'text': ''
    }
    return render(request, 'main/page.html', {'slide': slide, 'back_link': 'page_three', 'fwd_link': 'page_five'})


def page_five(request):
    slide = {
        'title': 'Administration',
        'text': '<a href="http://localhost:8080/admin/">Example</a>'
    }
    return render(request, 'main/page.html', {'slide': slide, 'back_link': 'page_four', 'fwd_link': 'page_six'})


def page_six(request):
    slide = {
        'title': 'Models',
        'text': ''
    }
    return render(request, 'main/page.html', {'slide': slide, 'back_link': 'page_five', 'fwd_link': 'page_seven'})


def page_seven(request):
    slide = {
        'title': '',
        'text': '<a href="https://www.djangoproject.com/">Django</a>',
    }
    return render(request, 'main/page.html', {'slide': slide, 'back_link': 'page_six', 'fwd_link': 'end'})


def end(request):
    return HttpResponse("<img src='https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Django_logo.svg/1200px-Django_logo.svg.png' />")


def python_source(request):
    slide = {
        'title': 'Hello World - Python',
        'text': '<code>print("Hello, world!")</code><br/>23 bytes.'
    }
    return render(request, 'main/page.html', {'slide': slide, 'back_link': 'page_two'})


def c_source(request):
    slide = {
        'title': 'Hello World - C',
        'text': '<code>#include <stdio.h> '
                'int main() { '
                'printf("Hello, world!"); '
                'return 0; '
                '}</code><br/>64 bytes.'
    }
    return render(request, 'main/page.html', {'slide': slide, 'back_link': 'page_two'})


def java_source(request):
    slide = {
        'title': 'Hello World - Java',
        'text': '<code>class Hello { '
                'public static void main(String args[]) { '
                'System.out.println("Hello, world!"); '
                '} '
                '}</code><br/>94 bytes.'
    }
    return render(request, 'main/page.html', {'slide': slide, 'back_link': 'page_two'})
