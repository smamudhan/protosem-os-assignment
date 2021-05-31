def waiting_time(n, b_t, a_t):
    service_time = [0] * n
    service_time[0] = 0
    w_t = [0] * n
    w_t[0] = 0
    
    for i in range(1, n):
        service_time[i] = service_time[i - 1] + b_t[i - 1]
        w_t[i] = service_time[i] - a_t[i]
        if (w_t[i] < 0):
            w_t[i] = 0

    return w_t

def turnaroundTime(n, b_t, w_t):
    ta_t = [0] * n

    for i in range(n):
        ta_t[i] = b_t[i] + w_t[i]
    
    return ta_t

def avgTime(n, b_t, a_t):
    w_t = waiting_time(n, b_t, a_t)
    ta_t = turnaroundTime(n, b_t, w_t)    
    total_w_t = 0
    total_ta_t = 0
    
    temp = [0] * n
    for i in range(n):
        total_w_t = total_w_t + w_t[i]
        total_ta_t = total_ta_t + ta_t[i]
        compl_time = ta_t[i] + a_t[i]
        temp [i] =  {"burst":b_t[i], "arrival":a_t[i], "wait":w_t[i], "turnaround":ta_t[i], "completion":compl_time}
    fcfs = {"algorithm":"fcfs", "avg_wt":total_w_t /n, "avg_tat":total_ta_t / n}
    for i in range(len(temp)):
        fcfs[str(i+1)] = temp[i]
    return fcfs

def main():
    n = 4
    b_t = [5, 12, 32, 23]
    a_t = [2, 1, 6, 4]
    
    return(avgTime(n, b_t, a_t))

if __name__ =="__main__":
    main()