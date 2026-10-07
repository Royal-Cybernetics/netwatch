PREFIX = /opt/netwatch
CONFDIR = /etc/netwatch

install:
	install -d $(PREFIX)
	install -m 644 src/scanner.py $(PREFIX)/scanner.py
	python3 -m venv $(PREFIX)/venv
	$(PREFIX)/venv/bin/pip install -r requirements.txt
	install -d $(CONFDIR)
	test -f $(CONFDIR)/netwatch.env || install -m 644 .env.example $(CONFDIR)/netwatch.env
uninstall:
	rm -rf $(PREFIX)
.PHONY: install uninstall 
