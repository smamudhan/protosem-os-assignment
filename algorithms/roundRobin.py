def waitingTime(n, b_t, w_t, quantum):
	rem_b_t = [0] * n

	for i in range(n):
		rem_b_t[i] = b_t[i]

	t = 0 

	while(1):
		done = True

		for i in range(n):
			if (rem_b_t[i] > 0) :
				done = False 
				
				if (rem_b_t[i] > quantum) :
					t += quantum
					rem_b_t[i] -= quantum
				
				else:
					t = t + rem_b_t[i]
					w_t[i] = t - b_t[i]
					rem_b_t[i] = 0
				
		if (done == True):
			break
			
def turnaroundTime(n, b_t, w_t, ta_t):
	for i in range(n):
		ta_t[i] = b_t[i] + w_t[i]


def avgTime(n, b_t, quantum):
	w_t = [0] * n
	ta_t = [0] * n

	waitingTime(n, b_t, w_t, quantum)

	turnaroundTime(n, b_t, w_t, ta_t)

	total_w_t = 0
	total_ta_t, temp = 0, [0] * n
	for i in range(n):
		total_w_t = total_w_t + w_t[i]
		total_ta_t = total_ta_t + ta_t[i]
		temp[i] = {"burst":b_t[i], "wait":w_t[i], "turnaround":ta_t[i]}

	rr = {"algorithm":"Round Robin", "Quantum":quantum, "avg_wt":total_w_t /n, "avg_tat":total_ta_t / n}
	for i in range(len(temp)):
		rr[str(i + 1)] = temp[i]
	return rr

def main():	
	n = 4
	burst_time = [5, 12, 23, 32]
	quantum = 5
	return(avgTime(n, burst_time, quantum))

if __name__ =="__main__":
	main()