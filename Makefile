help:
		@echo 'Makefile for Tinker                              '
		@echo 'Usage:                                           '
		@echo '   make install          install                                          '
		@echo '   make test             run test cases          '
		@echo '   make clean            clean                   '
		@echo '   make mybot            start bot               '
		@echo '   make docs             update docs             '
		@echo '   make upload           upload to pypi          '

install:
	pip install -r requirements.txt

test: install
	cd wechatbot; pytest
	make clean

clean:
	find . \( -name "*.pyc" -o -name "*.log" -o -name "*.swp" -o -name "*.swo" \) -delete

mybot:
	cd wechatbot; python -m bot.wechat_bot

docs:
	cd wechatbot
	cd docs; make html
	open docs/_build/html/index.html

upload:
	python setup.py sdist bdist_wheel
	twine upload dist/*

.PHONY: docs
