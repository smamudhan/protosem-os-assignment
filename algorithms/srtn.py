def waitingTime(processes, n, w_t):
	r_t = [0] * n

	for i in range(n):
		r_t[i] = processes[i][1]
	complete = 0
	
	t = 0
	minm = 999999999
	short = 0
	check = False

	while (complete != n):
		
		for j in range(n):
			if ((processes[j][2] <= t) and (r_t[j] < minm) and r_t[j] > 0):
				minm = r_t[j]
				short = j
				check = True

		if (check == False):
			t += 1
			continue
			
		r_t[short] -= 1

		minm = r_t[short]
		if (minm == 0):
			minm = 999999999

		if (r_t[short] == 0):

			complete += 1
			check = False

			fint = t + 1

			w_t[short] = (fint - processes[short][1] - processes[short][2])

			if (w_t[short] < 0):
				w_t[short] = 0
		
		t += 1

def turnaroundTime(processes, n, w_t, ta_t):
	for i in range(n):
		ta_t[i] = processes[i][1] + w_t[i]

def avgTime(processes, n):
	w_t = [0] * n
	ta_t = [0] * n

	waitingTime(processes, n, w_t)

	turnaroundTime(processes, n, w_t, ta_t)

	total_w_t = 0
	total_ta_t = 0
	temp = [0] * n
	for i in range(n):
		total_w_t = total_w_t + w_t[i]
		total_ta_t = total_ta_t + ta_t[i]
		temp[i] = {"burst":processes[i][1], "wait":w_t[i], "tat": ta_t[i]}

	srtn = {"algorithm":"srtn", "avg_wt":total_w_t /n, "avg_tat":total_ta_t / n}
	for i in range(len(temp)):
		srtn[str(i + 1)] = temp[i]
	return srtn

def main():	
	proc = [[1, 5, 2], [2, 12, 1], [3, 32, 6], [4, 23, 4]]
	n = 4
	return(avgTime(proc, n))

if __name__ =="__main__":
	main()