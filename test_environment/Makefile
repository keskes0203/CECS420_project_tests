


SOURCES=$(wildcard  *.c)
OBJECTS=$(patsubst %.c,%.o,$(SOURCES))
TARGET=$(patsubst %.c,%,$(SOURCES))

all: $(TARGET)

$(TARGET): $(OBJECTS)
	gcc -o $@ $@.o
$(OBJECTS):
	gcc -o $@ -c $*.c
