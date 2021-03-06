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
        'text': 'The Web Framework for Perfectionists with Deadlines',
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
        'text': '<ul>'
                '<li>Programmatic Delivery of HTTP content</li>'
                '<li>Implemented as Class/function</li>'
                '<li>Delivers HTTPResponse object that the middleware renders as HTML'
                '</ul>'
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
        'text': 'Backend database abstraction<br/>'
    }
    return render(request, 'main/page.html', {'slide': slide, 'back_link': 'page_five', 'fwd_link': 'page_seven'})


def page_seven(request):
    slide = {
        'title': '',
        'text': '<a href="https://www.djangoproject.com/">Django</a>',
    }
    return render(request, 'main/page.html', {'slide': slide, 'back_link': 'page_six', 'fwd_link': 'zen'})


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


def zen(request):
    slide = {
        'title': 'The Zen of Python',
        'text': '''Beautiful is better than ugly.<br/>
Explicit is better than implicit.<br/>
Simple is better than complex.<br/>
Complex is better than complicated.<br/>
Flat is better than nested.<br/>
Sparse is better than dense.<br/>
Readability counts.<br/>
Special cases aren't special enough to break the rules.<br/>
Although practicality beats purity.<br/>
Errors should never pass silently.<br/>
Unless explicitly silenced.<br/>
In the face of ambiguity, refuse the temptation to guess.<br/>
There should be one-- and preferably only one --obvious way to do it.<br/>
Although that way may not be obvious at first unless you're Dutch.<br/>
Now is better than never.<br/>
Although never is often better than *right* now.<br/>
If the implementation is hard to explain, it's a bad idea.<br/>
If the implementation is easy to explain, it may be a good idea.<br/>
Namespaces are one honking great idea -- let's do more of those!<br/>'''
    }
    return render(request, 'main/page.html', {'slide': slide, 'back_link': 'page_seven', 'fwd_link': 'end'})
