#include <stdio.h>
#include <stdlib.h>
#include <string.h> // Include string.h for strcmp function
#include <unistd.h>

void Usage(char *param) {
  printf("This program needs integer number/s as input parameter/s. It will "
         "write binary format.\n");
}

int main(int argc, char **argv) {
  int i;
  int num;
  char *type;

  if (argc < 3) { // Check if enough arguments are provided
    Usage(argv[0]);
    return 1;
  }

  type = argv[1]; // First parameter indicates the type of data

  // Loop through the rest of the arguments
  for (i = 2; i < argc; i++) {
    // Convert the input parameter according to the specified type
    if (strcmp(type, "char") == 0) {
      char c = (char)atoi(argv[i]);
      write(1, &c, sizeof(char));
    } else if (strcmp(type, "short") == 0) {
      short s = (short)atoi(argv[i]);
      write(1, &s, sizeof(short));
    } else if (strcmp(type, "int") == 0) {
      int n = atoi(argv[i]);
      write(1, &n, sizeof(int));
    } else if (strcmp(type, "long") == 0) {
      long l = atol(argv[i]); // Use atol for long
      write(1, &l, sizeof(long));
    } else if (strcmp(type, "longlong") == 0) {
      long long ll = atoll(argv[i]); // Use atoll for long long
      write(1, &ll, sizeof(long long));
    } else {
      printf("Invalid type specified.\n");
      return 1;
    }
  }
  return 0;
}
