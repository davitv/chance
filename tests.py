import unittest
import chance
import chance_exceptions
import datetime
import re
import dictionaries


class TestChanceBooleanFunction(unittest.TestCase):

    def test_boolean_returns_bool(self):
        for x in xrange(0, 200):
            self.assertTrue(isinstance(chance.boolean(), (bool)))

    def test_likelihood_50_approximately_result(self):
        true_values, false_values = 0, 0
        iterations = 1000000
        likelihood = 0.5
        infelicity = 0.1

        for x in xrange(0, iterations):
            if chance.boolean(likelihood*100):
                true_values += 1
            else:
                false_values += 1
        res = float(true_values) / false_values
        
        self.assertTrue(res > (likelihood - infelicity))

    def test_likelihood_80_approximately_result(self):
        true_values, false_values = 0, 0
        iterations = 10000
        likelihood = 0.8
        infelicity = 0.1

        for x in xrange(0, iterations):
            if chance.boolean(likelihood*100):
                true_values += 1
            else:
                false_values += 1
        res = float(true_values) / false_values
        
        self.assertTrue(res > (likelihood - infelicity))


    def test_likelihood_10_approximately_result(self):
        true_values, false_values = 0, 0
        iterations = 10000
        likelihood = 0.1
        infelicity = 0.1

        for x in xrange(0, iterations):
            if chance.boolean(likelihood*100):
                true_values += 1
            else:
                false_values += 1
        res = float(true_values) / false_values
        
        self.assertTrue(res > (likelihood - infelicity))

    def test_boolean_raise_wrong_argument_exception(self):
        wrongs = (-1, -.1, 101, 101.1, 'a', 'b', '!')
        for x in wrongs:
            self.assertRaises(chance_exceptions.WrongArgumentValue, chance.boolean, x )


