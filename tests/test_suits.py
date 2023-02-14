import json

FIRST_DICT = json.load(open('./tests/fixtures/first.json'))
SECOND_DICT = json.load(open('./tests/fixtures/second.json'))
DEEP_FIRST_DICT = json.load(open('./tests/fixtures/deep-first.json'))
DEEP_SECOND_DICT = json.load(open('./tests/fixtures/deep-second.json'))

CONVERT_JSON_TO_DICT_TS = [
    ('./tests/fixtures/first.json', FIRST_DICT),
    ('./tests/fixtures/first.yaml', FIRST_DICT),
    ('./tests/fixtures/first.yml', FIRST_DICT),
    ('./tests/fixtures/deep-first.json', DEEP_FIRST_DICT),
    ('./tests/fixtures/deep-first.yaml', DEEP_FIRST_DICT),
    ('./tests/fixtures/deep-first.yml', DEEP_FIRST_DICT),
    ('./tests/fixtures/deep-second.json', DEEP_SECOND_DICT),
    ('./tests/fixtures/deep-second.yaml', DEEP_SECOND_DICT),
    ('./tests/fixtures/deep-second.yml', DEEP_SECOND_DICT)
]

_D1_1 = {'k1': 1, 'k2': 2, 'k3': 3}
_D2_1 = {'k2': 2, 'k3': None, 'k4': None}
_DD_1 = {'k1': {'-': 1},
         'k2': {'': 2},
         'k3': {'-': 3, '+': None},
         'k4': {'+': None}
         }

_D1_2 = {'k1': 1, 'k2': {'k3': 3, 'k4': 4}}
_D2_2 = {'k1': 1, 'k2': {'k3': 4, 'k5': 5}}
_DD_2 = {'k1': {'': 1},
         'k2': {'': {'k3': {'-': 3, '+': 4},
                     'k4': {'-': 4},
                     'k5': {'+': 5}
                     }
                }
         }

_D1_3 = {'k1': 1, 'k2': {'k3': 3, 'k4': 4}}
_D2_3 = {'k1': {'k6': 6, 'k7': 7}, 'k2': {'k3': 4, 'k5': 5}}
_DD_3 = {'k1': {'-': 1,
                '+': {'k6': {'': 6},
                      'k7': {'': 7}
                      }
                },
         'k2': {'': {'k3': {'-': 3, '+': 4},
                     'k4': {'-': 4},
                     'k5': {'+': 5}
                     }
                }
         }

_D1_4 = {'k1': 1, 'k2': {'k3': 3, 'k4': 4}}
_D2_4 = {'k1': 1, 'k2': 22}
_DD_4 = {'k1': {'': 1},
         'k2': {'-': {'k3': {'': 3},
                      'k4': {'': 4}
                      },
                '+': 22
                }
         }

GET_DIFF_DICT_TS = [((_D1_1, _D2_1), _DD_1),
                    ((_D1_2, _D2_2), _DD_2),
                    ((_D1_3, _D2_3), _DD_3),
                    ((_D1_4, _D2_4), _DD_4)
                    ]

FIRST_SECOND_STYLISH_DIFF = \
    open('./tests/fixtures/first-second-stylish-diff.txt').read()
DEEP_FIRST_SECOND_STYLISH_DIFF = \
    open('./tests/fixtures/deep-first-second-stylish-diff.txt').read()
DEEP_FIRST_SECOND_PLAIN_DIFF = \
    open('./tests/fixtures/deep-first-second-plain-diff.txt').read()
FIRST_SECOND_JSON_DIFF = \
    open('./tests/fixtures/first-second-json-diff.json').read()
DEEP_FIRST_SECOND_JSON_DIFF = \
    open('./tests/fixtures/deep-first-second-json-diff.json').read()


GEN_STYLISH_DIFF_TS = [
    (('./tests/fixtures/first.json', './tests/fixtures/second.json'),
     FIRST_SECOND_STYLISH_DIFF),
    (('./tests/fixtures/first.yaml', './tests/fixtures/second.yaml'),
     FIRST_SECOND_STYLISH_DIFF),
    (('./tests/fixtures/first.yml', './tests/fixtures/second.yml'),
     FIRST_SECOND_STYLISH_DIFF),
    (('./tests/fixtures/first.json', './tests/fixtures/second.yaml'),
     FIRST_SECOND_STYLISH_DIFF),
    (('./tests/fixtures/deep-first.yaml', './tests/fixtures/deep-second.json'),
     DEEP_FIRST_SECOND_STYLISH_DIFF)
]

GEN_PLAIN_DIFF_TS = [
    (('./tests/fixtures/deep-first.json', './tests/fixtures/deep-second.json'),
     DEEP_FIRST_SECOND_PLAIN_DIFF)
]

GEN_JSON_DIFF_TS = [
    (('./tests/fixtures/deep-first.json', './tests/fixtures/deep-second.json'),
     DEEP_FIRST_SECOND_JSON_DIFF),
    (('./tests/fixtures/first.json', './tests/fixtures/second.json'),
     FIRST_SECOND_JSON_DIFF)
]
