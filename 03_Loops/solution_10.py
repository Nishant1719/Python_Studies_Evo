# Problem: Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.
import time

max_tries = 5
attempts = 1
wait_time = 1

while attempts <= max_tries:
    print(f"Attempts {attempts} - wait time {wait_time}")
    time.sleep(wait_time)
    wait_time *= 2
    attempts+=1
    
