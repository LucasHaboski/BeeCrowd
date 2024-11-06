#include <stdio.h>

int main() {
    int n;

    while (1) {
        scanf("%d", &n);  

        if (n == 0) break;  

        int heights[n];
        for (int i = 0; i < n; i++) {
            scanf("%d", &heights[i]);  
        }

        int peaks = 0;

        
        for (int i = 0; i < n; i++) {
            int prev = (i - 1 + n) % n;  
            int next = (i + 1) % n;       

            
            if ((heights[i] > heights[prev] && heights[i] > heights[next]) ||
                (heights[i] < heights[prev] && heights[i] < heights[next])) {
                peaks++;
            }
        }

        printf("%d\n", peaks);  
        }

    return 0;
}