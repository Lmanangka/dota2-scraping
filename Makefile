PREFIX := ~/
all: install
install:
	cp dota_stat.py $(DESTDIR)$(PREFIX)bin/dota-stat
	chmod 0755 $(DESTDIR)$(PREFIX)bin/dota-stat
uninstall:
	$(RM) $(DESTDIR)$(PREFIX)bin/dota-stat
.PHONY: all install uninstall
