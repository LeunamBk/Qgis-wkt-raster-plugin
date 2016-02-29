UI_SOURCES=$(wildcard ui/*.ui) $(wildcard db_plugins/*/ui/*.ui)
UI_FILES=$(patsubst %.ui,%.py,$(UI_SOURCES))

RC_SOURCES=$(wildcard *.qrc) $(wildcard db_plugins/*/*.qrc)
RC_FILES=$(patsubst %.qrc,%.py,$(RC_SOURCES)) 

GEN_FILES = ${UI_FILES} ${RC_FILES}

all: $(GEN_FILES)
ui: $(UI_FILES)
resources: $(RC_FILES)

$(UI_FILES): %.py: %.ui
	pyuic4 -o $@ $< || return 0
	
$(RC_FILES): %.py: %.qrc
	pyrcc4 -o $@ $< || return 0

clean:
	rm -f $(GEN_FILES) *.pyc

package:
	make && cd .. && rm -f wktraster.zip && zip -r wktraster.zip wktraster -x \*.svn* -x \*.pyc -x \*~ -x \*entries\* -x \*.git\*
