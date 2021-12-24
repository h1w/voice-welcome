import threading

total = 0
lock = threading.Lock()

def update_total(amount):
    global total

    with lock:
        total += amount
    
    print(total)

for i in range(10):
    my_thread = threading.Thread(target=update_total, args=(5, ))
    my_thread.start()