from signature_message import SignatureMessage
from message import Message

# Main starts here

# A message with a sender and a receiver, but no text
msg0 = Message("Magnus Carlsen", "Annika Sorenstram") 
print(msg0)

msg1 = Message("John Hurt", "Susan Field")
# Appending strings to the text of the message
msg1.append("This is the first line of the message")
msg1.append("and this is the second line.")
print(msg1)

msg2 = Message("Margaret Hamilton", "Joe Peters")
# Appending strings to the text of the message
msg2.append("Beginning of another message")
msg2.append("with another line")
msg2.append("and the third line")
print(msg2)

# The length of a message is the number of characters in its text (excluding newline characters)
print("The length of message 1: {}".format(len(msg1)))
print("The length of message 2: {}".format(len(msg2)))

# One message is greater than another if its length is greater than the length of the other
if msg1 > msg2:
    print("First message is longer than second message")
print()

# Create a message with a signature
msg3 = SignatureMessage("William Smith", "Richard Rush", "William Smith, Associate Professor, Reykjavik University")
msg3.append("This is a message with a signature.")
print(msg3)