class TestChanceCharacterFunction(unittest.TestCase):
    
    def test_character_returns_character(self):
        chars = 'abcdefghijklmnopqrstuvwxyz!@#$%^&*()[]'
        chars += chars.upper()
        for x in xrange(100):
            ch = chance.character()
            self.assertTrue(chars.find(ch) >= 0)

    def test_character_returns_character_default_params(self):
        chars = 'abcdefghijklmnopqrstuvwxyz!@#$%^&*()[]'
        chars += chars.upper()
        for x in xrange(100):
            ch = chance.character()
            self.assertTrue(chars.find(ch) >= 0)

    def test_character_returns_character_default_symbols_false(self):
        chars = 'abcdefghijklmnopqrstuvwxyz!@#$%^&*()[]'
        chars += chars.upper()
        for x in xrange(100):
            ch = chance.character(symbols=False)
            self.assertTrue(chars.find(ch) >= 0)

    def test_character_returns_default_numbers_true(self):
        chars = 'abcdefghijklmnopqrstuvwxyz!@#$%^&*()[]'
        chars += chars.upper()
        chars += '1234567890'
        for x in xrange(100):
            ch = chance.character(symbols=False)
            self.assertTrue(chars.find(ch) >= 0)

    def test_character_returns_only_symbols(self):
        chars = '!@#$%^&*()[]'
        for x in xrange(100):
            ch = chance.character(symbols=True, alpha=False)
            self.assertTrue(chars.find(ch) >= 0)

    def test_character_returns_character_only_symbols_and_numbers(self):
        chars = '!@#$%^&*()[]'
        chars += '1234567890'
        for x in xrange(100):
            ch = chance.character(symbols=True, alpha=False, numbers=True)
            self.assertTrue(chars.find(ch) >= 0)

    def test_character_returns_only_alpha_and_numbers(self):
        chars = 'abcdefghijklmnopqrstuvwxyz'
        chars += chars.upper()
        chars += '1234567890'
        for x in xrange(100):
            ch = chance.character(symbols=False, alpha=True, numbers=True)
            self.assertTrue(chars.find(ch) >= 0)

    def test_character_returns_only_uppercase_alpha(self):
        chars = 'abcdefghijklmnopqrstuvwxyz'.upper()
        for x in xrange(100):
            ch = chance.character(case='upper', symbols=False,  numbers=False)
            self.assertTrue(chars.find(ch) >= 0)

    def test_character_returns_only_uppercase_alpha_and_symbols(self):
        chars = 'abcdefghijklmnopqrstuvwxyz'.upper()
        chars += '!@#$%^&*()[]'
        for x in xrange(100):
            ch = chance.character(case='upper', symbols=True,  numbers=False)
            self.assertTrue(chars.find(ch) >= 0)

    def test_character_returns_only_uppercase_alpha_and_numbers(self):
        chars = 'abcdefghijklmnopqrstuvwxyz'.upper()
        chars += '1234567890'
        for x in xrange(100):
            ch = chance.character(case='upper', symbols=False,  numbers=True)
            self.assertTrue(chars.find(ch) >= 0)

    def test_character_returns_only_uppercase_alpha_with_symbols_and_numbers(self):
        chars = 'abcdefghijklmnopqrstuvwxyz'.upper()
        chars += '!@#$%^&*()[]'
        chars += '1234567890'
        for x in xrange(100):
            ch = chance.character(case='upper', symbols=True,  numbers=True)
            self.assertTrue(chars.find(ch) >= 0)

    def test_character_returns_only_lower_alpha_with_symbols_and_numbers(self):
        chars = 'abcdefghijklmnopqrstuvwxyz'
        chars += '!@#$%^&*()[]'
        chars += '1234567890'
        for x in xrange(100):
            ch = chance.character(case='lower', symbols=True,  numbers=True)
            self.assertTrue(chars.find(ch) >= 0)

    def test_character_returns_only_lowecase_alpha(self):
        chars = 'abcdefghijklmnopqrstuvwxyz'
        for x in xrange(100):
            ch = chance.character(case='lower', symbols=False,  numbers=False)
            self.assertTrue(chars.find(ch) >= 0)

    def test_character_returns_only_lowercase_alpha_and_symbols(self):
        chars = 'abcdefghijklmnopqrstuvwxyz'
        chars += '!@#$%^&*()[]'
        for x in xrange(100):
            ch = chance.character(case='lower', symbols=True,  numbers=False)
            self.assertTrue(chars.find(ch) >= 0)

    def test_character_returns_only_lowercase_alpha_and_numbers(self):
        chars = 'abcdefghijklmnopqrstuvwxyz'
        chars += '1234567890'
        for x in xrange(100):
            ch = chance.character(case='lower', symbols=False,  numbers=True)
            self.assertTrue(chars.find(ch) >= 0)


    def test_character_raise_exception(self):
        self.assertRaises(chance_exceptions.WrongArgumentValue, chance.character, 10)
        self.assertRaises(chance_exceptions.WrongArgumentValue, chance.character, -1)
        self.assertRaises(chance_exceptions.WrongArgumentValue, chance.character, -.25)
        self.assertRaises(chance_exceptions.DictionaryException, chance.character,  **{'language':'bbdasasdg'})
        self.assertRaises(chance_exceptions.DictionaryException, chance.character,  **{'language':'ff'})


class TestStringFunction(unittest.TestCase):
    
    def test_string_returns_string(self):
        for x in range(100):
            self.assertTrue(isinstance(chance.string(), (str)))

    def test_string_returns_string_with_correct_length(self):
        for x in xrange(1, 100):
            self.assertTrue(len(chance.string(length=x))==x)
       
    def test_string_returns_string_with_correct_min_max(self):
        for x in xrange(1, 100):
            l = len(chance.string(minimum=x, maximum=x+5))
            self.assertTrue(l >= x and l <= (x+5))
        
    def test_string_returns_string_from_correct_pool(self):
        pools = (
            'abcdef',
            'hjfj2131',
            '$553\&66hjfj2131',
            '=_-232fdsf',
        )
        for pool in pools:
            s = chance.string(pool=pool)
            for x in s:
                self.assertTrue(pool.find(x) != -1)

    def test_string_raises_exception(self):
        self.assertRaises(chance_exceptions.WrongArgumentValue, chance.string, -1)
        self.assertRaises(chance_exceptions.WrongArgumentValue, chance.string, -.1)
        self.assertRaises(chance_exceptions.WrongArgumentValue, chance.string, 0)
        self.assertRaises(chance_exceptions.WrongArgumentValue, chance.string, 1)
        self.assertRaises(chance_exceptions.WrongArgumentValue, chance.string, .1)
        self.assertRaises(chance_exceptions.DictionaryException, chance.string, **{'language':'dfsdf'})
    

