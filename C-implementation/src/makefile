CC=gcc
CFLAGS=-g -Wall
DEPSIR = all.h sir.h
SRCSIR = engine.c sir.c model.c
OBJSIR = $(SRCSIR:%.c=%.o)

default: sir

sir: $(OBJSIR)
	@echo "[LINK] Linking sirmodel"
	@gcc -o sirmodel $^ $(LFLAGS)

%.o : %.c
	@echo "[COMPILE] Compiling $@"
	@gcc $(CFLAGS) -c $< -o $@
