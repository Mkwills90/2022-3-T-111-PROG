class Message():

    def __init__(self, sender, recipient):
        self.sender = sender
        self.recipient = recipient
        self.text = []

    def append(self, line):
        self.text.append(line)
    
    def __str__(self):
        message_str = "From: {}\nTo: {}\n".format(self.sender, self.recipient)
        for line in self.text:
            message_str += "{}\n".format(line)
        
        return message_str 

    def __len__(self):
        count = 0
        for string in self.text:
            count += len(string)

        return count

    def __gt__(self, other):
        '''One message is greater than another its character count is greater'''
        return len(self) > len(other)