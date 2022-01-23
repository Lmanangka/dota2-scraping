PREFIX := ~/
all: install
install:
	cp dota_stat.py $(DESTDIR)$(PREFIX)bin/dota_stat
	chmod 0755 $(DESTDIR)$(PREFIX)bin/dota_stat
uninstall:
	$(RM) $(DESTDIR)$(PREFIX)bin/dota_stat
.PHONY: all install uninstall
