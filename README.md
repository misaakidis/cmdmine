# cmdmine
A simple command-line interface to enough Redmine functionality to easily log work activity

## Installation

The first thing to do to install cmdmine is to clone its repository to your computer and
edit the configuration file.  The `Configuration` section of this document explains the
significance of each setting.  Note that, for project, the key you provide can be anything.
If you have a project called `my_awesome_vacation`, you can add an entry to `redmine-projects`
like the following:

    "vacation": "my_awesome_vacation"

Also note that the project name that appears on the right side of the colon (':') can be
obtained from the URL of the project page on redmine.  For example,

    https://www.redmine.mysite.com/redmine/project/my_awesome_vacation

After you've finished editing the configuration file, providing crucial information such
as the URL to where your redmine instance is located as well as your username and password,
you will have to install the Python libraries that cmdmine depends on to work.

    sudo pip install python-redmine click

Finally, you can run the install script to automatically install cmdmine system-wide. This must be done
as root.

    sudo sh install.sh

With that, you're done! You can now start using cmdmine like a standard Unix utility.

## Usage

cmdmine is designed to make keeping redmine updated with your activity just as easy as
maintaining a simple log of your efforts.  By eliminating the extra procedure of updating
redmine based on recorded logs and reducing context-switching for developers who may be
spending a lot of time in a terminal anyway, cmdmine aims to improve your productivity
substantially.


cmdmine will provide useful help information like any standard Unix
tool so that you can quickly understand any of the commands and the options available
to them.  For instance, to see a list of commands available, simply run

    cmdmine

To see a list of options and arguments for a given command, run

    cmdmine <command> --help

cmdmine maintains a log for you in `$HOME/.cmdmine/activities.log` when you log hours with
the `log` command so that you can easily create reports for others or simply to remind
yourself what you've been doing without having to hunt around on redmine.

There are three resources that cmdmine manages for you.

1. Issues - Tasks on redmine for you to complete
2. Logs   - Recordsof your time committed to issues and updates to issues
3. Macros - Shortcut keywords you can use to identify issues instead of id numbers or full names

Note that, for a given resource, all the commands you'll use to do something will be of the form

    cmdmine <action> <resource> [-flag1 value1] [-flag2 value2] [...]

### Issues

Function | Description
---------|------------
new      | Create a new issue in a project
list     | Show a list of existing issues in a project
update   | Update an issue's information
delete   | Close an issue

### Logs

Function | Description
---------|------------
new      | Create a new time log, reporting work done
list     | Show logs created until now
update   | Not implemented
delete   | Not implemented

### Macros

Function | Description
---------|------------
new      | Create a new macro for an issue
list     | Show all recorded macros
update   | Not implemented
delete   | Delete a macro no longer used

## Configuration

### redmine-location

The URL of your redmine instance.

### redmine-api-key

Your personal API key for Redmine.  Obtained under the `API access key` section of the
`My account` page on the right side.

### redmine-projects

Mapping of shorthand aliases to project names.
For example, for a project named 'internal-management-tool', you could have an entry:

    'intmanage': 'internal-management-tool'

Remember to separate entries with commas!

### activities

A Mapping of activity names to their identifiers.
You can create an alias or provide whatever name you want for an activity
as long as you map to the same ID. For example, you could have another entry

    'dev': 9

to provide a shorthand way of referring to development activity.

### trackers

A mapping of tracker names to their identifiers.
You can create an alias for a tracker name (or provide whatever name you want)
Just as you can with `activities`.

### default-tracker

The default tracker to use for new tasks.
Must be one of the keys (words on the LEFT of ':') in `trackers`.

### priorities

A mapping of priority names to their identifier.
Aliases and names work just as with `trackers` and `activities`.

### default-priority

The default priority to use for new tasks.
Must be ones of the keys (words on the LEFT of ':') in `priorities`.

### statuses

The possible statuses that an issue can take on.

### closed-status

The ID of your equivalent of the "closed" status.

### assignee-me

The `<< me >>` identifier to assign yourself to a task.

### new-task-status

The identifier of the default status to use for new tasks.
