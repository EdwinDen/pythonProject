import time
import random

class Neighbor:
    def __init__(self, name):
        self.name = name
        self.hello_failures = 0

    def send_hello(self):
        print(f"Sending hello to {self.name}")
        # Simulate a network failure/success
        return random.choice([True, False])

    def handle_response(self, response):
        if response:
            print(f"Received I.H.U from {self.name}")
            self.hello_failures = 0
        else:
            print(f"Failed to receive I.H.U from {self.name}")
            self.hello_failures += 1

    def is_dead(self):
        if self.hello_failures > 3:
            print(f"{self.name} is OFFLINE")
            return True
        return False

def main():
    neighbor = Neighbor("Zamtel")

    while True:
        response = neighbor.send_hello()
        neighbor.handle_response(response)
        if neighbor.is_dead():
            print(f"Stopping communication with {neighbor.name}")
            break
        time.sleep(1)

if __name__ == '__main__':
    main()