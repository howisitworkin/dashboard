#include <stdio.h>
#include <stdlib.h>

int compute_even_sum(int n) {
    int sum = 0;
    for (int i = 1; i <= n; i++) {
        if (i % 2 == 0)
            sum += i;
    }
    return sum;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <N>\n", argv[0]);
        return 1;
    }
    int n = atoi(argv[1]);
    printf("Even Sum (1..%d) = %d\n", n, compute_even_sum(n));
    return 0;
}

