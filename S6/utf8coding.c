#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>

int utf8chr(char * c, int cp)
{
    int l;
    if     (cp<=0x7F)  { c[0] = cp; l = 1; }
    else if(cp<=0x7FF) { c[0] = (cp>>6)+192; c[1] = (cp&63)+128; l = 2; }
    else if(0xd800<=cp && cp<=0xdfff) { l = -1; } //invalid block of utf8
    else if(cp<=0xFFFF) { c[0] = (cp>>12)+224; c[1]= ((cp>>6)&63)+128; c[2]=(cp&63)+128; l = 3; }
    else if(cp<=0x10FFFF) { c[0] = (cp>>18)+240; c[1] = ((cp>>12)&63)+128; c[2] = ((cp>>6)&63)+128; c[3]=(cp&63)+128; l = 4; }
    else l = -1; // invalid codepoint
    return l;
}

void Usage(char * param){
	printf("This program presents UTF-8 characters read from the input.\n"
		"\t%s [-?]\n"
		"\t\t-?: show this help\n"
		"\t%s [-v]\n"
		"\t\t-v: verbose\n", param, param);
}

int main(int argc, char **argv){
	char str[100];
	char *s, verbose=0;
	int length, integer;

	if (argc == 2)	{
		if (strcmp(argv[1], "-?")==0){
			Usage(argv[0]);
			return 0;
		} else if(strcmp(argv[1], "-v")==0){
			verbose=1;
		} else {
			Usage(argv[0]);
			return 0;
		} 
	}

	while(read(0, &integer, sizeof(int))>0){
		bzero(str, sizeof(str));
		s = str;
		length = utf8chr(s, integer);

		if (verbose){
		   printf ("(%d bytes, %04d, U+%04x) %s\n", length, integer, integer, s);
		} else {
			printf("%s ", s);
		}
	}
   printf ("\n");
   
	return 0;
}
