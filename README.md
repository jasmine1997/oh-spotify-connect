# SpotifyConnect

This connects your Spotify account to OpenHumans and recommends music to you based on a set of parameters that you can tweak

To run the project from source:

- Install python dependencies using [pipenv](https://github.com/pypa/pipenv#installation)
```
pipenv install
```
- Populate the environment variables listed in `env.sample` in `.env`
- Apply migrations
```
python manage.py migrate
```
- Run server
```
python manage.py runserver
```
- Update user recently played data
```
python manage.py update_data
```
