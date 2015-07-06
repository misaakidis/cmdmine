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

### task

    cmdmine task [OPTIONS] PROJECT

The `task` command is used to create a new task for a given project, which you will later
log hours for work on.

The `PROJECT` parameter must be one of the shorthand names of a project (i.e. one of the
keys) in the `redmine-projects` mapping in your configuration file.

### log

    cmdmine log [OPTIONS] ACTIVITY

The `log` command is used to log some number of hours and minutes of work on a given issue.
The issue (task) to log time to can be identified either by the issue's ID (`-i` or `--issue`)
or by a macro name.  If an ID is provided, a project name (`-p` or `--project`) can also be
provided to be included in the log file, but it is not required.  If a macro name is provided
(`-m` or `--macro`), it takes presedence over an issue id.  Thus it typically makes sense to
provide only one.

This command accepts two time values, hours (`-H` or `--hours`), and minutes (`-M` or `--minutes`).
It is recommended that you use both of these flags instead of trying to compute the fractional
number of hours yourself.

The default behavior is to log time on the current day.  In the case that you would like to
log time for another date, the date (`-d` or `--date`) flag can be used. The format for this
option is YYYY-MM-DD.

`log` automatically updates a log file with the activity you enter, so that you can retrieve
a list of logged work without tracking it down on redmine.  More about this in `show`.

### issues

    cmdmine issues [OPTIONS] PROJECT

The `issues` command is used to quickly obtain a list of issues (tasks) in a given project.
Like with the `task` command, `PROJECT` is a shorthand project name- a key in the `redmine-projects`
mapping in your config.  This command limits the amount of output by default, so that you don't end
up with a long list of ancient tasks when you might only want to see the first few.  To override
this behavior, you can use the offset (`-o` or `--offset`) to start listing from an offset from the
most recently created issue and the limit (`-l` or `--limit`) to change the maximum number of
issues to list.

### macro

    cmdmine macro [OPTIONS] MACRO_NAME

The `macro` command is used to associate a name with a particular issue.  Using macros makes it
easier to reference issues that you have been working on without having to remember obscure
issue IDs or frequently list the issues in a project.  The issue (`-i` or `--issue`) option
takes the ID of the issue to create a macro for, and you can use the project (`-p` or `--project`)
option to also provide the project name the issue belongs to in order to make your logs appear
nicer.

### show

    cmdmine show WHAT

The `show` command is used to output locally stored information.  Currently, that can be either
the list of currently recorded macros (their names, along with the associated issue ID and
project name) or it can be the content of the log file storing information about your time logs.
As you might expect, `WHAT` is replaced with `macros` for the former case, and `logs` for the
latter.

## Configuration

### redmine-location

The URL of your redmine instance.

### redmine-username

Your redmine username.

### redmine-password

Your redmine password.

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

### assignee-me

The `<< me >>` identifier to assign yourself to a task.

### new-task-status

The identifier of the default status to use for new tasks.
