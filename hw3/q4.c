#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <pthread.h> //breaks on windows use wsl/linux or installpthread somehow

#define MILLION 1000000
#define ATTEMPT_CONST 100
#define NUM_THREADS ATTEMPT_CONST

int successes = 0;
pthread_mutex_t lock;

void *millionAttempts(void *arg) {
    int succ = 0;
    for (int i = 0; i < MILLION; ++i) {
        for (int j = 0; j < 6; ++j) {
            if ((rand() % 6) + 1 == 6) {
                succ++;
                break;
            }
        }
    }
    pthread_mutex_lock(&lock);
    successes += succ;
    pthread_mutex_unlock(&lock);
    printf("Thread done\n");
    return NULL;
}

int main() {
    srand(time(NULL));
    pthread_t threads[NUM_THREADS];
    pthread_mutex_init(&lock, NULL);

    for (int i = 0; i < NUM_THREADS; ++i) {
        if (pthread_create(&threads[i], NULL, millionAttempts, NULL) != 0) {
            perror("Failed to create thread");
        }
    }

    for (int i = 0; i < NUM_THREADS; ++i) {
        if (pthread_join(threads[i], NULL) != 0) {
            perror("Failed to join thread");
        }
    }

    pthread_mutex_destroy(&lock);

    printf("Total successes: %d\n", successes);
    return 0;
}

