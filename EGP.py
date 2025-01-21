import time
import random


class Router:
    def __init__(self, name, as_number):
        self.name = name
        self.as_number = as_number
        self.neighbors = []
        self.routing_table = {}
        self.hello_failures = {}
        self.poll_failures = {}
        self.hello_interval = 5  # seconds
        self.poll_interval = 10  # seconds

    def initialize_routing_table(self, directly_connected_networks):
        for network in directly_connected_networks:
            self.routing_table[network] = {
                "next_hop": None,
                "distance": 1,
                "neighbor_as": self.as_number,
                "status": "active",
            }
        print(f"{self.name} initialized routing table: {self.routing_table}")
        time.sleep(1)

    def attempt_establish_neighbor(self, neighbor_router):
        hello_response = self.send_hello(neighbor_router)
        if hello_response:
            self.neighbors.append(neighbor_router)
            self.hello_failures[neighbor_router.name] = 0
            self.poll_failures[neighbor_router.name] = 0

    def send_hello(self, neighbor):
        print(f"{self.name} sending HELLO to {neighbor.name}")
        time.sleep(1)
        return random.choice([True, False])

    def handle_hello_response(self, neighbor, response):
        if response:
            print(f"{self.name} received I.H.U from {neighbor.name}")
            self.hello_failures[neighbor.name] = 0
        else:
            print(f"{self.name} failed to receive I.H.U from {neighbor.name}")
            self.hello_failures[neighbor.name] += 1
        time.sleep(1)

    def send_poll(self, neighbor):
        print(f"{self.name} sending POLL to {neighbor.name}")
        time.sleep(1)
        return neighbor.respond_to_poll()

    def respond_to_poll(self):
        reachable_networks = {
            network: info["distance"]
            for network, info in self.routing_table.items()
            if info["status"] == "active"
        }
        print(
            f"{self.name} responding to POLL with reachable networks: {reachable_networks}"
        )
        time.sleep(1)
        return reachable_networks

    def handle_poll_response(self, neighbor, response):
        if response:
            print(f"{self.name} received UPDATE from {neighbor.name}")
            self.poll_failures[neighbor.name] = 0
            self.update_routing_table(neighbor, response)
        else:
            print(f"{self.name} failed to receive UPDATE from {neighbor.name}")
            self.poll_failures[neighbor.name] += 1
        time.sleep(1)

    def update_routing_table(self, neighbor, received_routes):
        for network, metric in received_routes.items():
            if (
                network not in self.routing_table
                or self.routing_table[network]["distance"] > metric + 1
            ):
                self.routing_table[network] = {
                    "next_hop": neighbor.name,
                    "distance": metric + 1,
                    "neighbor_as": neighbor.as_number,
                    "status": "active",
                }
        print(f"{self.name} updated routing table: {self.routing_table}")
        time.sleep(1)

    def notify_neighbors(self, unreachable_network):
        for neighbor in self.neighbors:
            print(
                f"{self.name} notifying {neighbor.name} that {unreachable_network} is unreachable."
            )
            neighbor.remove_unreachable_route(unreachable_network)
            time.sleep(1)

    def remove_unreachable_route(self, unreachable_network):
        if unreachable_network in self.routing_table:
            print(
                f"{self.name} removing unreachable route {unreachable_network} from routing table."
            )
            del self.routing_table[unreachable_network]
            print(f"{self.name} updated routing table: {self.routing_table}")
            time.sleep(1)

    def check_neighbors(self):
        for neighbor in self.neighbors:
            if (
                self.hello_failures[neighbor.name] > 3
                or self.poll_failures[neighbor.name] > 3
            ):
                print(f"{neighbor.name} is considered unreachable by {self.name}")
                self.neighbors.remove(neighbor)
                print(f"{self.name} removed {neighbor.name} from neighbors")
                # Mark routes through this neighbor as invalid and notify neighbors
                for network, info in list(self.routing_table.items()):
                    if info["next_hop"] == neighbor.name:
                        self.notify_neighbors(network)
                        del self.routing_table[network]
                print(f"{self.name} updated routing table: {self.routing_table}")
                time.sleep(1)


def main():
    routerA = Router("RouterA", 1)
    routerB = Router("RouterB", 2)
    routerC = Router("RouterC", 3)

    routerA.initialize_routing_table(["192.168.1.0/24", "192.168.2.0/24"])
    routerB.initialize_routing_table(["192.168.3.0/24", "192.168.4.0/24"])
    routerC.initialize_routing_table(["192.168.5.0/24", "192.168.6.0/24"])

    routerA.attempt_establish_neighbor(routerB)
    routerB.attempt_establish_neighbor(routerA)

    routerA.attempt_establish_neighbor(routerC)
    routerC.attempt_establish_neighbor(routerA)

    routerB.attempt_establish_neighbor(routerC)
    routerC.attempt_establish_neighbor(routerB)

    while True:
        for router in [routerA, routerB, routerC]:
            for neighbor in router.neighbors:
                hello_response = router.send_hello(neighbor)
                router.handle_hello_response(neighbor, hello_response)

                if hello_response:
                    poll_response = router.send_poll(neighbor)
                    router.handle_poll_response(neighbor, poll_response)

            router.check_neighbors()

        time.sleep(routerA.hello_interval)


if __name__ == "__main__":
    main()
