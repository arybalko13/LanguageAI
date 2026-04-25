# *** LEVEL 1 - ARBEITEN MIT LISTEN *** #
# Listen bieten uns eine praktische Möglichkeit, mehrere Elemente in einer Variable zu speichern.
# Das ist zum Beispiel nützlich, wenn wir nicht mit einem ganzen Satz arbeiten wollen, sondern seinen Bestandteilen.
# Im Folgenden finden Sie einen String, an dem wir unterschiedliche Operationen ausführen wollen:

sample_string = """Python is an interpreted, high-level and general-purpose programming language. 
Python's design philosophy emphasizes code readability with its notable use of significant indentation. 
Its language constructs and object-oriented approach aim to help programmers write clear, 
logical code for small and large-scale projects."""


# AUFGABE 1
# Spalten Sie den String in einzelne Wörter und speichern Sie das Ergebnis in sample_words!

sample_words = ["Python", "is", "an", "interpreted,", "high-level", "and", "general-purpose", "programming", "language.",
"Python's", "design", "philosophy", "emphasizes", "code", "readability", "with", "its", "notable", "use", "of", "significant", "indentation.",
"Its", "language", "constructs", "and", "object-oriented", "approach", "aim", "to", "help", "programmers", "write", "clear,",
"logical", "code", "for", "small", "and", "large-scale", "projects."]

print(sample_words)

# Spalten Sie den String zusätzlich in einzelne Sätze, die Sie in sample_sentences speichern!

sample_sentences = ["Python is an interpreted, high-level and general-purpose programming language.",
"Python's design philosophy emphasizes code readability with its notable use of significant indentation.",
"Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects."]

print(sample_sentences)


# AUFGABE 2
# Ersetzen Sie das erste Element von sample_words durch einen beliebigen String!
sample_words[0] = "Maomao"

print(sample_words)

# Entfernen Sie das letzte Element von sample_words!
sample_words.pop()

print(sample_words)

# Fügen Sie am Ende von sample_words ein neues Element hinzu!
sample_words.append("cats")

print(sample_words)


# AUFGABE 3
# Ermitteln Sie die Anzahl der Zeichen, Wörter und Sätze von sample_string!
# Die Zeichen manuell zu zählen ist dabei natürlich nicht erlaubt!



sample_string_chars_count = len(sample_string)
sample_string_sentence_count = len(sample_sentences)
sample_string_word_count = len(sample_words)

print(sample_string_chars_count)
print(sample_string_sentence_count)
print(sample_string_word_count)


# AUFGABE 4
# Setzen Sie die sample_words und sample_sentences wieder zu einem String zusammen!
# joined_sentences und joined_words sollten am Ende den Datentyp str haben!

joined_sentences = " ".join(sample_words)
joined_words =  " ".join(sample_sentences)

joined_sentences_type = type(joined_sentences)
joined_words_type = type(joined_words)

print(joined_sentences)
print(joined_words)
