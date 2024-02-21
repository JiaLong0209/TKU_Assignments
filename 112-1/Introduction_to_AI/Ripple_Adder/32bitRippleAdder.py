
class RippleAdder():

    def __init__(self, size = 8):
        self.size = size
        self.A = self.B = [0 for i in range(size+1)]

    def to_binary_array(self, n):
        binary_array = [int(i) for i in bin(n)[-self.size:].replace('b','')]
        while(binary_array.__len__() - self.size): binary_array.insert(0,0)
        return binary_array

    def HA(self, x, y, s, c):
        return [x,y,x^y, x&y]

    def FA(self, x, y, z, s, c):
        s1 = s2 = c1 = c2 = 0
        temp1 = self.HA(x,y,s1,c1)                # x y s1 c1
        temp2 = self.HA(temp1[2],z,s2,c2)         # s1 z s2 c2
        return [x,y,z,temp2[2],temp1[3]|temp2[3]] # x, y, z, s2, c1 or c2

    def toString(self, arr):
        string = ''.join([str(arr[i])+(" " if not(i+1)%4 else "") for i,v in enumerate(arr)])
        return string

    def read_number(self):
        prompt = f'Input number (0~{2**(self.size)-1}):\n'
        self.A = self.to_binary_array(int(input(prompt)));
        print(f"A = {self.toString(self.A)}")
        print()
        self.B = self.to_binary_array(int(input(prompt)));
        print(f"B = {self.toString(self.B)}")
        
    def calculate(self):
        bits = [0,0,0,0,0]
        self.C = [0 for i in range(self.size)]
        self.S = [0 for i in range(self.size)]
        self.Cout = 0
        for i in range(self.size-1, -1, -1):
            bits = self.FA(self.A[i], self.B[i], self.C[i], self.S[i], self.C[i-1])
            if i == 0 :
                self.Cout = bits[4]
            else:
                self.C[i-1] = bits[4]
            self.S[i] = bits[3]
            # print(i, bits)


        print()
        print(f'Sum = {self.S[0]}')
        print(f'Carry = {self.Cout} {"(overflow)" if self.Cout else ""}')
        print(f'S = {self.toString(self.S)} (Bin)')
        print(f'S = {int(self.toString(self.S).replace(" ", ""),2)} (Int)')
        ans = input('\nRestart? (y/n) ')
        if(ans == 'y'):
            print()
            self.start()
        else:
            return
        print('-'*20)



    def start(self):
        print('-'*20)
        print(f'{self.size}-bit Ripple Adder (0~{2**self.size-1})')
        self.read_number()
        self.calculate()
        return
        

if __name__ == "__main__":
    # RippleAdder(4).start()
    RippleAdder(32).start()





