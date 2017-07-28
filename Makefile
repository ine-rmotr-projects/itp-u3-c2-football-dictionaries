.PHONY: test tox

TAG="\n\n\033[0;32m\#\#\# "
END=" \#\#\# \033[0m\n"


test:
	@echo $(TAG)Running tests$(END)
	py.test -v --tb=short tests.py

tox:
	@echo $(TAG)Running TOX$(END)
	tox
