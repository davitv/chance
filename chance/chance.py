from __future__ import unicode_literals
from __future__ import absolute_import
import sys
import random
import datetime

from chance import dictionaries
from chance.chance_exceptions import DictionaryException, WrongArgumentValue

PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3

if PY3:
    text_type = str
else:
    text_type = unicode


def boolean(likelihood=50):
    if not isinstance(likelihood, int) or likelihood < 0 or likelihood > 100:
        raise WrongArgumentValue(
            "likelihood argument value provided for chance.boolean(likelihood) accepts integers from 0 to 100."
            )
    return random.random() * 100 < likelihood


def character(pool='', alpha=True, symbols=True, numbers=False, case='any', language='en'):

    if not isinstance(pool, text_type):
        raise WrongArgumentValue("Pool argument must be string instance")

    if language not in dictionaries.chars_lower:
        raise DictionaryException("chars_lower pool for language " + language + " not"
                                  " in dictionaries.py")

    chars_lower = dictionaries.chars_lower[language]
    if not pool:
        if alpha:
            pool += chars_lower

        if case == 'upper':
            pool = pool.upper()
        elif case == 'any':
            pool += pool.upper()

        if symbols:
            pool += dictionaries.symbols

        if numbers:
            pool += dictionaries.numbers

    return pool[random.randint(0, len(pool) - 1)]


def string(pool='', length=0, minimum=5, maximum=20, language='en'):

    if not isinstance(pool, text_type):
        raise WrongArgumentValue("pool argument must be string instance")

    length = length or random.randint(minimum, maximum)
    result = ''
    for x in range(0, length):
        result += character(pool=pool, language=language)

    return result


def syllable(length=0, minimum=2, maximum=3, vowel_first=False, language='en'):

    if not isinstance(length, int) or length < 0:
        raise WrongArgumentValue("length argument must be a positive integer")

    length = length or random.randint(minimum, maximum)

    if language not in dictionaries.consonants:
        raise DictionaryException("consonants pool for specified language  not found"
                                  " in dictionaries.py")

    if language not in dictionaries.vowels:
        raise DictionaryException("vowels pool for specified language  not found"
                                  " in dictionaries.py")

    if vowel_first:
        first, second = dictionaries.vowels[language], dictionaries.consonants[language]
    else:
        first, second = dictionaries.consonants[language], dictionaries.vowels[language]

    result = ''

    for x in range(0, length):
        result += first[random.randint(0, len(first)-1)]
        first, second = second, first
    return result


def word(syllables=0, language='en'):

    if not isinstance(syllables, int) or syllables < 0:
        raise WrongArgumentValue("syllables argument must be a positive integer")

    syllables = syllables or random.randint(2,3)

    result = ''
    for x in range(syllables):
        result += syllable(language=language)
    return result


def sentence(words=0, ended_by='', language='en'):

    if not isinstance(words, int) or words < 0:
        raise WrongArgumentValue("words argument must be a positive integer")

    if not isinstance(ended_by, text_type) or words < 0:
        raise WrongArgumentValue("ended_by argument must be a string")

    if not ended_by:
        ended_by = '.'
    elif len(ended_by) > 1:
        ended_by = ended_by[random.randint(0, len(ended_by)-1)]
    length = words or random.randint(12, 18)
    result = []
    for x in range(length):
        result.append(word(language=language))

    return ' '.join(result).capitalize() + ended_by


def paragraph(sentences=0, language='en'):

    if not isinstance(sentences, int) or sentences < 0:
        raise WrongArgumentValue("sentences argument must be a positive integer")

    last_char_pool = '.'*4+'?!'
    length = sentences or random.randint(3, 7)
    result = []
    for x in range(length):
        result.append(sentence(ended_by=last_char_pool, language=language))

    return ' '.join(result)


def age(period='age'):
    periods = {
        'child': (1, 12),
        'teen': (13, 19),
        'adult': (18, 120),
        'senior': (65, 120),
        'age': (1, 120),
    }

    if period not in periods:
        raise WrongArgumentValue("period should be one of this: " + ', '.join(periods.keys()))

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
        raise WrongArgumentValue("gender should be one of this: m (male), f (female)")
    else:
        gender = gender[0]

    if language not in dictionaries.first_names:
        raise WrongArgumentValue(language + " dictionary for first name not found in dictionaries module")
    cur_dict = dictionaries.first_names[language][gender]
    name = cur_dict[random.randint(0, len(cur_dict)-1)]
    return name


def last(gender='', language='en'):
    if not gender:
        gender = 'f' if boolean() else 'm'
    elif gender[0] != 'f' and gender[0] != 'm':
        raise WrongArgumentValue("gender should be one of this: m (male), f (female)")
    else:
        gender = gender[0]

    if language not in dictionaries.last_names:
        raise WrongArgumentValue(language + " dictionary for first name not found in dictionaries module")
    cur_dict = dictionaries.last_names[language][gender]
    name = cur_dict[random.randint(0, len(cur_dict)-1)]
    return name


def name(gender='', language='en'):
    if not gender:
        gender = 'f' if boolean() else 'm'
    return first(gender, language) + ' ' + last(gender, language)


def hex_hash(length=20):
    return string(length=length, pool=dictionaries.hex_pool)


