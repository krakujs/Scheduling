def find_waiting_time(processes, bt, wt, quantum, n):
    pending_bt = [0] * n
    i = 0
    while (i < n):
        pending_bt[i] = bt[i]
        i += 1
    process_time = 0
    work = True
    while (work == True):
        work = False
        i = 0
        while i < n:
            if pending_bt[i] > 0:
                work = True
                if pending_bt[i] > quantum:
                    process_time += quantum
                    pending_bt[i] -= quantum
                else:
                    process_time = process_time + pending_bt[i]
                    wt[i] = process_time - bt[i]
                    pending_bt[i] = 0
            i += 1


class RoundRobin:

    def find_avg_time(self, processes, burst_time, quantum, n):
        turnaround_time = [0] * n
        waiting_time = [0] * n
        total_waiting_time = 0
        total_turnaround_time = 0
        i = 0
        find_waiting_time(processes, burst_time, waiting_time, quantum, n)
        while (i < n):
            turnaround_time[i] = burst_time[i] + waiting_time[i]
            i += 1
        print(" (Process) (Burst Time) (Waiting Time) (Turn Around Time)", end="")
        i = 0
        while (i < n):
            total_waiting_time += waiting_time[i]
            total_turnaround_time += turnaround_time[i]
            print("\n p", processes[i], " \t\t", burst_time[i], " \t\t", waiting_time[i], " \t\t", turnaround_time[i],
                  end="")
            i += 1
        print("\n Average Waiting Time : ", (total_waiting_time / n))
        print(" Average Turn Around Time : ", (total_turnaround_time / n))


def main():
    obj = RoundRobin()
    processes = [1, 2, 3, 4]
    burst_time = [4, 3, 5, 9]
    n = len(processes)
    quantum = 2
    obj.find_avg_time(processes, burst_time, quantum, n)


if __name__ == "__main__":
    main()
