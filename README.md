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
Rerturning a random character (lower or uppercase) or symbol
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
Rerturning a random string by calling chance.character(pool) length times
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
