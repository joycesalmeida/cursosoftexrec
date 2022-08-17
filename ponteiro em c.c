#include<stdlib.h>
#include<stdio.h>

int main(){
    int* vetor = (int *) malloc(5 * sizeof(int));
    
    vator = (int *) realloc(vetor , 22 * sizeof (int));

    for (int i = 0; i < 22; i++) {
        vetor[i] = 2 * i;
    }

    for (int i = 0; i < 22; i++) {
        printf("%d\n", vetor[i]);
    }
    
    free(vetor);

}
