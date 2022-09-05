from django.shortcuts import render
from markdown2 import markdown
from random import choice
from django.http import HttpResponseRedirect

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
    })

def entry(request, page):
    html = parse_md(util.get_entry(page))
    return render(request, "encyclopedia/page.html", {
        "entry": html,
        "title": page
    })

def random(request):
    return HttpResponseRedirect(f'wiki/{choice(util.list_entries())}')

def search(request):
    print(request.GET.get('q'))

def parse_md(content):
    return markdown(content) if content else content
