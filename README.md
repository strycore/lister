# Lister

Lister is a minimalist to-do list and note taking application. It is composed
of a small Flask server and a Vue frontend and uses plain text files as a
storage engine.

Start a new note by opening a browser to `http://localhost:8080/note/some-note-name`

Lister can handle 3 different types of documents, its UI automatically adapts
based on the URL.

* Text notes: `/note/some-note`
* Sortable lists: `/list/a-list`
* To-do lists: `/todo/some-todo-items`

## Server setup

Install dependencies:
```
pip3 install -r config/requirements.pip
```

Configure folders for notes and lists
```
mkdir /path/to/notes
cd /path/to/notes
mkdir note todo list
export NOTES_DIR=/path/to/notes
```

Run the server: `flask run`


## Frontend setup

Installs dependencies: `npm install`

Compiles and hot-reloads for development: `npm run serve`

Compiles and minifies for production: `npm run build`
