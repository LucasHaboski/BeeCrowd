#include <stdio.h>

int main() {
    int n;

    while (1) {
        scanf("%d", &n);  // Lê o número de cartas

        if (n == 0) break;  // Encerra o loop se o número de cartas for 0

        int deck[n], discarded[n - 1];  // Array para o baralho e para as cartas descartadas
        int discardCount = 0;           // Contador de cartas descartadas

        // Inicializa o baralho com as cartas de 1 a n
        for (int i = 0; i < n; i++) {
            deck[i] = i + 1;
        }

        int front = 0, rear = n - 1;  // Índices para o início e o final da fila

        // Simula o processo de descarte
        while (front < rear) {
            discarded[discardCount++] = deck[front];  // Armazena a carta descartada
            front++;                                  // Remove a carta do topo

            // Move a próxima carta para o final
            deck[rear + 1] = deck[front];
            rear++;
            front++;
        }

        // Exibe as cartas descartadas
        printf("Discarded cards:");
        for (int i = 0; i < discardCount; i++) {
            printf(" %d", discarded[i]);
            if (i < discardCount - 1) printf(",");
        }
        printf("\n");

        // Exibe a última carta restante
        printf("Remaining card: %d\n", deck[front]);
    }

    return 0;
}
