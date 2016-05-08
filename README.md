chance
======


There is an awesome random generator called [chance](http://chancejs.com/)
written by [Victor Quinn](http://victorquinn.com/). It is quite useful for
filling something with dump data which will look like real one in production.
Also there can be a lot of other cases to use it.

This lib written in Python, using chance.js implementation as a
guide.

##Installation
As easy as:
```
pip install chance
```
Then just:
```
from chance import chance
```

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

#####hex_hash
Return a random hex hash. Defahult length is 20.
```
chance.hash()
chance.hash(length=25)
```


#####color
Return a color. Available formats are hex and rgb with grayscale option. 
```
chance.color() # #d722ef
chance.color(form='rgb') # rgb(168, 187, 156)
chance.color(grayscale=True) # '#e5e5e5'
chance.color(form='rgb', grayscale=True) # rgb(176, 176, 176)
```


#####tld
Return a random tld (Top Level Domain) from this list:
('com', 'org', 'edu', 'gov', 'co.uk', 'net', 'io', 'ru', 'eu',).
No parameters supported for this function.
```
chance.tld() # 'org'
```

#####domain
Return a random domain name. You can specify tld.
```
chance.domain() # zircoz.com
chance.domain('ru') # wippok.ru
chance.domain(tld='eu') # vovupjib.eu
```

#####url
Generating url. Domain, path and file extentions are
optional arguments.
```
chance.url() # pebwiwa.eu/huke/sipofnu/tummi/bowace
chance.url(p='/1/2/3') # chance.url(p='/1/2/3') # wippok.ru
chance.url(dom='example.com') # example.com/wecobi/vopoga/bizizuz/livtellu
chance.url(exts=['py', 'cpp', 'css', 'html']) # kibuv.io/nocal/tepoji/sifezril/wozbochi/nalzolip/lonlumi.css
```

#####email
Return a random email with optionally specified domain name.
```
chance.email() # banku@cagvil.org
chance.email(dom='edu.com') # nigu@edu.com
```

#####phone
Phone number, which can be formatted or not (it is by default).
Groups parameter can be used to configure numbers amount after
phone prefix.
```
chance.phone() # '(449) 936-062-335-345'
chance.phone(formatted=False) # '952117233862906'
chance.phone(groups=3) # '(229) 628-707-001'
```

#####ip
Return a random ip.
```
chance.ip() # 201.248.197.225
```

#####ipv6
Just a random ipv6.
```
chance.ipv6() # 0ac7:c557:edf2:e048:00d9:615e:67f1:932b
```

#####twitter
Random twitter handle.
```
chance.twitter() # '@jewlo'
```

#####country
Random real country name. By default returns full name in 
english, but language and short optional arguments can be used.
```
chance.country() # Australia
chance.country(short=True) # NP
chance.country(language='ru', ) # Норвегия
chance.country(language='ru', short=True) # TL
```


#####state
Random state name which depends on language option. For "en" it will be on of USA states,
and with 'ru' Russian one. You can also specify option for short names.
```
chance.state() # Wisconsin
chance.state(language='ru') # Кемеровская область
chance.state(language='ru', ) # Переулок Симгудвыд
chance.state(language='ru', short=True) # ул. Орен. обл.
chance.state(language='en', short=True) # VI
```


#####city
Random city name with optional language parameter.
```
chance.city() # Nowochel
chance.city(language='ru') # Вызящу
```


#####street
Return a random street name. Available options are short suffix and language.
```
chance.street() # Vehu Highway
chance.street(short_suffix=True) # Wemvofhu Rdg
chance.street(language='ru') # Переулок Симгудвыд
chance.street(language='ru', short_suffix=True) # ул. Тосэкэг
```


#####path
Local folder path. Exact depth can be specified or minimum and maximum of it.
```
chance.path() # /judip/sebozfir/zamuthej/bozi/tutweki/wuchihu
chance.path(depth=4) # /tacpozsu/noddo/soke/hegof
chance.path(minimum=4, maximum=7) # /gonuhce/popag/tujubzin/modevmo/hozi
```


#####filepath
Local path to file. Options are same as for path, but extentions list
can be optionally added.
```
chance.filepath() # /decu/dosa/locavu/roskekib/belomlew/robpa.css
chance.filepath(depth=4) # /ruplu/hutcuvaf/tihku/fubjepot/jeribo.mp3'
chance.filepath(minimum=4, maximum=7) # /munos/bowafi/sanasza/vehodru/woraz/mukhetna/lona.html
chance.filepath(extentions=['py', 'cpp']) # /jebzihis/misge/nira/cizollos/tazfetti/fotatcil/didfonih.cpp
```


#####dictionary
This function generates dictionary from values parameter.
For example this:
```
example = {
    'streetway': ('street', {'language': 'en'}),
    'first_name': ('first', {'language': 'en'})
}
chance.dictionary(example)
```
will output something like this:
```
{'streetway': 'Jabhuru Point', 'first_name': 'Eunice'}
```



