import os
import json
import math
import pickle

CMDMINE_DIR = os.sep.join([os.environ['HOME'], '.cmdmine'])
MACROS_FILE = os.sep.join([CMDMINE_DIR, 'macros.dat'])
ACTIVITY_FILE = os.sep.join([CMDMINE_DIR, 'activities.log'])
NEW_ACT_FILE = os.sep.join([CMDMINE_DIR, 'activities.json'])
NEW_MACROS_FILE = os.sep.join([CMDMINE_DIR, 'macros.json'])

'''
Convert macros from the old dictionary form
    { MACRO: { 'issue_id': <int>, 'project_name': <str> }}
To JSON format since pickling sucks and isn't user-friendly.
'''
def convert_macros():
    macros = pickle.loads(open(MACROS_FILE, 'r').read())
    json_macros = json.dumps(macros)
    open(NEW_MACROS_FILE, 'w').write(json_macros)
    print('Created new file', NEW_MACROS_FILE, 'for JSON-formatted macros.')
    os.remove(MACROS_FILE)
    print('Removed old file', MACROS_FILE, '.')


'''
Convert the old nasty plaintext activity logs where each entry was of the form
    <DATE> <TIME>@@<NUM_HOURS>@@<PROJECT> issue #<ISSUE_ID>@@<TYPE>
    Issue: <ISSUE_NAME>
    Comment: <LOG_COMMENT>
To a much more programmer-friendly JSON format
    [
        {
            "date": <DATE>,
            "time": <TIME>,
            "hours": <HOURS>,
            "minutes": <MINUTES>,
            "projectName": <PROJECT>,
            "issueId": <ISSUE_ID>,
            "issueName": <ISSUE_NAME>,
            "commitType": <TYPE>,
            "comment": <LOG_COMMENT>
        },
    ]
Note that the previously-used log format stored committed time as a float,
so 1 hour, 30 minutes = 1.5 hours.  This function will handle converting
such numbers into the preferrable hour, minute format.
'''
def convert_logs():
    # Read log file lines but strip out empty lines so that it's easier to handle
    # and so that we don't run into problems in case a log comment has an endline.
    lines = [line.replace('\n', '') 
                 for line in open(ACTIVITY_FILE).readlines()
                 if len(line) > 1]
    # Each log is kind of like a three-line triplet, so let's group them as such
    triplets = [(lines[i], lines[i + 1], lines[i + 2])
                for i in range(0, len(lines), 3)]
    json_formatted = []
    for triplet in triplets:
        date_time, total_hours, issue_info, _type = triplet[0].split('@@')
        new_log = {}
        new_log['date'] = date_time.split()[0]
        new_log['time'] = date_time.split()[1]
        total_hours = float(total_hours.split()[0])
        hours = int(math.floor(total_hours))
        minutes = int((total_hours - hours) * 60)
        new_log['hours'] = hours
        new_log['minutes'] = minutes
        project_name, _, issue_number = issue_info.split()
        new_log['projectName'] = project_name
        new_log['issueId'] = int(issue_number.replace('#', ''))
        new_log['commitType'] = _type
        new_log['issueName'] = ' '.join(triplet[1].split()[1:]) # Strip out prefixing "Issue: "
        new_log['comment'] = ' '.join(triplet[2].split()[1:]) # Strp out prefixing "Comment: "
        json_formatted.append(new_log)
    open(NEW_ACT_FILE, 'w').write(json.dumps(json_formatted))
    print('Created new file', NEW_ACT_FILE, 'for JSON-formatted logs.')
    os.remove(ACTIVITY_FILE)
    print('Removed old file', ACTIVITY_FILE, '.')

if __name__ == '__main__':
    convert_macros()
    convert_logs()
