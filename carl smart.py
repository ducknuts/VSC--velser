name = input('Name of the victim ? ')
str = """
Most highly esteemed $XXX.
We have the incredible pleasure of introducing you to out new series of products for the discerning customer. 
As you, $name, is known as one who only goes for the best of the best, please allow us to offer youa personal introductory discount.
In order for you to make use of this irresistable discount, $XXX, it is vital that you enter your full name, 
your visa account number and this code: 542XS3486Q-9, when you order from us.
We are looking forwards to making you, $XXX, a regular and esteemed customer.
Carl Smart. CEO, Dan-junc."""

str = str.replace("$XXX", name)
str = str.replace("$name", name)

print(str)

#Use the call:   str = str.replace( what, replacement)A template for the text is found in your home directory, subdirectory spam.txt
