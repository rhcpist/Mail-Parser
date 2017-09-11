import re
from collections import Counter

# Return tuple of From, Subject, Date
def parse_string_obj(string):
    prog_from = re.search(r"From:\s*(?P<from>.*.)\n", string).group('from')
    prog_subject = re.search(r"Subject:\s*(?P<subject>.*.)\n", string).group('subject')
    prog_date = re.search(r"Date:\s*(?P<date>\w*[a-zA-Z]{3},.*.)\n", string).group('date')
    return (prog_from, prog_subject, prog_date)

PATH = 'mbox.txt'
message_list = []
str_obj = ''
prog = re.compile(r"From\s*\w.{0,}@\w.{0,}\s*\w*[a-zA-Z]{3}\s\w*[a-zA-Z]{3}\s*\d*\s\d{2}:\d{2}:\d{2}\s*\d{4}")
with open(PATH, 'r', encoding='utf-8') as outfile:
    for line in outfile:
        matched_line = prog.match(line)
        if matched_line and str_obj:
            message_list.append(parse_string_obj(str_obj))
            str_obj = ''
        str_obj += line
    # To insert last message string
    message_list.append(parse_string_obj(str_obj))

# Data in format from (date): subject
for message in sorted(message_list):
    print(message[0] + ' (' + message[2] + '): ' + message[1])

counted_list = Counter(elem[0] for elem in sorted(message_list))

# Count of messages for each sender in format from:quantity
for key, val in counted_list.items():
    print(key + ' : ' + str(val))