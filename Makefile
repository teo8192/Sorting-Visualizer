LIBSOURCE=*.c *.h

.PHONY: all
all: libsort.so

libsort.so: $(LIBSOURCE) Makefile
	gcc -shared -o $@ -fPIC $(LIBSOURCE)