class TestSyllableFunction(unittest.TestCase):
    def test_syllable_returns_correct_string(self):
        syll = chance.syllable()
        for x in xrange(20):
            syll = chance.syllable(x+1)
            n = syll[0]
            nxt = dictionaries.vowels['en'] if dictionaries.consonants['en'].find(n) != -1 else dictionaries.vowels['en']
            prv = dictionaries.vowels['en'] if dictionaries.vowels['en'].find(n) != -1 else dictionaries.consonants['en'] 
            for i, ch in enumerate(syll):
                if i == 0 or i == (len(syll)-1):
                    continue
                self.assertFalse(nxt.find(ch) == -1)
                nxt, prv = prv, nxt

    def test_syllable_returns_correct_starting_string(self):
        
        for x in xrange(20):
            syll = chance.syllable(x+1, vowel_first=True)
            n = syll[0]
            self.assertFalse(dictionaries.vowels['en'].find(n) == -1)
            nxt = dictionaries.consonants['en']
            prv = dictionaries.vowels['en'] 
            for i, ch in enumerate(syll):
                if i == 0 or i == (len(syll)-1):
                    continue
                self.assertFalse(nxt.find(ch) == -1)
                nxt, prv = prv, nxt
        
        for x in xrange(20):
            syll = chance.syllable(x+1, vowel_first=False)
            n = syll[0]
            self.assertFalse(dictionaries.consonants['en'].find(n) == -1)
            nxt = dictionaries.vowels['en']
            prv = dictionaries.consonants['en']
            for i, ch in enumerate(syll):
                if i == 0 or i == (len(syll)-1):
                    continue
                self.assertFalse(nxt.find(ch) == -1)
                nxt, prv = prv, nxt

    def test_syllable_raises_exception(self):
           self.assertRaises(chance_exceptions.WrongArgumentValue, chance.syllable, 'a')
           self.assertRaises(chance_exceptions.WrongArgumentValue, chance.syllable, dict())
           self.assertRaises(chance_exceptions.WrongArgumentValue, chance.syllable, -1)
           self.assertRaises(chance_exceptions.WrongArgumentValue, chance.syllable, 1.5)
           self.assertRaises(chance_exceptions.DictionaryException, chance.syllable, **{'language':'dasdas'})


class TestWordFunction(unittest.TestCase):

    def test_word_returns_correct_value(self):
        for x in xrange(20):
            word = chance.word()
            self.assertEquals(str, type(word))
            self.assertTrue(len(word) > 3 and len(word) < 10)

    def test_word_raises_exception(self):
        self.assertRaises(chance_exceptions.WrongArgumentValue, chance.word, 'a')
        self.assertRaises(chance_exceptions.WrongArgumentValue, chance.word, dict())
        self.assertRaises(chance_exceptions.WrongArgumentValue, chance.word, -1)
        self.assertRaises(chance_exceptions.WrongArgumentValue, chance.word, 1.5)
        self.assertRaises(chance_exceptions.DictionaryException, chance.word, **{'language':'dasdas'})

class TestSentenceFunction(unittest.TestCase):
    
    def test_sentence_returns_correct_value(self):
        for x in xrange(20):
            self.assertEquals(str, type(chance.sentence()))
            length = len(chance.sentence())
            self.assertTrue(length >= 45 and length <= 324)
        for x in xrange(50):
            self.assertEquals(str, type(chance.sentence(x+1)))
            
    def test_sentence_returns_correct_endings(self):
        end_pool = '?!.:'
        for x in end_pool:
            self.assertEquals(x, chance.sentence(ended_by=x)[-1:])
        last = chance.sentence(ended_by=end_pool)[-1:]
        self.assertTrue(end_pool.find(last) != -1)

    def test_sentence_raises_exception(self):
        self.assertRaises(chance_exceptions.WrongArgumentValue, chance.sentence, 'a')
        self.assertRaises(chance_exceptions.WrongArgumentValue, chance.sentence, dict())
        self.assertRaises(chance_exceptions.WrongArgumentValue, chance.sentence, -1)
        self.assertRaises(chance_exceptions.WrongArgumentValue, chance.sentence, 1.5)
        self.assertRaises(chance_exceptions.WrongArgumentValue, chance.sentence, 5, 12)
        self.assertRaises(chance_exceptions.WrongArgumentValue, chance.sentence, 9, 18)
        self.assertRaises(chance_exceptions.DictionaryException, chance.sentence, **{'language':'dasdas'})


