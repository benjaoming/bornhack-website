# Bornhack

Django project to power Bornhack. Features include news, villages, webshop, and more.

## Development setup

### Clone the repo
Clone with --recursive to include submodules:

    git clone --recursive https://github.com/bornhack/bornhack-website

If you already cloned the repository, you can add the submodules like this:

    git submodule update --init --recursive

### Virtualenv
Create a Python 3 virtual environment and activate it:
```
$ virtualenv venv -p python3
$ source venv/bin/activate
```

### System libraries
Install system dependencies (method depends on OS):
- postgresql headers (for psycopg2):
  - Debian: libpq-dev
  - FreeBSD: databases/postgresql93-client
- libjpeg (for pdf generation)
  - Debian: libjpeg-dev
  - FreeBSD: graphics/jpeg-turbo
- wkhtmltopdf (also for pdf generation):
  - Debian: wkhtmltopdf
  - FreeBSD: converters/wkhtmltopdf
- fonts
  - Debian: ?
  - FreeBSD: x11-fonts/webfonts

### Python packages
Install pip packages:
```
(venv) $ pip install -r src/requirements/dev.txt
```

### Postgres

You need to have a running Postgres instance (we use Postgres-specific datetime range fields). Install Postgress, and add a database `bornhack` (or whichever you like) with some way for the application to connect to it, for instance adding a user with a password.

You can also use Unix socket connections if you know how to. It's faster, easier and perhaps more secure.

### Configuration file

Copy dev environment settings file and change settings as needed:

```
(venv) $ cp src/bornhack/environment_settings.py.dist.dev src/bornhack/environment_settings.py
```

Edit the configuration file, setting up `DATABASES` matching your Postgres settings.

### Database
Is this a new installation? Initialize the database:

```
(venv) $ src/manage.py migrate
```

Is this for local development? Bootstrap the database with dummy data and users:

```
(venv) $ src/manage.py bootstrap-devsite
```


### Done
Is this for local development? Start the Django devserver:
```
(venv) $ src/manage.py runserver
```

Otherwise start uwsgi or similar to serve the application.

Enjoy!

### Elm schedule

To build the schedule source with Elm, you need NPM and Elm, but if you have Docker, you can also run the `docker` make target:

```
cd schedule
make docker
```

## Notes

### Add a camp

Add a new camp by running:

```
(venv) $ src/manage.py createcamp {camp-slug}
```

Then go to the admin interface to edit the camp details, adding the same slug
that you just used and some current dates.

You can also specify details like:

* A sponsors page, `{camp-slug}_sponsors.html`, to `sponsors/templates`.
* A frontpage, `{camp-slug}_camp_detail.html`, to `camps/templates`.
* A call for speakers page, `{camp-slug}_call_for_speakers.html`, to `program/templates`.
* A `static_src/img/{camp-slug}/logo` and add two logos:
    * `{camp-slug}-logo-large.png`
    * `{camp-slug}-logo-small.png`

## Contributors
* Alexander Færøy https://github.com/ahf
* Benjamin Bach https://github.com/benjaoming
* coral https://github.com/coral
* Henrik Kramshøj https://github.com/kramse
* Janus Troelsen https://github.com/ysangkok
* Jonty Wareing https://github.com/Jonty
* Kasper Christensen https://github.com/fALKENdk
* klarstrup https://github.com/klarstrup
* kugg https://github.com/kugg
* RadicalPet https://github.com/RadicalPet
* Reynir Björnsson https://github.com/reynir
* Ronni Elken Lindsgaard https://github.com/rlindsgaard
* Stephan Telling https://github.com/Telling
* Thomas Steen Rasmusssen https://github.com/tykling
* Víðir Valberg Guðmundsson https://github.com/valberg
* Ximin Luo https://github.com/infinity0
