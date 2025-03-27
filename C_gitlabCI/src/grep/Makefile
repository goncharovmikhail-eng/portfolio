TARGET = s21_grep
GCC = gcc -Wall -Wextra -Werror -std=c11

all: clang clean $(TARGET)

$(TARGET):
	$(GCC) $(TARGET).c -o $(TARGET)


clean:
	rm -rf *.o *.out $(TARGET) .clang-format

clang:
	clang-format -style=google -i *.c *.h

