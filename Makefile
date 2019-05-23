# Author: Teodor Dahl Knutsen <teodor@dahlknutsen.no>

LIBSOURCE=*.c *.h

.PHONY: all
all: libsort.so

.PHONY: clean
clean:
	@rm -rf libsort.so

libsort.so: $(LIBSOURCE) Makefile
	gcc -shared -o $@ -fPIC $(LIBSOURCE)
