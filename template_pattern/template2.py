class AbstractClass:
    def template_method(self):
        self.common_operation1()
        self.specialized_operation1()
        self.common_operation2()
        self.specialized_operation2()

    def common_operation1(self):
        print("AbstractClass: Common Operation 1")

    def common_operation2(self):
        print("AbstractClass: Common Operation 2")

    def specialized_operation1(self):
        raise NotImplementedError("Subclasses must implement specialized_operation1")

    def specialized_operation2(self):
        raise NotImplementedError("Subclasses must implement specialized_operation2")


class ConcreteClass1(AbstractClass):
    def specialized_operation1(self):
        print("ConcreteClass1: Specialized Operation 1")

    def specialized_operation2(self):
        print("ConcreteClass1: Specialized Operation 2")


class ConcreteClass2(AbstractClass):
    def specialized_operation1(self):
        print("ConcreteClass2: Specialized Operation 1")

    def specialized_operation2(self):
        print("ConcreteClass2: Specialized Operation 2")


def client_code(abstract_class):
    abstract_class.template_method()


if __name__ == "__main__":
    print("Client code with ConcreteClass1:")
    concrete_class1 = ConcreteClass1()
    client_code(concrete_class1)

    print("\nClient code with ConcreteClass2:")
    concrete_class2 = ConcreteClass2()
    client_code(concrete_class2)
