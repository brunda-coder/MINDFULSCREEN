class EventBus:
    def __init__(self):
        self.listeners = {}

    def subscribe(self, event, callback):
        self.listeners.setdefault(event, []).append(callback)

    def publish(self, event, data=None):
        if event in self.listeners:
            for callback in self.listeners[event]:
                callback(data)

