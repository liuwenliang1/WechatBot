help:
		@echo 'Makefile for Tinker                              '
		@echo 'Usage:                                           '
		@echo '   make install          install                                          '
		@echo '   make test             run test cases          '
		@echo '   make clean            clean                   '
		@echo '   make mybot            start bot               '

install:
	pip install -r requirements.txt

test:
	python -m unittest -v tests.command

clean:
	find . \( -name *.pyc -o -name *.swp -o -name *.swo \) -delete

mybot:
	python -m bot.wechat_bot
