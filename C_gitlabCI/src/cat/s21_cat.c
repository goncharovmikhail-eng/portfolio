#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#define max 10000
#define optmax 8

bool parser(int argc, char* argv[], int option[]);
void cat(int argc, char* argv[], int code);
void add_v(char str[], int i);

int main(int argc, char* argv[]) {
  int flag = 0;  // for return;
  int opt[optmax] = {0};
  if (!parser(argc, argv, opt)) flag += 1;

  int code = -1;
  int welche_opt = 0;
  for (int i = 0; i < optmax; i++) {
    if (opt[i]) welche_opt++;
    if (opt[i]) code = i;
  }

  if (flag > 0) return 0;
  cat(argc, argv, code);
}

bool parser(int argc, char* argv[], int option[]) {
  bool flag = true;
  for (int i = 1; i < argc && flag; i++) {
    if (argv[i][0] != '-') continue;
    if (strlen(argv[i]) == 2 && argv[i][0] == '-' && argv[i][1] != '-') {
      switch (argv[i][1]) {
        default:
          flag = false;
          break;
        case 'n':
          option[0] = 1;
          break;
        case 'b':
          option[1] = 1;
          break;
        case 's':
          option[2] = 1;
          break;
        case 't':
          option[3] = 1;
          break;
        case 'T':
          option[4] = 1;
          break;
        case 'e':
          option[5] = 1;
          break;
        case 'E':
          option[6] = 1;
          break;
        case 'v':
          option[7] = 1;
          break;
      }
    } else {
      int code = -1;
      if (strcmp(argv[i], "--number-nonblank") == 0) code = 0;
      if (strcmp(argv[i], "--number") == 0) code = 1;
      if (strcmp(argv[i], "--squeeze-blank") == 0) code = 2;
      if (strcmp(argv[i], "--") == 0) code = 3;
      if (strcmp(argv[i], "-") == 0) code = 3;

      switch (code) {
        default:
          fprintf(stderr,
                  "cat: неверный ключ — «%s»\n По команде «cat --help» можно "
                  "получить дополнительную информацию.\n",
                  argv[2]);
          flag = false;
          break;
        case 0:
          option[1] = 1;
          break;
        case 1:
          option[1] = 1;
          break;
        case 2:
          option[2] = 1;
          break;
        case 3:
          break;
      }
    }
  }
  return flag;
}

void cat(int argc, char* argv[], int code) {
  FILE* file = NULL;
  char str_in_file[max];
  int num_str = 0;
  int full_str_num = 0;
  char s1 = 36;
  bool succes = true;
  int symbol = 0;
  char last[max];
  last[0] = '\0';
  int fl = 0;

  for (int i = 1; i < argc; i++) {
    file = fopen(argv[i], "r");
    if (file == NULL) {
      file = fopen(argv[i + 1], "r");
    }
    if (file != NULL) {
      while (!feof(file)) {
        if (fgets(str_in_file, max, file) != NULL) {
          num_str += 1;
          int j;
          for (j = 0; str_in_file[j] == '\0'; j++) {
          }
          int h = 0;
          int last_symbl = 0;
          while (str_in_file[h] != 10) {
            symbol += 1;
            h++;
          }
          if (code == -1) printf("%s", str_in_file);
          if (code == 0) printf("%6d\t%s", num_str, str_in_file);  // -n
          if (code == 1) {                                         //-b
            if (symbol != last_symbl) {
              full_str_num += 1;
              printf("%6d\t%s", full_str_num, str_in_file);
            }
            if (symbol == last_symbl) printf("%s", str_in_file);
            symbol = last_symbl;
          }
          if (code == 2) {  // -s

            if (str_in_file[0] == '\n' && last[0] == '\n') {
              fl++;
            } else {
              printf("%s", str_in_file);
            }
          }
          if (code == 3 || code == 4) {  // -t; -T
            char buff[1024] = {'^', 'I'};
            char tabb = 9;
            for (int index = 0; str_in_file[index] != '\0'; index++) {
              add_v(str_in_file, index);

              if (str_in_file[index] == tabb) {
                strcat(buff, str_in_file + j + 1);
                strcpy(str_in_file, buff);
              }
            }
            printf("%s", str_in_file);
          }
          if (code == 5 || code == 6) {  //-e; -E
            int index;
            for (index = 0; str_in_file[index] != '\0'; index++) {
              add_v(str_in_file, index);
            }
            str_in_file[index - 1] = s1;
            printf("%s\n", str_in_file);
          }
          if (code == 7) {  // -v
            for (int index = 0; str_in_file[index] != '\0'; index++) {
              add_v(str_in_file, index);
            }
            printf("%s", str_in_file);
          }
          i++;
          if (feof(file)) printf("\n");
        }
        *last = *str_in_file;
      }
    }
    if (file == 0) {
      fprintf(stderr, "cat: %s: Нет такого файла или каталога\n", argv[i]);
      break;
    }
  }
  if (argc <= 1) {
    char input[max];
    while (succes == true) {
      scanf("%248s", input);
      printf("%s\n", input);
    }
  }
  fclose(file);
}
void add_v(char str[], int i) {
  if (str[i] < 31 && str[i] != 10 && str[i] != 9) {
    str[i] += 64;
    char buffer[1024] = "";
    strncat(buffer, str, i);
    strcat(buffer, "^");
    strcat(buffer, str + i);
    strcpy(str, buffer);
  }
}
