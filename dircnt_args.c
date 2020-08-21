// fast counting of files in a dir 
// copied from https://stackoverflow.com/questions/1427032/fast-linux-file-count-for-a-large-number-of-files
// with a -2 modification
// compile with gcc -o dircnt_args dircnt_args.c
#include <stdio.h>
#include <dirent.h>

int main(int argc, char *argv[]) {
    DIR *dir;
    struct dirent *ent;
    long count;
    long countsum = 0;
    int i;

    for(i=1; i < argc; i++) {
        dir = opendir(argv[i]);
        count = 0;
        while((ent = readdir(dir)))
            ++count;

        closedir(dir);


        count = count - 2 ; // to correct off by two due to counting of . and ..
        printf("%s contains %ld files\n", argv[i], count);
        countsum += count;
    }
    printf("sum: %ld\n", countsum);

    return 0;
}
