# Target interface 
class Target:
  def request(self):
    return "Target: The default target's behavior."

# Adaptee 
class Adaptee:
  def specific_request(self):
    return ".eetpadA eht fo roivaheb laicepS"

# Adapter 
class Adapter(Target):
  def __init__(self, adaptee):
    self.adaptee = adaptee
  
  def request(self):
    return f"Adapter: (TRANSLATED) {self.adaptee.specific_request()[::-1]}"
  
# Client
def client_code(target):
  print(target.request(), end="")

# Create objects
adaptee = Adaptee() 
adapter = Adapter(adaptee)
target = Target()

# Client calls
client_code(target)
print("\n")
client_code(adapter)