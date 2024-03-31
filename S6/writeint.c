#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

void Usage(char * param){
	printf("This program needs integer number/s as input parameter/s. It will write binary format.\n");
}
	
int main(int argc, char **argv){
	int i;
	int num;
	
	if (argc == 1){
		Usage(argv[0]);
		return 1;
	}

	for (i=1; i<argc; i++){
		num = (int) atoi(argv[i]);
		write(1, &num, sizeof(int));
	}
	return 0;	
}
