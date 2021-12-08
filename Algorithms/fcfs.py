def Cal(arrival_time, burst_time, N):
    waiting_time = [0] * N;
    waiting_time[0] = 0;

    print("P.No.\tArrival Time\t", "Burst Time\tWaiting Time");
    print("1", "\t\t", arrival_time[0], "\t\t", burst_time[0], "\t\t", waiting_time[0]);

    for i in range(1, 5):
        waiting_time[i] = (arrival_time[i - 1] + burst_time[i - 1] + waiting_time[i - 1]) - arrival_time[i];
        print(i + 1, "\t\t", arrival_time[i], "\t\t", burst_time[i], "\t\t", waiting_time[i]);

    average = 0.0;
    sum = 0;
    for i in range(5):
        sum = sum + waiting_time[i];
    average = sum / 5;
    print("Average waiting time = ", average);


if __name__ == '__main__':
    N = 5;
    Arrival_time = [0, 1, 2, 3, 4];
    burst_time = [4, 3, 1, 2, 5];
    Cal(Arrival_time, burst_time, N);
