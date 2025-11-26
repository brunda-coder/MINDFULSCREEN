class SystemManager:
    def __init__(self):
        self.systems = {}

    def register_system(self, name, system):
        self.systems[name] = system
        print(f"[SystemManager] Registered system: {name}")

    def get_system(self, name):
        return self.systems.get(name)

    def start_all(self):
        for name, system in self.systems.items():
            if hasattr(system, "start"):
                print(f"[SystemManager] Starting {name}...")
                system.start()
