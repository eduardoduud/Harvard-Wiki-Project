import re
import markdown2

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))


def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))

def save_and_rename(old_title, new_title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    old_filename = f"entries/{old_title}.md"
    new_filename = f"entries/{new_title}.md"

    if old_title != new_title:
        if default_storage.exists(old_filename):
            default_storage.delete(old_filename)
    default_storage.save(new_filename, ContentFile(content))


def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        with default_storage.open(f"entries/{title}.md") as f:
            md_content = f.read()
        return markdown2.markdown(md_content)
    except FileNotFoundError:
        f = default_storage.open("encyclopedia/templates/encyclopedia/notfound.html")
        return f.read().decode("utf-8")
