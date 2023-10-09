#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

#define MAX_THREADS 4

pthread_mutex_t mutex;
pthread_cond_t conds[MAX_THREADS];
pthread_t threads[MAX_THREADS];
int done[MAX_THREADS];

// maximum number of elements in the common array

#define MAX_ELEM 1000

// common array shared to all threads

int arr[MAX_ELEM];

// pointer to the next element in the common array

int next = 0;

// thread function to update the common array

void check_all_done()
{
    for (int i= 0; i < MAX_THREADS; i++)
    {
        if (done[i] == 0)
            return;
    }
    for (int j= 0; j < MAX_THREADS; j++)
    {
        done[j] = 0;
        pthread_cond_signal(&conds[j]);
    }
}

void *thread_update(void *arg)
{
    int tid;

    tid = *(int *)arg;

    while (next < MAX_ELEM)
    {
        pthread_mutex_lock(&mutex);
        // wait for all other threads to finish, then proceed.
        // No starvation!
        while (done[tid] == 1)
            pthread_cond_wait(&conds[tid], &mutex);
        if (next >= MAX_ELEM) {
            done[tid] = 1;
        }
        else
        {
            // update array
            printf("%d %d\n", next, tid);
            arr[next++] = tid;
            // this thread mark itself as done
            done[tid] = 1;
        }
        check_all_done();
        pthread_mutex_unlock(&mutex);
    }
}

int main()
{

    pthread_mutex_init(&mutex, NULL);

    for (int i= 0; i < MAX_THREADS; i++)
        done[i] = 0;

    for (int tid = 0; tid < MAX_THREADS; tid++)
    {
        int *arg = malloc(sizeof(int));

        *arg = tid;
        pthread_cond_init(&conds[tid], NULL);
        pthread_create(&threads[tid], NULL, thread_update, arg);
    }

    for (int tid = 0; tid < MAX_THREADS; tid++)
        pthread_join(threads[tid], NULL);

    printf("DONE\n");


    FILE *fptr;
    fptr = fopen("test.txt", "w");
    for (int k = 0; k < MAX_ELEM; k++)
       fprintf(fptr, "%d", arr[k]);
    fclose(fptr);
}
