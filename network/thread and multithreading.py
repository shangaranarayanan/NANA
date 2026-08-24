import threading, time
'''
def shihan(brand):
    for x in range(3):
        print(f"{brand}, S.No. {x+1}")
        time.sleep(5)
thread_1 = threading.Thread(target=shihan, args=("peaky blinders",))

thread_1.start()
thread_1.join()  
'''

'''
def movies(name):
    for x in range(1):
        print(f"{name}, S.No. {x+1}")
        time.sleep(3)
thread_1 = threading.Thread(target=movies, args=("peaky blinders",))
thread_2 = threading.Thread(target=movies, args=("the odyssey",))
thread_1.start()
thread_1.join()  

thread_2.start()
thread_2.join()  
'''

def movies(name):
    for x in range(2):
        print(f"{name}, S.No. {x+1}")
        time.sleep(3)
thread_1 = threading.Thread(target=movies, args=("peaky blinders",))
thread_2 = threading.Thread(target=movies, args=("the odyssey",))
thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()


