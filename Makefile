help:
		@echo 'Makefile for Tinker                              '
		@echo 'Usage:                                           '
		@echo '   make wsgi_serve       start a wsgi service    '
		@echo '   make test             run test cases          '
		@echo '   make clean            clean                   '

test:   help
	python -m unittest -v tests.command

wsgi_serve:
	python core.py

clean:
	find . -name "*.pyc|*.swp|*.swo" -delete
