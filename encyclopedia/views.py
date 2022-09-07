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
    query = request.GET.get('q', '')
    if query.lower() in list(map(to_lower, util.list_entries())):
        return HttpResponseRedirect(f'http://localhost:8000/wiki/{query}')
    search_results = []
    for elem in util.list_entries():
        if query.lower() in elem.lower():
            search_results.append(elem)
    return render(request, "encyclopedia/results.html", {
        "query": query,
        "results": search_results,
        "matches": len(search_results) > 0
    })


def create_page(request):
    return render(request, "encyclopedia/new.html", {
        "page_exists": False
    })


def publish_new_page(request):
    md = request.GET.get('page_text')
    html = parse_md(md)
    name = html[html.find('<h1>') + 4: html.find('</h1>')]
    if name.lower() in list(map(to_lower, util.list_entries())):
        return render(request, "encyclopedia/new.html", {
            "page_exists": True,
            "name": name
        })
    else:
        util.save_entry(name, md)
        return HttpResponseRedirect(f'wiki/{name}')


def publish_edited_page(request):
    md = request.GET.get('page_text')
    html = parse_md(md)
    name = html[html.find('<h1>') + 4: html.find('</h1>')]
    util.save_entry(name, md)
    return HttpResponseRedirect(f'wiki/{name}')


def edit(request, page):
    return render(request, "encyclopedia/edit.html", {
        "initial_content": util.get_entry(page),
        "entry": page
    })

def parse_md(content):
    return markdown(content) if content else content


def to_lower(elem):
    return elem.lower()
