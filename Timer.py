import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer , end="\r")
        time.sleep(1)
        t -= 1
    print("\n\n**********\nTime's up!\n**********\n")
#main Fun^x
Duration= int(input("Enter the duration in seconds: ")) 
print(f"your timer for {Duration} second is started")
countdown(Duration)