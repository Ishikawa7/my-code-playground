#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define N_ELEMENTS_TO_SORT 10
#define MAX_VALUE 300

// Funzione per ordinare un array usando CountingSort
void CountingSort(int* arr, int n) {
  // Crea un array di dimensione MAX_VALUE per memorizzare la frequenza di ciascun elemento
  int counts[MAX_VALUE+1] = {0};

  // Contare la frequenza di ciascun elemento nell'array
  for (int i = 0; i < n; i++) {
    counts[arr[i]]++;
  }

  // Scorri l'array counts e aggiungi ciascun elemento all'array originale per il numero di volte in cui appare nell'array counts
  int j = 0;
  for (int i = 0; i < 301; i++) {
    for (int k = 0; k < counts[i]; k++) {
      arr[j++] = i;
    }
  }
}

int main() {
    // Crea un array casuale di numeri interi compresi tra 0 e 300 con MAX_VALUE elementi
    srand(time(NULL));
    int arr[N_ELEMENTS_TO_SORT];

    for (int i = 0; i < N_ELEMENTS_TO_SORT; i++) {
        arr[i] = rand() % 301;
    }

    int n = sizeof(arr) / sizeof(arr[0]);

    // Misura il tempo di esecuzione del CountingSort
    clock_t start = clock();
    CountingSort(arr, n);
    clock_t end = clock();
    double time_spent = (double)(end - start) / CLOCKS_PER_SEC;

    // Stampa l'array ordinato
    for (int i = 0; i < n; i++) {
      printf("%d ", arr[i]);
    }
    printf("\n");

    // Stampa il tempo di esecuzione
    printf("\n");
    printf("Time spent: %f secondi", time_spent);
    printf("\n");

    return 0;
}
