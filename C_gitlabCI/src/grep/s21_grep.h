#ifndef S21_GREP_H_
#define S21_GREP_H_

#include <getopt.h>
#include <regex.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define max 10000

typedef struct flags {
  char str[max];
  char str_o[max];
  char filename[max];
  char pattern[max];
  int c_flag;
  int e;
  int i;
  int v;
  int c;
  int l;
  int n;
  int h;
  int s;
  int f;
  int o;
} flags;

void grep(char *argv[], flags *A);
void parser(int argc, char *argv[], flags *A);
void f_flag(flags *A);

#endif  // S21_GREP_H_