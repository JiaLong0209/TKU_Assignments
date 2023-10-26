
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
        s1 = 0
        s2 = 0
        c1 = 0
        c2 = 0
        # s1 = s2 = c1 = c2 = 0
        temp1 = self.HA(x,y,s1,c1)                # x y s1 c1
        temp2 = self.HA(temp1[2],z,s2,c2)         # s1 z s2 c2
        return [x,y,z,temp2[2],temp1[3]|temp2[3]] # x, y, z, s2, c1 | c2

    def read_number(self):
        self.A = self.to_binary_array(127);
        self.B = self.to_binary_array(48);
        
    def calculate(self):
        bits = [0,0,0,0,0]
        C = [0 for i in range(self.size)]
        S = [0 for i in range(self.size)]
        for i in range(self.size-1, 0, -1):
            bits = self.FA(self.A[i], self.B[i], C[i], S[i], C[i-1])
            C[i-1] = bits[4]
            S[i] = bits[3]
            print(i, bits)

        for i in S:
            print(i, end='')
        print()
        # print(bits[4])

        print(S)
        return

    def start(self):
        self.read_number()
        print(self.A, self.B)
        self.calculate()

        return
        

if __name__ == "__main__":
    RippleAdder().start()