class TestParagraphFunction(unittest.TestCase):
    def test_pragraph_returns_correct_value(self):
        for x in xrange(20):
            self.assertEquals(str, type(chance.paragraph()))
            length = len(chance.paragraph())
            self.assertTrue(length >= 45)



class TestAgeFunction(unittest.TestCase):

    def test_age_returns_correct_value(self):
        for x in xrange(20):
            self.assertEquals(int, type(chance.age()))
            a = chance.age('child')
            self.assertTrue(a >= 1 and a <= 12 )
            a = chance.age('teen')
            self.assertTrue(a >= 13 and a <= 19 )
            a = chance.age('adult')
            self.assertTrue(a >= 18 and a <= 120 )
            a = chance.age('senior')
            self.assertTrue(a >= 65 and a <= 120 )
            a = chance.age()
            self.assertTrue(a >= 1 and a <= 120 )

    def test_age_raises_exception(self):
        self.assertRaises(chance_exceptions.WrongArgumentValue, chance.age, 'i\'m')



class TestDateFunction(unittest.TestCase):

    def test_date_returns_correct_value(self):
        for x in xrange(20):
            self.assertEquals(datetime.datetime, type(chance.date()))


class TestBirthdayFunction(unittest.TestCase):

    def test_birthday_returns_correct_value(self):
        current_year = datetime.date.today().year
        for x in xrange(20):
            self.assertEquals(datetime.date, type(chance.birthday()))
            self.assertTrue(datetime.date(current_year - 121, 1, 1) < chance.birthday())
            self.assertTrue(datetime.date(current_year - 13, 1, 1) < chance.birthday('child'))
            self.assertTrue(datetime.date(current_year - 20, 1, 1) < chance.birthday('teen'))
            self.assertTrue(datetime.date(current_year + 13, 1, 1) > chance.birthday('teen'))
            self.assertTrue(datetime.date(current_year + 20, 1, 1) > chance.birthday('teen'))

class TestFirstNameFunction(unittest.TestCase):

    def test_first_returns_correct_value(self):
        for x in xrange(20):
            self.assertEquals(str, type(chance.first()))


    def test_first_returns_only_gender_specified_name(self):
        from dictionaries import first_names
        names = first_names['en']
        for x in xrange(20):
            name = chance.first(gender='m')
            self.assertTrue(name in names['m'])
        for x in xrange(20):
            name = chance.first(gender='female')
            self.assertTrue(name in names['f'])

class TestLastNameFunction(unittest.TestCase):

    def test_first_returns_correct_value(self):
        for x in xrange(20):
            self.assertEquals(str, type(chance.last()))


    def test_first_returns_only_gender_specified_name(self):
        from dictionaries import last_names
        names = last_names['en']
        for x in xrange(20):
            name = chance.last(gender='m')
            self.assertTrue(name in names['m'])
        for x in xrange(20):
            name = chance.last(gender='female')
            self.assertTrue(name in names['f'])


class TestNameFunction(unittest.TestCase):

    def test_name_returns_correct_value(self):
        for x in xrange(20):
            self.assertEquals(str, type(chance.name()))


    def test_name_returns_only_gender_specified_name(self):
        from dictionaries import last_names, first_names
        first_names = first_names['en']
        last_names= last_names['en']
        for x in xrange(20):
            name = chance.name(gender='m')
            first, last = name.split(' ')
            self.assertTrue(first in first_names['m'])
            self.assertTrue(last in last_names['m'])
        for x in xrange(20):
            name = chance.name(gender='f')
            first, last = name.split(' ')
            self.assertTrue(first in first_names['f'])
            self.assertTrue(last in last_names['f'])

    def test_name_returns_only_language_specified_name(self):
        from dictionaries import last_names, first_names
        first_names = first_names['ru']
        last_names= last_names['ru']
        for x in xrange(200):
            name = chance.name(gender='m', language='ru')
            first, last = name.split(' ')
            self.assertTrue(first in first_names['m'])
            self.assertTrue(last in last_names['m'])
        for x in xrange(200):
            name = chance.name(gender='f', language='ru')
            first, last = name.split(' ')
            self.assertTrue(first in first_names['f'])
            self.assertTrue(last in last_names['f'])

