import time

class Simpletron():
    def __init__(self, memory_size = 100):
        # Instruction Register
        self.IR = '+0000'
        self.counter = 0

        # Accumulator
        self.ACC = 0

        # Memory
        self.memory_size = memory_size
        self.memory = self.initialize_memory()

        self.operation_code = 0
        self.operand = 0



    def initialize_memory(self):
        arr = []
        for i in range(self.memory_size):
            arr.append('+0000')
        return arr

    def load_code(self, code):
        for index, text in enumerate(code):
            code = int(text.replace('\n','').replace(' ',''))
            self.memory[index] = self.format(code)

    def format(self, num):
        if(num == 0): return '+0000'
        sign = '+' if num > 0 else ''
        return f'{sign}{format(num,"04")}'
        
    def ex(self):
        return self

    def show(self):

        # Registers
        
        Registers = '{:30}'.format("Registers:")
        Accumulator = '{:20}'.format('Accumulator')+'{:>10}'.format(self.format(self.ACC))
        Instruction_Counter = '{:20}'.format('Instruction Counter')+'{:>10}'.format(format(self.counter,'02'))
        Instruction_Register ='{:20}'.format('Instruction Register')+'{:>10}'.format(self.format(int(self.IR)))
        Operation_Code = '{:20}'.format('Operation Code')+'{:>10}'.format(format(self.operation_code,'02'))
        Operand = '{:20}'.format('Operand')+'{:>10}'.format(format(self.operand,'02'))
        registers_info = [Registers,'{:30}'.format(''),Accumulator, Instruction_Counter, Instruction_Register, Operation_Code, Operand]
 
        # Memory
        self.printText('{:^30}'.format('')+'{:^80}'.format('Memory'),end='\n\n')

        self.printText('{:>30}'.format(''), end='')
        self.printText('{:>10}'.format(''), end='')
        for i in range(self.memory_size // 10):
            self.printText('{:>7}'.format(i), end='')
        self.printText()

        for index, code in enumerate(self.memory):
            if((index+1) % 10 == 0):
                self.printText('{:>7}'.format(code))
                if(index+1 == len(self.memory)): continue

                # Print the registers_info 
                if((index+1) // 10 - 1 < len(registers_info)):
                    self.printText(registers_info[(index+1) // 10 -1], end='')
                else:
                    self.printText('{:>30}'.format(''), end='')
                    
                self.printText('{:>10}'.format(((index+1) // 10)*10), end='')

            else:
                if(index == 0): 
                    self.printText('{:>30}'.format(''), end='')
                    self.printText('{:>10}'.format((index) // 10), end='')
                self.printText('{:>7}'.format(code), end='')
            
        self.printText()
    
    def printText(self, str = '', delta=0.000, end='\n', normal_mode=True):
        """
        Print the string character by character.
        """
        if(normal_mode):
            for i in str:
                # print each character by the delta time
                time.sleep(delta)
                print(i, end='')
            print(end=end)
        else:
            print(str,end=end)

def readFile(path):
    lines = []
    f = open(path)
    for line in f.readlines():
        lines.append(line)
    f.close()
    return lines

path = 'sample.txt'
code = readFile(path)

simpletron = Simpletron(100)
simpletron.load_code(code)
simpletron.show()


