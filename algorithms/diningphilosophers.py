import threading
import time

results = {}
counter = 1

class Philosopher(threading.Thread):
 
    running = True
 
    def __init__(self, xname, forkOnLeft, forkOnRight):
        threading.Thread.__init__(self)
        self.name = xname
        self.forkOnLeft = forkOnLeft
        self.forkOnRight = forkOnRight
 
    def run(self):
        while(self.running):
            time.sleep(2)
            global results, counter
            results[counter] = ('%s is hungry.' % self.name)
            counter += 1
            self.dine()
 
    def dine(self):
        fork1, fork2 = self.forkOnLeft, self.forkOnRight
 
        while self.running:
            fork1.acquire(True)
            locked = fork2.acquire(False)
            if locked: break
            fork1.release()
            global results, counter
            results[counter] = ('%s swaps forks' % self.name)
            counter += 1
            fork1, fork2 = fork2, fork1
        else:
            return
 
        self.dining()
        fork2.release()
        fork1.release()
 
    def dining(self):
        global results, counter
        results[counter] = ('%s starts eating '% self.name)
        counter += 1
        time.sleep(2)
        results[counter] = ('%s finishes eating and leaves to think.' % self.name)
        counter += 1
 
def DiningPhilosophers():
    forks = [threading.Lock() for n in range(3)]
    philosopherNames = ('Sudharson', 'Adithya', 'Amudhan')
 
    philosophers= [Philosopher(philosopherNames[i], forks[i%3], forks[(i+1)%3]) \
            for i in range(3)]
 
    Philosopher.running = True
    for p in philosophers: p.start()
    time.sleep(10)
    Philosopher.running = False
    global results, counter
    results[counter] = ("Now we're finishing.")
    counter += 1

def main():
    DiningPhilosophers()
    return(results)

if __name__ == "__main__":
    main()