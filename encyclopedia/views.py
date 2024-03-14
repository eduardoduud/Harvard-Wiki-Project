import random

from django.shortcuts import render, redirect
from django import forms

from html2markdown import convert

from . import util

class NewEntryForm(forms.Form):
    entry = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Title'}), label="")
    content = forms.CharField(widget= forms.Textarea(attrs={'placeholder':'Write your article'}), label="")

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entries(request, title):
    return render(request, "encyclopedia/entry.html", {
        "entry": util.get_entry(title),
        "title": title
    })

def new_entry(request):
    form = NewEntryForm(request.POST)
    if form.is_valid():
        title = form.cleaned_data["entry"]
        content = form.cleaned_data["content"]
        entries = util.list_entries()
        if title in entries:
            error_message = "An entry with this title already exists."
            return render(request, "encyclopedia/new_entry.html", {
                "form": form,
                "error_message": error_message
            })
        else:
            util.save_entry(title, content)
            return redirect('entries', title=title)
    else:
        form = NewEntryForm()
        return render(request, "encyclopedia/new_entry.html", {
            "form": form        
    })

def edit_entry(request, title):
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            new_content = form.cleaned_data["content"]
            old_title = title
            new_title = form.cleaned_data["entry"]
            util.save_and_rename(old_title, new_title, new_content)
            return redirect('entries', title=new_title)
    else:
        entry_content = util.get_entry(title)
        if entry_content is not None:
            markdown_content = convert(entry_content)
            form = NewEntryForm(initial={'entry': title, 'content': markdown_content})
            return render(request, "encyclopedia/edit_entry.html", {
                "form": form,
                "title": title
            })
        else:
            return render(request, "encyclopedia/notfound.html", {
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
        
def random_entry(request):
    entries = util.list_entries()
    random_title = random.choice(entries)
    return redirect('entries', title=random_title)