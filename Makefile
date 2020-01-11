# TODO (Khangaroo): Make this process a lot less hacky (no, export did not work)
# See MakefileNRO

.PHONY: all clean skyline send

CROSSVER ?= 600

all: skyline

skyline:
	$(MAKE) all -f MakefileNRO CROSSVER=$(CROSSVER)

send: all
	python scripts/sendPatch.py $(IP) $(CROSSVER)

clean:
	$(MAKE) clean -f MakefileNRO
