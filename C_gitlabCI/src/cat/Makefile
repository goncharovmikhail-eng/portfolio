SOURCES_1 = s21_cat.c

all: s21_cat style test $(TARGET)
s21_cat: $(SOURCES_1) s21_cat.c
	gcc -Wall -Wextra -Werror -std=c11 $(SOURCES_1) -o s21_cat
style:
	clang-format -i s21_cat.c
test:
	bash test.sh
