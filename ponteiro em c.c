int main(){
    int* vetor = (int *) malloc(5 * sizeof(int));
    vetor[0] = 1;
    vetor[1] = 2;
    vetor[2] = 3;
    vetor[3] = 4;
    vetor[4] = 5;

    // printf("%d\n", vetor[0]);
    // printf("%d\n", vetor[1]);
    // printf("%d\n", vetor[2]);
    // printf("%d\n", vetor[3]);
    // printf("%d\n", vetor[4]);

    vator = (int *) realloc(vetor , 22 * sizeof (int));

    for (int i = 0; i < 22; i++) {
        vetor[i] = 2 * i;
    }

    for (int i = 0; i < 22; i++) {
        printf("%d\n", vetor[i]);
    }

}