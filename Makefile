server:
	. venv/bin/activate; python app/main.py

db:
	rm -f app/sql.db
	. venv/bin/activate; python app/makedb.py
