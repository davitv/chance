import random
import chance_exceptions
import datetime
import dictionaries


NUMBERS = '0123456789';
CHARS_LOWER = 'abcdefghijklmnopqrstuvwxyz'
SYMBOLS = "!@#$%^&*()[]"
HEX_POOL = NUMBERS + 'abcdef'
MAX_INT = 9007199254740992
MIN_INT = -MAX_INT
CONSONANTS = 'bcdfghjklmnprstvwz'
VOWELS = 'aeiou'


def boolean(likelihood=50):
    if likelihood < 0 or likelihood > 100:
        raise chance_exceptions.WrongArgumentValue(
            "likelihood argument value provided for chance.boolean(likelihood) accepts numbers from 0 to 100."
            )
    return random.random()  * 100 < likelihood


def character(pool='', alpha=True, symbols=True, numbers=False, case='any'):

    if not isinstance(pool, (str)):
        raise chance_exceptions.WrongArgumentValue("Pool argument must be string instance")
    
    if not pool:
        if alpha:
            pool += CHARS_LOWER
        
        if case == 'upper':
            pool = pool.upper()
        elif case == 'any':
            pool += pool.upper()

        if symbols:
            pool += SYMBOLS

        if numbers:
            pool += NUMBERS
        
    return pool[random.randint(0, len(pool) - 1)]


def string(pool='', length=0, minimum=5, maximum=20):

    if not isinstance(pool, (str)):
        raise chance_exceptions.WrongArgumentValue("pool argument must be string instance")

    length = length or random.randint(minimum, maximum)
    result = ''
    for x in range(0, length):
        result += character(pool=pool)

    return result


def syllable(length=0, minimum=2, maximum=3, vowel_first=False):
    
    if not isinstance(length, (int)) or length < 0:
        raise chance_exceptions.WrongArgumentValue("length argument must be a positive integer")

    length = length or random.randint(minimum, maximum)

    if vowel_first:
        first, second = VOWELS, CONSONANTS
    else:
        first, second = CONSONANTS, VOWELS

    result = ''

    for x in xrange(0, length):
        result += first[random.randint(0, len(first)-1)]
        first, second = second, first
    return result


def word(syllables=0):
    
    if not isinstance(syllables, (int)) or syllables < 0:
        raise chance_exceptions.WrongArgumentValue("syllables argument must be a positive integer")
    
    syllables = syllables or random.randint(2,3)

    result = ''
    for x in xrange(syllables):
        result += syllable()
    return result

def sentence(words=0, ended_by=''):

    if not isinstance(words, (int)) or words < 0:
        raise chance_exceptions.WrongArgumentValue("words argument must be a positive integer")
    
    if not isinstance(ended_by, (str)) or words < 0:
        raise chance_exceptions.WrongArgumentValue("ended_by argument must be a string")
    
    if not ended_by:
        ended_by = '.'
    elif len(ended_by) > 1:
        ended_by = ended_by[random.randint(0, len(ended_by)-1)]
    length = words or random.randint(12, 18)
    result = []
    for x in xrange(length):
        result.append(word())

    return ' '.join(result).capitalize() + ended_by


def paragraph(sentences=0):

    if not isinstance(sentences, (int)) or sentences < 0:
        raise chance_exceptions.WrongArgumentValue("sentences argument must be a positive integer")
    
    last_char_pool = '.'*4+'?!'
    length = sentences or random.randint(3, 7)
    result = []
    for x in xrange(length):
        result.append(sentence(ended_by=last_char_pool))
    
    return ' '.join(result)


def age(period='age'):
    periods = {
         'child': (1, 12),
         'teen': (13, 19),
         'adult': (18, 120),
         'senior': (65, 120),
         'age': (1, 120),
    }

    if not period in periods:
        raise chance_exceptions.WrongArgumentValue("period should be one of this: " + ', '.join(periods.keys()))

    return random.randint(periods[period][0], periods[period][1])


def date(year=0, month=0, day=0, hour=0, minutes=0, minyear=500):
    months_days_tuple = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    if not year:
        year = random.randint(minyear, 3000)

    if not month:
        month = random.randint(1, 12)

    if not day:
        day = random.randint(1, months_days_tuple[month-1]-1) 

    if not hour:
        hour = random.randint(0, 23) 

    if not minutes:
        minutes = random.randint(0, 59) 

    return datetime.datetime(year, month, day, hour, minutes)


def birthday(period='age'):
    year = datetime.date.today().year - age(period)
    return date(year=year).date()


def first(gender='', language='en'):
    if not gender:
        gender = 'f' if boolean() else 'm'
    elif gender[0] != 'f' and gender[0] != 'm':
        raise chance_exceptions.WrongArgumentValue("gender should be one of this: m (male), f (female)")
    else:
        gender = gender[0]

    if not language in dictionaries.first_names:
        raise chance_exceptions.WrongArgumentValue(language + " dictionary for first name not found in dictionaries module")
    cur_dict = dictionaries.first_names[language][gender]
    name = cur_dict[random.randint(0, len(cur_dict)-1)]
    return name



def last(gender='', language='en'):
    if not gender:
        gender = 'f' if boolean() else 'm'
    elif gender[0] != 'f' and gender[0] != 'm':
        raise chance_exceptions.WrongArgumentValue("gender should be one of this: m (male), f (female)")
    else:
        gender = gender[0]

    if not language in dictionaries.last_names:
        raise chance_exceptions.WrongArgumentValue(language + " dictionary for first name not found in dictionaries module")
    cur_dict = dictionaries.last_names[language][gender]
    name = cur_dict[random.randint(0, len(cur_dict)-1)]
    return name


def name(gender='', language='en'):
    return first(gender, language) + ' ' + last(gender, language)


def hex_hash(length=20):
    return string(length=length, pool=HEX_POOL)


def color(form='hex', grayscale=False):
    def gray(value, delimeter=''):
        v = str(value)
        return delimeter.join([v,v,v])
    
    if form == 'hex':
        return '#' + gray(hex_hash(2)) if grayscale else '#' + hex_hash(6)

    if form == 'rgb':
        a, b, c = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        return 'rgb(' + gray(a, ', ') + ')' if grayscale else 'rgb(' + str(a) + ', ' + str(b) + ', ' + str(c) + ')'

    raise chance_exceptions.WrongArgumentValue('invalid format provided. Please provide one of "hex" or "rgb"')


def domain(tld=''):

    if not isinstance(tld, (str)):
        raise chance_exceptions.WrongArgumentValue("tld argument must be a string")
    
    tlds = ('com', 'org', 'edu', 'gov', 'co.uk', 'net', 'io',)
    if not tld:
        tld = tlds[random.randint(0, len(tlds)-1)]

    return word() + '.' + tld

def email(dom=''):

    if not isinstance(dom, (str)):
        raise chance_exceptions.WrongArgumentValue("dom (domain) argument must be a string")
    
    if not dom:
        dom = domain()

    return word() + '@' + dom


def ip():
    tup = (str(random.randint(0, 255)) for x in xrange(4))
    return '.'.join(tup)