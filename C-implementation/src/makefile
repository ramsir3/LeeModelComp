CC=gcc
CFLAGS=-g -Wall
DEPSIR = all.h lacoperon.h
SRCSIR = engine.c lacoperon.c run.c
OBJSIR = $(SRCSIR:%.c=%.o)

default: sir

sir: $(OBJSIR)
	@echo "[LINK] Linking lacmodel"
	@gcc -o lacmodel $^ $(LFLAGS)

%.o : %.c
	@echo "[COMPILE] Compiling $@"
	@gcc $(CFLAGS) -c $< -o $@
