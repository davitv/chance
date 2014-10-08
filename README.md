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
# will produce symbol or alpha
chance.character(pool='', alpha=True, symbols=True, numbers=False, case='any') 

chance.character(pool='', alpha=False, symbols=True, numbers=False, case='any') 
# will produce symbol only
```

#####string
Rerturning a random string by calling chance.character(pool) length times
```
# will string from symbols or alphas
chance.string(pool='', length=0, minimum=5, maximum=20)

# custom pool also can be passed
chance.string(pool='abcdef8', length=0, minimum=5, maximum=20)

```
