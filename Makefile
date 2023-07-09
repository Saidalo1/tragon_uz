.PHONY: mig

mig:
	@echo "----- Running migrations... -----"
	@python manage.py makemigrations --noinput
	@echo "----- Migrations created! -----"
	@python manage.py migrate --noinput
	@echo "----- Migrations applied! -----"

make admin:
	@echo "----- Creating superuser... -----"
	@python manage.py createsuperuser
