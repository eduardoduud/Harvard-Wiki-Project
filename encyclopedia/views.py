from django.shortcuts import render, redirect

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entries(request, title):
    return render(request, "encyclopedia/entry.html", {
        "entry": util.get_entry(title),
        "title": title
    })

def search(request):
    if request.method == "GET":
        title = request.GET['q']
        if title:
            entries = util.list_entries()
            for entry in entries:
                if title == entry:
                    return redirect('entries', title=title)
            substring_list = []
            for entry in entries:
                if title.lower() in entry.lower():
                    substring_list.append(entry)
            return render(request, "encyclopedia/search.html", {
                "entries": substring_list,
                "title": title
            })