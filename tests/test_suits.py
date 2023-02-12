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

NORM_VAL_TS = [(1, 1), ({'a': 1, 'b': 2}, {('', 'a'): 1, ('', 'b'): 2}),
               ({'a': 1, 'k': {'b': 2, 'd': 3}},
                {('', 'a'): 1, ('', 'k'): {('', 'b'): 2, ('', 'd'): 3}}
                )
               ]

_D1_1 = {'k1': 1, 'k2': 2, 'k3': 3}
_D2_1 = {'k2': 2, 'k3': 33, 'k4': 5}
_DD_1 = {('-', 'k1'): 1,
         ('', 'k2'): 2,
         ('-', 'k3'): 3,
         ('+', 'k3'): 33,
         ('+', 'k4'): 5
         }
_DD_1_STR = ('{\n'
             '  - k1: 1\n'
             '    k2: 2\n'
             '  - k3: 3\n'
             '  + k3: 33\n'
             '  + k4: 5\n'
             '}'
             )

_D1_2 = {'k1': 1, 'k2': {'k3': 3, 'k4': 4}}
_D2_2 = {'k1': 1, 'k2': {'k3': 4, 'k5': 5}}
_DD_2 = {('', 'k1'): 1,
         ('', 'k2'): {('-', 'k3'): 3,
                      ('+', 'k3'): 4,
                      ('-', 'k4'): 4,
                      ('+', 'k5'): 5
                      }
         }
_DD_2_STR = ('{\n'
             '    k1: 1\n'
             '    k2: {\n'
             '      - k3: 3\n'
             '      + k3: 4\n'
             '      - k4: 4\n'
             '      + k5: 5\n'
             '    }\n'
             '}'
             )

_D1_3 = {'k1': 1, 'k2': {'k3': 3, 'k4': 4}}
_D2_3 = {'k1': {'k6': 6, 'k7': 7}, 'k2': {'k3': 4, 'k5': 5}}
_DD_3 = {('-', 'k1'): 1,
         ('+', 'k1'): {('', 'k6'): 6,
                       ('', 'k7'): 7
                       },
         ('', 'k2'): {('-', 'k3'): 3,
                      ('+', 'k3'): 4,
                      ('-', 'k4'): 4,
                      ('+', 'k5'): 5
                      }
         }
_DD_3_STR = ('{\n'
             '  - k1: 1\n'
             '  + k1: {\n'
             '        k6: 6\n'
             '        k7: 7\n'
             '    }\n'
             '    k2: {\n'
             '      - k3: 3\n'
             '      + k3: 4\n'
             '      - k4: 4\n'
             '      + k5: 5\n'
             '    }\n'
             '}'
             )


_D1_4 = {'k1': 1, 'k2': {'k3': 3, 'k4': 4}}
_D2_4 = {'k1': 1, 'k2': 22}
_DD_4 = {('', 'k1'): 1,
         ('-', 'k2'): {('', 'k3'): 3,
                       ('', 'k4'): 4
                       },
         ('+', 'k2'): 22
         }
_DD_4_STR = ('{\n'
             '    k1: 1\n'
             '  - k2: {\n'
             '        k3: 3\n'
             '        k4: 4\n'
             '    }\n'
             '  + k2: 22\n'
             '}'
             )


GET_DICT_DIFF_TS = [((_D1_1, _D2_1), _DD_1),
                    ((_D1_2, _D2_2), _DD_2),
                    ((_D1_3, _D2_3), _DD_3),
                    ((_D1_4, _D2_4), _DD_4)
                    ]


FORMAT_DIFF_TS = [(_DD_1, _DD_1_STR),
                  (_DD_2, _DD_2_STR),
                  (_DD_3, _DD_3_STR),
                  (_DD_4, _DD_4_STR)
                  ]

FIRST_SECOND_DIFF = open('./tests/fixtures/first-second-diff.txt').read()
DEEP_FIRST_SECOND_DIFF = \
    open('./tests/fixtures/deep-first-second-diff.txt').read()

GET_JSON_DIFF_TS = [
    (('./tests/fixtures/first.json', './tests/fixtures/second.json'),
     FIRST_SECOND_DIFF),
    (('./tests/fixtures/first.yaml', './tests/fixtures/second.yaml'),
     FIRST_SECOND_DIFF),
    (('./tests/fixtures/first.yml', './tests/fixtures/second.yml'),
     FIRST_SECOND_DIFF),
    (('./tests/fixtures/first.json', './tests/fixtures/second.yaml'),
     FIRST_SECOND_DIFF),
    (('./tests/fixtures/first.yaml', './tests/fixtures/second.json'),
     FIRST_SECOND_DIFF),
    (('./tests/fixtures/first.json', './tests/fixtures/second.yml'),
     FIRST_SECOND_DIFF),
    (('./tests/fixtures/first.yml', './tests/fixtures/second.yaml'),
     FIRST_SECOND_DIFF)
]
