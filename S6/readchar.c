#include <stdio.h>
#include <unistd.h>
	
int main(int argc, char **argv){
	int i=0;
	char num;
	
	while(read(0, &num, sizeof(char))){
		printf("value: %c (%d decimal value)\n", num, num); 
	}
	return 0;	
}
