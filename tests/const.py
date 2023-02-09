import json

HELP_MESSAGE = open('./tests/fixtures/help-message.txt').read()

FIRST_DICT = json.load(open('./tests/fixtures/first.json'))
SECOND_DICT = json.load(open('./tests/fixtures/second.json'))

FIRST_SECOND_DIFF = open('./tests/fixtures/first-second-diff.txt').read()
FIRST_SECOND_DICT_DIFF = {'- follow': False,
                          '  host': 'hexlet.io',
                          '- proxy': '123.234.53.22',
                          '- timeout': 50,
                          '+ timeout': 20,
                          '+ verbose': True
                          }

TEST_SUITE = [(('./tests/fixtures/first.json', './tests/fixtures/second.json'),
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
