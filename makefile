run: elbarto/app.db
	export FLASK_APP=elbarto/run.py
	flask db upgrade
	flask db migrate
	flask run

clean:
	rm -rf migrations
	rm elbarto/app.db
	flask db init

elbarto/app.db:
	flask db init
