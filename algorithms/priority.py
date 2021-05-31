def waitingTime(processes, n, w_t):
    w_t[0] = 0

    for i in range(1, n):
        w_t[i] = processes[i - 1][1] + w_t[i - 1]


def turnaroundTime(processes, n, w_t, ta_t):

    for i in range(n):
        ta_t[i] = processes[i][1] + w_t[i]


def avgTime(processes, n, priority):
    w_t = [0] * n
    ta_t = [0] * n

    waitingTime(processes, n, w_t)

    turnaroundTime(processes, n, w_t, ta_t)
    total_w_t = 0
    total_ta_t, temp = 0, [0] * n
    for i in range(n):

        total_w_t = total_w_t + w_t[i]
        total_ta_t = total_ta_t + ta_t[i]
        temp[i] = {
            "burst": processes[i][1],
            "wait": w_t[i],
            "turnaround": ta_t[i]
        }

    priority["avg_wt"] = total_w_t / n
    priority["avg_tat"] = total_ta_t / n
    for i in range(len(temp)):
        priority[str(i + 1)] = temp[i]
    return priority


def priorityScheduling(proc, n):

    proc = sorted(proc, key=lambda proc: proc[2], reverse=True)

    priority = {"algorithm": "priority"}
    execorder = ""
    for i in proc:
        execorder += str(i[0]) + " "
    priority["exec_order"]=execorder
    return avgTime(proc, n, priority)

def main():
    proc = [[1, 5, 2], [2, 12, 1], [3, 23, 6], [4, 32, 4]]
    n = 4
    return(priorityScheduling(proc, n))

if __name__ =="__main__":
    main()