def color(form='hex', grayscale=False):
    def gray(value, delimeter=''):
        v = text_type(value)
        return delimeter.join([v,v,v])

    if form == 'hex':
        return '#' + gray(hex_hash(2)) if grayscale else '#' + hex_hash(6)

    if form == 'rgb':
        a, b, c = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        return 'rgb(' + gray(a, ', ') + ')' if grayscale else u'rgb({0}, {1}, {2})'.format(text_type(a), text_type(b),
                                                                                           text_type(c))

    raise WrongArgumentValue('invalid format provided. Please provide one of "hex" or "rgb"')


def tld():
    """
    Return a random tld (Top Level Domain) from the tlds list below
    :return: str
    """
    tlds = ('com', 'org', 'edu', 'gov', 'co.uk', 'net', 'io', 'ru', 'eu',)
    return tlds[random.randint(0, len(tlds)-1)]


def domain(t=''):

    if not isinstance(t, text_type):
        raise WrongArgumentValue("t (tld) argument must be a string")

    if not t:
        t = tld()
    return word() + '.' + t


def url(dom='', p='', exts=''):

    if not isinstance(dom, text_type):
        raise WrongArgumentValue("dom (domain) argument must be a string")

    dom = dom or domain()
    p = p or path()
    extention = '.' + exts[random.randint(0, len(exts)-1)] if exts else ''
    return dom + p + extention


def email(dom=''):

    if not isinstance(dom, text_type):
        raise WrongArgumentValue("dom (domain) argument must be a string")

    if not dom:
        dom = domain()

    return word() + '@' + dom


def ip():
    tup = (text_type(random.randint(0, 255)) for x in range(4))
    return '.'.join(tup)


def ipv6():
    return ':'.join((text_type(hex_hash(4)) for x in range(8)))


def twitter():
    return '@' + word()


def country(language='en', short=False):
    if language not in dictionaries.countries:
        raise DictionaryException("countries pool for specified language  not found"
                                  " in dictionaries.py")
    countries = dictionaries.countries[language]
    if short:
        kind = 'code'
    else:
        kind = 'name'
    rand = random.randint(0, len(countries)-1)
    return countries[rand][kind]


def street(language='en', short_suffix=False):

    if language not in dictionaries.streets_suffixes:
        raise DictionaryException("street suffixs pool for specified language  not found"
                                  " in dictionaries.py")

    streets_suffixes = dictionaries.streets_suffixes[language]
    suffix_type = 'abbreviation' if short_suffix else 'name'
    suffix = streets_suffixes[random.randint(0, len(streets_suffixes)-1)][suffix_type]
    if language == 'en':
        return word(language=language).capitalize() + ' ' + suffix
    elif language == 'ru':
        suffix + ' ' + word(language=language).capitalize()

    return suffix + ' ' + word(language=language).capitalize()


def state(language='en', short=False):
    if language not in dictionaries.states:
        raise DictionaryException("states pool for specified language  not found"
                                  " in dictionaries.py")
    states = dictionaries.states[language]
    if short:
        kind = 'abbreviation'
    else:
        kind = 'name'
    rand = random.randint(0, len(states)-1)
    return states[rand][kind]


def city(language='en'):
    return word(3, language).capitalize()


def phone(formatted=True, groups=4):
    prefix = ''
    for x in range(3):
        prefix += text_type(random.randint(0, 9))

    suffix = []
    for x in range(groups):
        tmp = ''
        for x in range(3):
            tmp += text_type(random.randint(0, 9))
        suffix.append(tmp)
    if formatted:
        res = '(' + prefix + ')' + ' ' + '-'.join(suffix)
    else:
        res = prefix + ''.join(suffix)

    return res


def path(depth=0, minimum=4, maximum=6):
    delimeter = '/'
    folders = []
    depth = depth or random.randint(minimum, maximum)
    for x in range(depth):
        folders.append(word())

    return delimeter + delimeter.join(folders)


def filepath(extentions=None, depth=0, minimum=4, maximum=6):
    extentions = extentions or dictionaries.extentions
    result = path(depth, minimum, maximum)
    extention = extentions[random.randint(0, len(extentions)-1)]
    result += '/' + word() + '.' + extention
    return result

functions_map = {
    'boolean': boolean,
    'character': character,
    'string': string,
    'syllable': syllable,
    'word': word,
    'sentence': sentence,
    'paragraph': paragraph,
    'age': age,
    'date': date,
    'birthday': birthday,
    'first': first,
    'last': last,
    'name': name,
    'hex_hash': hex_hash,
    'color': color,
    'domain': domain,
    'email': email,
    'ip': ip,
    'street': street,
    'state': state,
    'city': city,
    'phone': phone,
    'path': path,
    'filepath': filepath
}


def dictionary(values):
    """
    This function generates dictionary
    from values parameter.
    For example this:
    example = {
        'streetway': ('street', {'language': 'en'}),
        'first_name': ('first', {'language': 'en'})
    }
    chance.dictionary(example)
    will output something like this:
    {'streetway': 'Jabhuru Point', 'first_name': 'Eunice'}

    :param values: dict
    :return: dict
    """
    result = dict()
    for key in values:
        fname = values[key][0]
        if fname not in functions_map:
            result[key] = values[key]
        else:
            params = values[key][1] if len(values[key]) == 2 else {}
            result[key] = functions_map[fname](**params)
    return result
