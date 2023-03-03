class RouteEntity:
    origin: str
    destination: str
    travel_time: int

    def __init__(self, origin, destination, travel_time):
        self.origin = origin
        self.destination = destination
        self.travel_time = travel_time
