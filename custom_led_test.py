from machine import Pin
import utime


strip = Pin(10, Pin.OUT)

print("Starting isolated LED strip test...")
print("The blue 3-LED strip should flash once per second.")
print("Press Ctrl+C in Thonny to stop the test safely.")

try:
    while True:
        strip.value(1)  
        utime.sleep(1.0)   
        
        strip.value(0)  
        utime.sleep(1.0)    

except KeyboardInterrupt:
    
    strip.value(0)

