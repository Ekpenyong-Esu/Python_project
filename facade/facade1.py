# Complex subsystem
class CPU:
  def process(self):
    print("CPU processing...")
    
class Memory:
  def load(self):
    print("Loading memory...")

class HardDrive:
  def read(self):
    print("Reading from hard drive...")
      
# Facade     
class ComputerFacade:
  def __init__(self):
    self.cpu = CPU()
    self.memory = Memory()
    self.hard_drive = HardDrive()

  def start(self):
    self.cpu.process()
    self.memory.load()
    self.hard_drive.read()

# Client 
facade = ComputerFacade()
facade.start()