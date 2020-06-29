class Letter:
    def __init__(self, letterfrom, letterto):
        self.recipient = letterto
        self.sender = letterfrom
        self.body = ''
        return

    def append(self, line):
        self.body += '\n'
        self.body += line
        return

    def __str__(self):
        re_str = ""
        re_str += 'Dear '
        re_str += self.recipient
        re_str += ' :'
        re_str += self.body
        re_str += '\nSincerely,\n'
        re_str += self.sender
        return re_str


sender = input("Who is Sender?")
receiver = input("Who is receiver? ")
Letter = Letter(sender, receiver)

line = int(input("How many lines in the massage?"))
for i in range(1, line+1):
    print("Input ", i, "line of the massage : ")
    ins_str = input()
    Letter.append(ins_str)

r_str = Letter.__str__()
print(r_str)
