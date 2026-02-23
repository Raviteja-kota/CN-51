class Palidrome:
    def check(self):
        class Stringpalin(Palidrome):
            def init(self, s):
                self.s = s

            def check(self):
                if self == s.self[::-1]:
                    print("the word given is a Palindrome")
                else:
                    print("the word isnot a palindrome")

        class NumberPalin(Palidrome):
            def init(self, n):
                self.n = n

            def check(self):
                if self == n.self[::-1]:
                    print("the given number is a Palindrome")
                else:
                    print("the number is not a palindrome")

                s = str(input("enter the string needs palindrome check"))
                n = int(input("enter the number needs palindrome check"))

                print("the given string:", s)
                print("the given number", n)

                print(Stringpalin(s).check())
                print(NumberPalin(n).check())