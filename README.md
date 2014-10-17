chance
======


Recently i found javascript generator  called [chance](http://chancejs.com/) written by  [Victor Quinn](http://victorquinn.com/). I liked it a lot and found it quite useful for programms testing or filling something with dump data. I could't find anything similar for python so i decided to write it on my own, using chance.js implementation as a guide. 

##Usage

####Basic
=
#####boolean
Returning boolean value
```
chance.boolean() # true or false
```
Also likelihood of true can be specified in percents as integer
```
chance.boolean(likelihood=70) # more true values
chance.boolean(likelihood=20) # more false values
```

#####character
Returning a random character (lower or uppercase) or symbol
```
# random symbol or alpha
chance.character(pool='', alpha=True, symbols=True, numbers=False, case='any') 

# random symbol only
chance.character(pool='', alpha=False, symbols=True, numbers=False, case='any')

# random symbol from sepcified pool
chance.character(pool='12!') # 1 or 2 or !

# random symbol from russian language characters pool from dictionaries.py
chance.character(language='ru') 


```

#####string
Returning a random string by calling chance.character(pool) length times
```
# random string from symbols or alphas
chance.string(pool='', length=0)

# if length is 0 (default value) and minimum and maximum specified
# will poduce string with random length, from minimum to maximum
chance.string(pool='abcdef8', minimum=5, maximum=20)

# random string from russian language characters pool from dictionaries.py
# basically, will call chance.character(language='ru')
chance.string(language='ru')
```


#####syllable
Creating a random syllable by alternately concatenating vowel and consonant.
By default, starts from consonant, but with vowel_first parameter turned True
vowel will be first. 
```
# random syllable with consonant first
chance.syllable(language='en', length=0, minimum=2, maximum=3, vowel_first=False)

# random syllable with vowel first
chance.syllable(vowel_first=True)

# random syllable from russian characters pool
chance.syllable(language='ru', vowel_first=True)
```



#####word
Generating random word by concatenating few syllables.

```
# random word
chance.word(language='en')

# random word from russian chars pool
chance.word('ru')

```

#####sentence
Generating random sentence by concatenating few words.

```
# random sentence
chance.sentence(language='en')

# random sentence from russian chars pool with
# '!' at the end
chance.sentence(language='ru', ended_by='!')

```


#####paragraph
Generating paragraph by concatenating sentences.

```
# random sentence
chance.paragraph()

# random paragraph from russian chars pool with
# which contains 20 sentences
chance.paragraph(language='ru', sentences=20)

```

#####age
Actually, generating random integer, which interval is based on period parameter.
```
# periods is a dict with values for random.randint(fr, to)
periods = {
         'child': (1, 12),
         'teen': (13, 19),
         'adult': (18, 120),
         'senior': (65, 120),
         'age': (1, 120),
}
# from 1 to 12
chance.age('child')

# from 18 to 120
chance.age('adult')

```

#####date
Returning datetime object. It's possible to choose which date value will be randomly generated
(year, month, day, hour, minutes), by default all of them will be random. Also you can pass minimal
year as minyear parameter.
All parameters should be integers.

```
# will return datetime object with minimal year 500
chance.date(year=0, month=0, day=0, hour=0, minutes=0, minyear=500)

# every time value will be random, except year
chance.date(year=2012)

# only hour and minutes will be randomly generated
chance.date(year=1999, month=8, day=12)

```

#####birthday
This function based on chance.date function, it's calling chance.age function and
passing returned value to chance.date as year parameter. You can specify period just like in age function.

```
# will return random birth date of a teenager
chance.birthday('teen')

# random adults birthday
chance.birthday('adult')

```

#####first
Returning a first name, randomly selected from dictionary, located in dictionaries.py.
You can add more names localisation there.
```
# first name in english, male or female
chance.first()

# this one will be female name, english again
chance.first(gender='f')

# russian male name
chance.first(language='ru', gender='m')

```

#####last
Similar to chance.first function. Same parameters, same algorythm, just another dictionary used.
```
# last name in english, male or female
chance.last()

# this one will be female surname, english again
chance.last(gender='f')

# russian male surname
chance.last(language='ru', gender='m')

```

#####name
Just a shorthand function, for calling chance.first(<params>) + ' ' + chance.last(<params>)
```
# name in english, male or female
chance.name()

# this one will be female name, english again (chance.first(gender='f') + ' ' + chance.last(gender='f')
chance.name(gender='f')

# russian male name
chance.name(language='ru', gender='m')

```
