# cmdmine
A simple command-line interface to enough Redmine functionality to easily log work activity


# Configuration

## redmine-location

The URL of your redmine instance.

## redmine-username

Your redmine username.

## redmine-password

Your redmine password.

## redmine-projects

Mapping of shorthand aliases to project names.
For example, for a project named 'internal-management-tool', you could have an entry:

    'intmanage': 'internal-management-tool'

Remember to separate entries with commas!

## activities

A Mapping of activity names to their identifiers.
You can create an alias or provide whatever name you want for an activity
as long as you map to the same ID. For example, you could have another entry

    'dev': 9

to provide a shorthand way of referring to development activity.

## trackers

A mapping of tracker names to their identifiers.
You can create an alias for a tracker name (or provide whatever name you want)
Just as you can with `activities`.

## default-tracker

The default tracker to use for new tasks.
Must be one of the keys (words on the LEFT of ':') in `trackers`.

## priorities

A mapping of priority names to their identifier.
Aliases and names work just as with `trackers` and `activities`.

## default-priority

The default priority to use for new tasks.
Must be ones of the keys (words on the LEFT of ':') in `priorities`.

## assignee-me

The `<< me >>` identifier to assign yourself to a task.

## new-task-status

The identifier of the default status to use for new tasks.
