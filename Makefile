help:
		@echo 'Makefile for Tinker                              '
		@echo 'Usage:                                           '
		@echo '   make test             run test cases          '
		@echo '   make clean            clean                   '
		@echo '   make mybot            start bot               '

test:   help
	python -m unittest -v tests.command

clean:
	find . -name "*.pyc|*.swp|*.swo" -delete

mybot:
	python -m bot.wechat_bot
