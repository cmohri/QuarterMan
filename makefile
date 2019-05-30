run: app.db
	export FLASK_APP=elbarto/run.py
	flask run

app.db: migrations
	flask db upgrade
	flask db migrate

migrations:
	flask db init
