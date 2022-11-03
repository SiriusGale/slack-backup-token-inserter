import json
import sys


default_incorrect_messages_filename = './incorrect_messages.json'
default_correct_messages_filename = './correct_messages.json'


def convert_incorrect_messages_to_correct(tokenstring, incorrect_messages_filename, correct_messages_filename):
    with open(incorrect_messages_filename) as f:
        messages = json.load(f)

    for m in messages:
        if 'files' in m:
            for f in m['files']:
                for k in f:
                    if type(f[k]) == str and f[k].startswith('https://files.slack.com/'):
                        f[k] = f[k] + tokenstring

    with open(correct_messages_filename, 'w') as f:
        json.dump(messages, f)

if __name__ == '__main__':
    args_len = len(sys.argv)
    tokenstring = sys.argv[1]
    incorrect_messages_filename = default_incorrect_messages_filename if args_len <= 2 else sys.argv[2]
    correct_messages_filename = default_correct_messages_filename if args_len <= 3 else sys.argv[3]

    convert_incorrect_messages_to_correct(tokenstring, incorrect_messages_filename, correct_messages_filename)
