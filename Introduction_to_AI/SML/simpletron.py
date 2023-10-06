import time

class Simpletron():
    def __init__(self, memory_size = 100):
        self.stop = False
        # Instruction Register
        self.IR = '+0000'
        self.counter = 0

        # Accumulator
        self.ACC = '+0000'

        # Memory
        self.memory_size = memory_size
        self.memory = self.initialize_memory()

        self.operation_code = 0
        self.operand = 0
        self.operation_set = {
            '10': self.Read,
            '11': self.Write,
            '20': self.Load,
            '21': self.Store,
            '30': self.Add,
            '31': self.Subtract,
            '32': self.Divide,
            '33': self.Multiply,
            '40': self.Branch,
            '41': self.BranchNeg,
            '42': self.BranchZero,
            '43': self.Halt
        }
        
    def Read(self):
        self.printText(f'Enter a number into memory address {self.format_two_digital(self.operand)}: ', 0.01 ,end='')
        input_value = input()

        while(not input_value):
            self.printText(f'Enter a number into memory address {self.format_two_digital(self.operand)}: ', 0.01 ,end='')
            input_value = input()

        self.memory[self.operand] = self.format(int(input_value))

    def Write(self):
        self.printText(f'The value of memory address {self.format_two_digital(self.operand)} is {int(self.memory[self.operand])}', 0.01)
        input()

    def Load(self):
        self.ACC = self.memory[self.operand]

    def Store(self):
        self.memory[self.operand] = self.ACC

    def Add(self):
        self.ACC = self.format(int(self.ACC) + int(self.memory[self.operand]))

    def Subtract(self):
        self.ACC = self.format(int(self.ACC) - int(self.memory[self.operand]))

    def Divide(self):
        self.ACC = self.format(int(self.ACC) / int(self.memory[self.operand]))

    def Multiply(self):
        self.ACC = self.format(int(self.ACC) * int(self.memory[self.operand]))

    def Branch(self):
        self.counter = self.operand

    def BranchNeg(self):
        if(int(self.ACC) < 0 ): self.counter = self.operand

    def BranchZero(self):
        if(int(self.ACC) == 0): self.counter = self.operand

    def Halt(self):
        self.stop = True

    def initialize_memory(self):
        arr = []
        for i in range(self.memory_size):
            arr.append('+0000')
        return arr

    def load_code(self, code):
        for index, text in enumerate(code):
            if(text.replace('\n','').replace(' ','') == ''): continue
            code = int(text.replace('\n','').replace(' ','')[0:4])
            self.memory[index] = self.format(code)

    def execute(self):
        """
        Instruction Execution Cycle
        1. Fetch Instruction
        2. Increasement Counter
        3. Decode (Instruction)
        4. Execution
        """
        while(not self.stop):
            # Show the information
            self.show()
            input("Press 'Enter' key to continue...")

            # Fetch Instruction
            self.IR = self.memory[self.counter]

            # Increasement Counter
            self.counter += 1

            # Decode and Execution
            self.decode(self.IR)
            self.execute_by_step()



        self.show()
        input("Press 'Enter' key to continue...")

        self.printText(f'\nThis is the end of the process.', 0.03)
        time.sleep(0.5)
        self.printText(f'Accumulator: {self.ACC}', 0.03)
        self.printText(f'Int: {int(self.ACC)}', 0.03)
        time.sleep(1)
        self.printText('(｡・ω・｡)')
        self.reset()


    def decode(self, code):
        self.operation_code = int(code[1:3])
        self.operand = int(code[3:])
        return self        

    def execute_by_step(self):
        self.operation_set[str(self.operation_code)]()
        return self

    def reset(self):
        self.stop = False
        self.IR = '+0000'
        self.counter = 0
        self.ACC = '+0000'
        self.operation_code = 0
        self.operand = 0
        self.memory = self.initialize_memory()

    def format_two_digital(self, num):
        return format(num, '02')

    def format(self, num):
        if(num == 0): return '+0000'
        if(num > 0):
            return f'+{format(num,"04")}'
        else:
            return f'{format(num,"05")}'

    def show(self):
        # Registers
        counter_symbol = '|'
        Registers = '{:30}'.format("Registers:")
        Accumulator = '{:20}'.format('Accumulator')+'{:>10}'.format((self.ACC))
        Instruction_Counter = '{:20}'.format('Instruction Counter')+'{:>10}'.format(self.format_two_digital(self.counter))
        Instruction_Register ='{:20}'.format('Instruction Register')+'{:>10}'.format(self.format(int(self.IR)))
        Operation_Code = '{:20}'.format('Operation Code')+'{:>10}'.format(self.format_two_digital(self.operation_code))
        Operand = '{:20}'.format('Operand')+'{:>10}'.format(self.format_two_digital(self.operand))
        registers_info = [Registers,'{:30}'.format(''),Accumulator, Instruction_Counter, Instruction_Register, Operation_Code, Operand]
 
        # Memory
        self.printText('{:^30}'.format('')+'{:^80}'.format('Memory'),end='\n\n',slow_mode=True)

        self.printText('{:>30}'.format(''), end='',slow_mode=True)
        self.printText('{:>10}'.format(''), end='',slow_mode=True)
        for i in range(10):
            self.printText('{:>7}'.format(i), end='',slow_mode=True)
        self.printText(slow_mode=True)

        for index, instruction in enumerate(self.memory):
            if((index+1) % 10 == 0):
                self.printText('{:>7}'.format(f'{counter_symbol if self.counter == index else ""}{instruction}'),slow_mode=True)
                if(index+1 == len(self.memory)): continue

                # Print the registers_info 
                if((index+1) // 10 - 1 < len(registers_info)):
                    self.printText(registers_info[(index+1) // 10 -1], end='',slow_mode=True)
                else:
                    self.printText('{:>30}'.format(''), end='',slow_mode=True)
                    
                self.printText('{:>10}'.format(((index+1) // 10)*10), end='',slow_mode=True)

            else:
                if(index == 0): 
                    self.printText('{:>30}'.format(''), end='',slow_mode=True)
                    self.printText('{:>10}'.format((index) // 10), end='',slow_mode=True)
                self.printText('{:>7}'.format(f'{counter_symbol if self.counter == index else ""}{instruction}'), end='',slow_mode=True)
            
        self.printText(slow_mode=True)
        return self
    
    def printText(self, str = '', delta=0.0001, end='\n', slow_mode=True):
        """
        Print the string character by character. (optional)
        """
        if(slow_mode):
            for i in str:
                # print each character by the delta time
                time.sleep(delta)
                print(i, end='')
            print(end=end)
        else:
            print(str,end=end)
        
        return self

def readFile(path):
    lines = []
    f = open(path)
    for line in f.readlines():
        lines.append(line)
    f.close()
    return lines

def executeCodeByPath(path):
    code = readFile(path)
    simpletron.load_code(code)
    simpletron.execute()
    

simpletron = Simpletron()
path = input('Enter file path: ')

while(True):
    
    while(path == ''):
        path = input('Next file path (enter "q" can quit): ')
    executeCodeByPath(path)
    path = input('Next file path (enter "q" can quit): ')
    if(path == 'q' or path == 'quit' ): break

