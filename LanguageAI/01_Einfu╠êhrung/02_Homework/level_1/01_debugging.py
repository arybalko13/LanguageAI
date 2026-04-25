# *** LEVEL 1 - DEBUGGING *** #
# Der folgende Code enthält einige absichtlich eingebaute Fehler.
# Nutzen Sie die Traceback-Nachrichten und das PyCharm Syntax-Highlighting um diese Fehler zu finden und zu beheben!
# Erklären Sie außerdem in Kommentaren, wodurch der Fehler ausgelöst wird!
# Die Aufgabe ist erfolgreich abgeschlossen, wenn beim Ausführen des Codes keine Fehler auftreten.


# AUFGABE 1 - VARIABLEN

int = 1
float = 1.0
boolean = True
string = "11"

sample_int = 1
sample_int = 2
sample_int != 3
sample_int == 4

sample_string = "hello world!"
sample_string = 'hello world!'
sample_string = "hello world!"
sample_string = """hello world!"""
sample_string = "hello world!"
sample_string = "hello world"
sample_string = "hello world!"
sample_string = "hello world!"
sample_string = "hello world!"

sample_list = [1, 2, 3, 4, 5]
sample_list = [1, 2, 3, 4, 5.5]
sample_list = [1.2, 2, 03.22, 4, 5]
sample_list = [1.123, 2.434, 3.334, 4.343, 5.552]
sample_list = ["Hello", "world!"]
sample_list = ["Hello", "world!", "Nice", "to", "meet", "you!"]
sample_list = ["Hello", "world!", "Nice", "to", "meet", "you", 2, "!"]
sample_list = ["Hello", "world!", ["Nice", "to", "meet", "you", 2, "!"]]
sample_list = [["Hello", "world!"], ["Nice", "to", "meet", "you", 2, "!"]]
sample_list = [["Hello", "world!"], ["Nice", ["to", "meet"], "you", 2, "!"]]

sample_dict = {"Hello": 1, "world!": 2}
sample_dict = {"Hello": 1, "world!": 2, "Hi": 1, "John!": 3.5}
sample_dict = {"Hello": 1, "world!": 2, "Hi": 1, "John!": 3.5}
sample_dict = {"Hello": 1, "world!": 2, "Hello": 1, "John!": 3.5}


# AUFGABE 2 - EINGEBAUTE FUNKTIONEN

# sample_int_length = len(sample_int)
# sample_string_length = len(sample_string)
sample_list_length = len(sample_list)
sample_dict_length = len(sample_dict)

print(sample_int)
print(sample_string)
print(sample_list)

type(sample_string)
type(sample_dict)
type(sample_string)


# AUFGABE 3 - EINGEBAUTE METHODEN

"Hello world!".split()
"Hello world!".split()
("Hello", "World")

[1, 2, 3, 4, 5].sort()
[1, 2, 3.3, 4, 5].sort()
[1, 2, 3.3, 4.22, 5].sort()
[1, 2, 3.3, 4.22, 5*2].sort()
["Hello", "world!"].sort()
["Hello", "world!", "Nice", "to", "meet", "you!"].sort()
["Hello", "world!", "Nice", "to", "meet", "you", "2"].sort()
["Hello", "world!", "Nice", "to", "meet", "you!", "2"].sort()


# AUFGABE 4 - INDEX OPERATIONEN

sample_string[0]
sample_string[-1]
sample_string[1]
sample_string[len(sample_list)]

sample_list[0]
sample_list[-1]
sample_list[1]
len(sample_list)

sample_string[0:2]
# Sample_string[:]
sample_string[:len(sample_string)]

sample_list[0:2]
sample_list[:]
sample_list[:len(sample_list)]