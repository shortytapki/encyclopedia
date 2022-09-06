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
    return render(request, "encyclopedia/page.html", {
        "entry": parse_md(util.get_entry(page)),
        "title": page
    })


def random(request):
    return HttpResponseRedirect(f'wiki/{choice(util.list_entries())}')


def search(request):
    def to_lower(elem):
        return elem.lower()
    query = request.GET.get('q', '')
    if query == '':
        return HttpResponseRedirect(f'http://localhost:8000')
    if query.lower() in list(map(to_lower, util.list_entries())):
        return HttpResponseRedirect(f'http://localhost:8000/wiki/{query}')
    search_results = []
    for elem in util.list_entries():
        if query in elem:
            search_results.append(elem)
    return render(request, "encyclopedia/results.html", {
        "entry": query,
        "results": search_results,
        "matches": len(search_results) > 0
    })


def parse_md(content):
    return markdown(content) if content else content