class TestHashFunction(unittest.TestCase):
    
    def test_hash_returns_correct_value(self):
        for x in xrange(20):
            self.assertEquals(int, type(hash(chance.hex_hash())))

class TestColorFunction(unittest.TestCase):
    
    def test_color_returns_correct_value(self):
        hex_color_pattern = re.compile('^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$')
        rgb_color_pattern = re.compile('rgb\((\d{1,3}), (\d{1,3}), (\d{1,3})\)')
        
        for x in xrange(20):
            hex_color = chance.color(form='hex')
            rgb_color = chance.color(form='rgb')
            gray_color = chance.color(grayscale=True)
            self.assertTrue(hex_color_pattern.match(hex_color) != None)
            self.assertTrue(hex_color_pattern.match(gray_color) != None)

            matches = rgb_color_pattern.findall(rgb_color)
            self.assertTrue(len(matches)==1)
            self.assertTrue(len(matches[0])==3)
            for x in matches[0]:
                self.assertTrue(int(x) >= 0 and int(x) <= 255)
            
         
    def test_color_raises_exception(self):
        self.assertRaises(chance_exceptions.WrongArgumentValue, chance.color, 'i\'m')
        self.assertRaises(chance_exceptions.WrongArgumentValue, chance.color, 'sitting')
        self.assertRaises(chance_exceptions.WrongArgumentValue, chance.color, 'in')
        self.assertRaises(chance_exceptions.WrongArgumentValue, chance.color, 'my')
        self.assertRaises(chance_exceptions.WrongArgumentValue, chance.color, 'room')
   

class TestDomainFunction(unittest.TestCase):
    
    def test_domain_returns_correct_value(self):
        domain_pattern = re.compile('^([A-Za-z0-9]+\.[a-z\.]{2,5})$')
       
        for x in xrange(20):
            self.assertTrue(domain_pattern.match(chance.domain()) != None)
         
    def test_domain_raises_exception(self):
        self.assertRaises(chance_exceptions.WrongArgumentValue, chance.domain, 2)
        self.assertRaises(chance_exceptions.WrongArgumentValue, chance.domain, 1)
        self.assertRaises(chance_exceptions.WrongArgumentValue, chance.domain, -1)
        self.assertRaises(chance_exceptions.WrongArgumentValue, chance.domain, .1)
   
class TestEmailFunction(unittest.TestCase):
    def test_email_returns_correct_values(self):
        email_pattern = re.compile('^([A-Za-z0-9]+@[A-Za-z0-9]+\.[a-z\.]{2,5})$')

        for x in xrange(20):
            self.assertTrue(email_pattern.match(chance.email()) != None)

    def test_email_raises_exception(self):
        self.assertRaises(chance_exceptions.WrongArgumentValue, chance.email, 2)
        self.assertRaises(chance_exceptions.WrongArgumentValue, chance.email, 1)
        self.assertRaises(chance_exceptions.WrongArgumentValue, chance.email, -1)
        self.assertRaises(chance_exceptions.WrongArgumentValue, chance.email, .1)

class TestIpFunction(unittest.TestCase):
    def test_ip_returns_correct_values(self):
        ip_pattern = re.compile('^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$')
        for x in xrange(20):
            self.assertTrue(ip_pattern.match(chance.ip()) != None)


class TestStreetFunction(unittest.TestCase):
    def test_street_returns_string_type(self):
        for x in xrange(10):
            self.assertEquals(type(chance.street()), str)
    
    def test_street_returns_unicode(self):
        for x in xrange(10):
            self.assertEquals(type(chance.street(language='ru')), unicode)


