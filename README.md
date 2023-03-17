# NoteApp
NoteApp is a basic web application for taking notes online. The application allows users to create an account, log in, and create notes that are saved to a database. The application is built with Flask and uses a SQLite database to store notes and user accounts.

## Installation
To run the application, first clone the repository:

``` bash
git clone https://github.com/tobiasiglesias/NoteApp
```

Install the required dependencies:

``` bash
pip install -r requirements.txt
```

Finally, run the application:
``` bash
python main.py
```

The application will be available at http://localhost:5000.


## Usage
To use the application, you must first create an account. Click "Sign up" on the homepage and complete the registration form. Once registered, you will be automatically logged in.
![Captura de pantalla de la página de inicio](screenshots/2023-03-17%2012_42_12-.png)

Once you've logged in, you can create a note by clicking the "Create note" button. Enter the title and content of the note and click "Save". Saved notes will be available on the main page.

![Captura de pantalla de la página de notas](screenshots/2023-03-17%2012_48_47-Notes%20-%20Brave.png)


NoteApp allows users to easily view all notes with the same title. By clicking on the title of a note, users will be redirected to a page that displays all notes with that same title. This feature makes it easy for users to quickly access all their notes on a particular topic, without having to manually search through their notes.

![Captura de pantalla de la opcion de titulos](screenshots/2023-03-17%2012_52_13-.png)
