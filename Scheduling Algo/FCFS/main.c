#include<stdio.h>
#define maxTime 30
void main(){

    int no_of_process = 0;
    int burstTime[maxTime];
    int waitingTime[maxTime];
    int turnAroundTime[maxTime];

    float avgWaitingTime = 0;
    float avgTurnAroundTime = 0;

    printf("Enter the Number of Process = ");
    scanf("%d", &no_of_process);

    printf("Enter the Burst Time = ");
    for(int i=0; i<no_of_process; i++){
        scanf("%d", &burstTime[i]);
    }

    printf("process\tburst_time\twaiting_time\tturn_around_time\n");
    for(int i=0; i<no_of_process; i++){
        waitingTime[i] = 0;
        turnAroundTime[i] = 0;
        for(int j=0; j<i; j++){
            waitingTime[i] = waitingTime[i] + burstTime[j];
        }
        turnAroundTime[i] = waitingTime[i] + burstTime[i];
        avgWaitingTime = avgWaitingTime + waitingTime[i];
        avgTurnAroundTime = avgTurnAroundTime + turnAroundTime[i];
        printf("%d\t%d\t\t%d\t\t%d\n", i+1, burstTime[i], waitingTime[i], turnAroundTime[i]);
    }
    avgWaitingTime = avgWaitingTime/no_of_process;
    avgTurnAroundTime = avgTurnAroundTime/no_of_process;
    printf("Average waiting Time = %f\n", avgWaitingTime);  
    printf("Average Turn Around Time = %f\n4", avgTurnAroundTime);

}