class TestStateFunction(unittest.TestCase):
    def test_state_returns_string(self):
        for x in xrange(20):
            self.assertEquals(type(chance.state()), str)

    def test_short_state(self):
        for x in xrange(20):
            st = chance.state(short=True)
            self.assertTrue(len(st) > 1 and len(st) < 4)

    def test_state_returns_correct_language(self):
        all_states = [x['name'] for x in dictionaries.states['en']]
        for x in xrange(20):
            self.assertTrue(chance.state() in all_states)

    def test_state_short_returns_correct_language(self):
        all_states = [x['abbreviation'] for x in dictionaries.states['en']]
        for x in xrange(20):
            self.assertTrue(chance.state(short=True) in all_states)


class TestCityFuncton(unittest.TestCase):
    def test_city_returns_string(self):
        for x in xrange(20):
            self.assertEquals(type(chance.city()), str)


class TestPhoneFunction(unittest.TestCase):
    def test_phone_returns_string(self):
        for x in xrange(20):
           self.assertEquals(str, type(chance.phone()))    

class TestDictionaryFunction(unittest.TestCase):
    def test_dictionary_returns_dict(self):
        example = {
            'first_name': ('first', dict(language='ru')),
            'last_name': ('last', dict(language='ru')),
            'phone': ('phone', dict()),
            'email': ('email', dict()),
            'birthday': ('birthday', dict()),
            'password': '123'
        }
        for x in xrange(10):
            d = chance.dictionary(example)
            for key in example:
                self.assertTrue(key in d)


class TestUnixPathFunction(unittest.TestCase):
    
    def test_correct_value(self):
        path = chance.path()
        for x in xrange(4):
            self.assertTrue(isinstance(path, str))

        for x in xrange(4):
            self.assertTrue(isinstance(path, str))
            self.assertEquals(len(chance.path(depth=3).split('/')), 4)
            self.assertEquals(len(chance.path(depth=4).split('/')), 5)
            self.assertEquals(len(chance.path(depth=6).split('/')), 7)

        for x in xrange(4):
            self.assertTrue(len(chance.path().split('/')) >= 5 and len(chance.path().split('/')) <= 7)
           

class TestUnixFilePathFunction(unittest.TestCase):
    
    def test_correct_value_type(self):
        path = chance.filepath()
        for x in xrange(4):
            self.assertTrue(isinstance(path, str))

    def test_unix_filepath_kind(self):
        for x in xrange(20):
            fpath = chance.filepath()
            pieces = fpath.split('/')
            self.assertTrue(len(pieces) >= 6 and len(pieces) <= 8, (len(pieces), pieces,))
            self.assertTrue(pieces[-1:][0].find('.') > 0)
            
    def test_unix_filepath_returns_correct_extention(self):
        exts = ['hhj']
        for x in xrange(20):
            fpath = chance.filepath(extentions=exts)
            pieces = fpath.split('/')
            self.assertTrue(len(pieces) >= 6 and len(pieces) <= 8, (len(pieces), pieces,))
            self.assertTrue(pieces[-1:][0].find('.') > 0)
            ext = pieces[-1:][0].split('.')[1]
            self.assertTrue( any(ext == x for x in exts))
        
        exts = ['txt', 'emuy']
        for x in xrange(20):
            fpath = chance.filepath(extentions=exts)
            pieces = fpath.split('/')
            self.assertTrue(len(pieces) >= 6 and len(pieces) <= 8, (len(pieces), pieces,))
            self.assertTrue(pieces[-1:][0].find('.') > 0)
            ext = pieces[-1:][0].split('.')[1]
            self.assertTrue( any(ext == x for x in exts))

        exts = ['txt', 'emuy', 'core']
        for x in xrange(20):
            fpath = chance.filepath(extentions=exts)
            pieces = fpath.split('/')
            self.assertTrue(len(pieces) >= 6 and len(pieces) <= 8, (len(pieces), pieces,))
            self.assertTrue(pieces[-1:][0].find('.') > 0)
            ext = pieces[-1:][0].split('.')[1]
            self.assertTrue( any(ext == x for x in exts))


            

if __name__ == '__main__':
    unittest.main()
