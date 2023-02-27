DOCFILES = $(shell ls *.py | sed 's/.py/.html/')
PKG = server
include ../common.mk

docs: $(DOCFILES)

%.html: %.py
	pydoc3 -w ./$<
	git add $@
