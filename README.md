## Online Encyclopedia

This GitHub repository hosts the code for an online encyclopedia project inspired by Wikipedia. The project aims to provide a platform where users can create, edit, and browse encyclopedia entries on various topics.

  

## Technologies Used:

 - Python: The project is built using Django, a high-level Python web
   framework.
 - Markdown: Encyclopedia entries are stored using Markdown, a
   lightweight markup language, making it human-friendly to write and
   edit.
 - HTML/CSS: Frontend templates and styling are done using HTML and CSS.
 - python-markdown2: Markdown content is converted to HTML using the
   python-markdown2 package.

## Project Features:

 1. Entry Page: Users can visit /wiki/TITLE to view the contents of a
    specific encyclopedia entry. If the requested entry does not exist,
    an error page is displayed.
 2. Index Page: The index page lists all encyclopedia entries, and users
    can click on any entry name to directly navigate to that entry's
    page.
 3. Search: Users can search for encyclopedia entries using a search
    box. If the query matches an entry's name, the user is redirected to
    that entry's page. If not, a search results page is displayed with
    relevant entries.
 4. New Page: Users can create new encyclopedia entries by clicking
    "Create New Page" in the sidebar. They can enter a title and
    Markdown content for the new page.
 5. Edit Page: Each entry page has a link to edit the entry's content.
    Users can edit the Markdown content in a textarea and save the
    changes.
 6. Random Page: Clicking "Random Page" in the sidebar takes the user to
    a random encyclopedia entry.
 7. Markdown to HTML Conversion: Markdown content is converted to HTML
    before being displayed to the user, ensuring proper rendering of
    headings, bold text, lists, links, and paragraphs.

## Getting Started:

Clone the repository.

Install necessary dependencies.

Run the Django server to launch the application locally.

## Directory Structure:

**encyclopedia/**: Contains the Django project and app files.

**encyclopedia/entries/**: Directory to store encyclopedia entries as Markdown files.

**encyclopedia/templates/**: HTML templates for rendering views.

**encyclopedia/static/**: Static files like CSS and JavaScript.