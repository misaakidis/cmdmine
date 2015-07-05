# URL of your redmine instance
REDMINE_LOCATION = ''

# Your redmine username
REDMINE_USERNAME = ''

# Your redmine password
REDMINE_PASSWORD = ''

# Mapping of shorthand aliases to project names
# For example, for a project named 'internal-management-tool', you could have an entry
# 'intmanage': 'internal-management-tool'
# Remember to separate entries with commas!
REDMINE_PROJECTS = {
}

# A Mapping of activity names to their identifiers
# You can create an alias or provide whatever name you want for an activity
# as long as you map to the same ID. For example, you could have another entry
# 'dev': 9
# to provide a shorthand way of referring to development activity
ACTIVITIES = {
  'design': 8,
  'development': 9,
  'maintenance': 10,
  'progress': 11,
  'communications': 12
}

# A mapping of tracker names to their identifiers
# You can create an alias for a tracker name (or provide whatever name you want)
# Just as you can with ACTIVITIES
TRACKERS = {
  'bug': 1,
  'feature': 2,
  'support': 3,
  'task': 4
}

# The default tracker to use for new tasks
# Must be one of the keys (words on the LEFT of ':') in TRACKERS
DEFAULT_TRACKER = 'task'

# A mapping of priority names to their identifiers
# Aliases and names work just as with TRACKERS and ACTIVITIES
PRIORITIES = {
  'low': 3,
  'normal': 4,
  'high': 5,
  'urgent': 6,
  'immediate': 7
}

# The default priority to use for new tasks
# Must be one of the keys (words on the LEFT of ':') in PRIORITIES
DEFAULT_PRIORITY = 'normal'

# The '<< me >>' identifier to assign yourself a task
ASSIGNEE_ME = 18

# The identifier of the default status ot use for new tasks
NEW_TASK_STATUS = 1
