def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ', 10)
    return words
# split seems to be an actual command
# it is; check in python, help(str)
# split transforma string (str) em lista
# empty separator error sem nenhum espaço; (' ') do exercise not necessário
# o tamanho de /um space em diante/ também define a separação @ whitespaces
# se você usa ',', a lista é dividida a partir de onde se acham commas
# um bom exemplo é .split('r').
# contudo, os Rs desaparecem onde a lista se divide

# S.split(sep=None, maxsplit=-1) -> list of strings

# Return a list of the words in S, using sep as the
# delimiter string.  If maxsplit is given, at most maxsplit
# splits are done. If sep is not specified or is None, any
# whitespace string is a separator and empty strings are
# removed from the result.

# maxsplit = segundo valor dentro do parênteses, integer.
# define a quantidade máxima de partes que o split pode se separar

# return é importante pra guardar o valor pra funções subsequentes, com várias

def sort_words(words):
    """Sorts the words."""
    return sorted(words)
# Return a new list containing all items from the iterable in ascending order.

# A custom key function can be supplied to customize the sort order, and
# the reverse flag can be set to request the result in descending order.

def print_first_word(words):
    """Prints the first word after popping it off."""
    words = words.pop(0)
    print(words)
    return words
# pop só funciona em lists
# chega a remover o valor da lista
# use return pra salvar o valor de pop, otherwise só funciona uma vez (1)
# (2) e então o valor é perdido, sendo popped out da string original
# (3) onde pop foi aplicado

# 0 = primeiro item da lista

# return words
# print(words)

#vs

# print(words)
# return words

# nesta função:

# 1. guarda o valor e não printa nada, pois o item 0 foi removido da lista
# 1.1 passa a retornar o valor ao se digitar uma variável igual à função
# 1.2 mas não antes disso; nada é printado antes de se digitar a variável

# 2. printa o item de valor 0 primeiro
# 2.1 depois o guarda como valor através de return(variável que é = arg.pop)
# 2.2 todo uso subsequente da variável definida e digitada repete o valor
# 2.3 que foi guardado por pop
# 2.4 a diferença é que print chega a printar o item antes do valor ser guardado

# exs:

# Python

# >>> = um comando

#>>> import ex25
#>>> sentence = "All good things come to those who wait."
#>>> asdf = ex25.break_words(sentence)
#>>> asdf
#['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']
#>>> popping = ex25.print_first_word(asdf)              ##(nada printado)
#>>> popping
#'All'
## podendo popping ser repetido agora e entregando o valor acima; thanks return

#>>> import ex25
#>>> sentence = "All good things come to those who wait."
#>>> asdf = ex25.break_words(sentence)
#>>> asdf
#['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']
#>>> sentence
#'All good things come to those who wait.'
#>>> popping = ex25.print_first_word(asdf)
#All
#>>> popping
#'All'
## popping também podendo ser repetido e entregando o valor de lista acima
#>>> asdf
#['good', 'things', 'come', 'to', 'those', 'who', 'wait.']
#>>> sentence
#'All good things come to those who wait.'

def print_last_word(words):
    """Prints the last word after popping it off."""
    words = words.pop(-1)
    print(words)

# -1 = último item da lista

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_sentence(words)
# AttributeError: 'list' object has no attribute 'split'
# Não pode ser usado até uma lista ter sido criada através do split
# quebra a string em lista
# retorna (guarda) o valor da string quebrada em lista
# então aplica a função sort sobre a variável definida, através do 1° argumento

##quebrando com return break_words(words):

#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#  File "C:\Users\User\prog\lpthw\ex25.py", line 111, in sort_sentence
#    return break_words(words)
#  File "C:\Users\User\prog\lpthw\ex25.py", line 3, in break_words
#    words = stuff.split(' ', 10)
#AttributeError: 'list' object has no attribute 'split'

##testando com break_words(sentence):

#>>> import ex25
#>>> sentence = "All good things come to those who wait."
#>>> asdf = ex25.break_words(sentence)
#>>> sentence
#'All good things come to those who wait.'
#>>> sortest = ex25.sort_sentence(sentence)
#>>> sortest
#['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']
#>>> asdf
#['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    myboi = break_words(sentence)
    print_first_word(myboi)
    print_last_word(myboi)

# >>> sentence
# 'All good things come to those who wait.'
# >>> fandlast = ex25.print_first_and_last(sentence)
# All
# wait.
# >

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    myboi = sort_sentence(sentence)
    print_first_word(myboi)
    print_last_word(myboi)

# >>> sentence
# 'All good things come to those who wait.'
# >>> fandlastsort = ex25.print_first_and_last_sorted(sentence)
# All
# who
# >
