# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

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
        'title': 'Models',
        'text': ''
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
        'text': ''
    }
    return render(request, 'main/page.html', {'slide': slide, 'back_link': 'page_four', 'fwd_link': 'page_six'})


def page_six(request):
    slide = {
        'title': 'Django Source Code',
        'text': ''
    }
    return render(request, 'main/page.html', {'slide': slide, 'back_link': 'page_five', 'fwd_link': 'page_seven'})