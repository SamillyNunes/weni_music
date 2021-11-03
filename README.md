# Weni Music API
This system refers to a music API developed for Weni Company, 
while participating of a selection. It consists in a music manager, where
stores musics, artists and playlists. Inside that, a music contains a title
and an artist, an artist contains a name and a playlist contains a list of
musics.

### Requirements

Cloning these applications requires the features below:
- Python 3
- Django
- Django rest framework

And other python lib requirements described in requirements.txt

### Structure

The API module is structured in the followed way:
- Models: Where the entities are defined
- Views: Where the rest methods (get, post, put, delete) are implemented
- Urls: Where the endpoints are described and targeted
- Serializers: Where the classes responsible for converting json
files in object types, and also the inverse option, are implemented
- Tests: Where the unit tests are perfomed
- Admin: Where some admin features are implemented, like registering
a model for using it in the admin page
- Apps: Information about the module

### Running

1. Clone the repository with `git clone https://github.com/SamillyNunes/weni_music.git` in your local machine
2. Enter the weni music folder
3. Type `python manage.py runserver` inside the terminal
4. Follow the API address indicated in the information presented, usually localized in http://127.0.0.1:8000/

### Endpoints

The endpoints option you can use are:

- `http://localhost/admin/`: Where you can access the admin page
- `http://localhost/swagger/`: The documentation with swagger interface
- `http://localhost/swagger.json`: The documentation in .json file
- `http://localhost/swagger.yaml`: The documentation in .yaml file
- `http://localhost/redoc/`: The documentation in another interface
- `http://localhost/musics/`: The musics list
- `http://localhost/musics/id`: The id music (1, 2, ...)
- `http://localhost/artists`: The artists list
- `http://localhost/artists/id`: The id artist (1, 2, ...)
- `http://localhost/playlist`: The playlist list
- `http://localhost/playlist/id`: The id playlist (1, 2, ...)