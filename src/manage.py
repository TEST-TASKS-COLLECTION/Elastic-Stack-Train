from flask.cli import FlaskGroup

from elastic_app import client, app

cli = FlaskGroup(app)

if __name__ == "__main__":
    cli()