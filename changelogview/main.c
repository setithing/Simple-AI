/*Simple changelog viewer. v0.01
*Licenced under the GPL.
*Copyright Ben Tatman 2012*/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct {
  char date[50];
  char desc[500];
  char title[50];
  char todo[50][500];
} update;
update changes[50];

int current = -1;

/*DATE: 16-11-12
OVERVIEW: Updated name generation
DESC: Made it so the user can force it to generate names
TODO: Make it take arguments from CMD, instead of on waking up.
LINES: 41-72, 125-144*/

size_t ExtractSubstring(const char* source, size_t position, size_t size_to_copy, char* destination) {

memcpy(destination, source+position, size_to_copy);
destination[size_to_copy]='\0';
return size_to_copy;
}
/*substring function*/
char* substr(const char* source, size_t position, size_t size_to_copy) {
	char* buffer=(char*)malloc((size_to_copy+1)*sizeof(char)); //Allocate memory
	if (NULL==buffer) return NULL; //Check if buffer has space
	ExtractSubstring(source, position, size_to_copy, buffer); //Uses other function
	return buffer;
}

int read(char filename[500]) {
	FILE* fp;
	char line[600];
	if ((fp = fopen(filename,"r"))!=NULL) {
		while(fgets(line,sizeof(line),fp)) {
			if (strcmp(substr(line,0,strlen("DATE")),"DATE") == 0) {
				current++;
				strcpy(changes[current].date,substr(line,strlen("DATE: "),100));
			} else if (strcmp(substr(line,0,strlen("OVERVIEW")), "OVERVIEW") == 0) {
				strcpy(changes[current].title,substr(line,strlen("OVERVIEW: "),100));
			} else if (strcmp(substr(line,0,strlen("DESC")),"DESC") == 0) {
				strcpy(changes[current].desc,substr(line,strlen("DESC: "),100));
			} else if (strcmp(substr(line,0,strlen("TODO")),"TODO") == 0) {
				strcpy(changes[current].todo[0],substr(line,strlen("TODO: "),100));
			}
		}
		fclose(fp);
	} else {
		return -1;
	}

	return 1;
}

void view(int i) {
	printf("%s - %s\n Description: %s\n Todo: %s\n",substr(changes[i].date,0,strlen(changes[i].date)-1), substr(changes[i].title,0,strlen(changes[i].title)-1), substr(changes[i].desc,0,strlen(changes[i].desc)-1), substr(changes[i].todo[0],0,strlen(changes[i].todo[0])-1));
	return;
}

int main(int argc, char *argv[]) {
	char file[500] = "../changelog";
	int i;
	if (argc >= 2)
		strcpy(file,argv[1]);
	read(file);
	if (argc >= 3) {
		if (strcmp(argv[2],"view") == 0) {
			if (strcmp(argv[3],"all") == 0) {
				for (i=0;i<=current;i++) {
					 view(i);
				}
			} else {
				view(atoi(argv[3]));
			}
		} else if (strcmp(argv[2],"list") == 0) {
			for (i=0;i<=current;i++) {
				 printf("%d (%s) %s\n",i,substr(changes[i].date,0,strlen(changes[i].date)-1),substr(changes[i].title,0,strlen(changes[i].title)-1));
			}
		}
	}

  return 1;
}