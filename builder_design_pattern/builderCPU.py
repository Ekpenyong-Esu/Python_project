# Product
class Computer:
    def __init__(self, CPU, RAM, storage, GPU):
        self.CPU = CPU
        self.RAM = RAM
        self.storage = storage
        self.GPU = GPU

# Builder interface
class ComputerBuilder:
    def build_CPU(self):
        pass

    def build_RAM(self):
        pass

    def build_storage(self):
        pass

    def build_GPU(self):
        pass

    def get_computer(self):
        pass

# Concrete builder
class HighEndComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = Computer(None, None, None, None)

    def build_CPU(self):
        self.computer.CPU = "High-end CPU"

    def build_RAM(self):
        self.computer.RAM = "32GB RAM"

    def build_storage(self):
        self.computer.storage = "1TB SSD"

    def build_GPU(self):
        self.computer.GPU = "NVIDIA RTX 3080"

    def get_computer(self):
        return self.computer

# Director
class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct_computer(self):
        self.builder.build_CPU()
        self.builder.build_RAM()
        self.builder.build_storage()
        self.builder.build_GPU()

# Client code
if __name__ == "__main__":
    high_end_builder = HighEndComputerBuilder()
    director = Director(high_end_builder)

    director.construct_computer()
    high_end_computer = high_end_builder.get_computer()

    print("High-end Computer:")
    print(f"CPU: {high_end_computer.CPU}")
    print(f"RAM: {high_end_computer.RAM}")
    print(f"Storage: {high_end_computer.storage}")
    print(f"GPU: {high_end_computer.GPU}")
