from message import Message
from signature_message import SignatureMessage

msg = Message("First1 Last1", "First2 Last2")
actual = str(msg)
expected = "From: First1 Last1\nTo: First2 Last2\n"
assert actual == expected, f"\nExpected:\n{expected}\nActual:\n{actual}"

msg1 = Message("John Hurt", "Susan Field")
msg1.append("The first line of the message")
msg1.append("the second line.")
actual = str(msg1)
expected = "From: John Hurt\nTo: Susan Field\nThe first line of the message\nthe second line.\n"
assert actual == expected, f"\nExpected:\n{expected}\nActual:\n{actual}"

msg2 = Message("Margaret Hamilton", "Joe Peters")  
msg2.append("First line")
msg2.append("Second line")
msg2.append("Third line")
actual = str(msg2)
expected = "From: Margaret Hamilton\nTo: Joe Peters\nFirst line\nSecond line\nThird line\n"
assert actual == expected, f"\nExpected:\n{expected}\nActual:\n{actual}"

actual = len(msg2)
expected = 31
assert actual == expected, f"\nExpected:\n{expected}\nActual:\n{actual}"

actual = msg1 > msg2
expected = True
assert actual == expected, f"\nExpected:\n{expected}\nActual:\n{actual}"

actual = msg2 > msg1
expected = False
assert actual == expected, f"\nExpected:\n{expected}\nActual:\n{actual}"

msg3 = SignatureMessage("Bob Jones", "Bill Gates", "Bob Jones, Assistant Professor, Reykjavik University")
msg3.append("A message with a signature")
msg3.append("and two lines.")

actual = str(msg3)
expected = "From: Bob Jones\nTo: Bill Gates\nA message with a signature\nand two lines.\n\nBob Jones, Assistant Professor, Reykjavik University"
assert actual == expected, f"\nExpected:\n{expected}\nActual:\n{actual}"

actual = len(msg3)
expected = 40
assert actual == expected, f"\nExpected:\n{expected}\nActual:\n{actual}"

actual = msg3 > msg2
expected = True
assert actual == expected, f"\nExpected:\n{expected}\nActual:\n{actual}"

