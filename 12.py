class Car:
    def __init__(self, gas_level):
        self.gas_level = gas_level
        self.gas_level = ''
    
    def add_gas(self, additional_gas):
        self.additional_gas = additional_gas
        self.new_gas_level = self.gas_level + self.additional_gas
        return self.new_gas_level
        
    
    def fill_up(self):
        if self.add_gas(self.gas_level) < 13.0:
            return 13.0 - self.gas_level
        else:
            return 0


# some tests to check your code, Do Not Post These in Vocareum

