# cmdmine functions

Cmdmine managed three resources:

1. Issues
2. Logs
3. Macros

and there exist functions for manipulating each. Below are descriptions
of each of the functions available for each resource.

Note that all functions will be invoked via a command of the form

    cmdmine <action> <resource> [-arg1 value1] [-arg2 value2] [...]

## Issues

Function | Description
---------|------------
new      | Create a new issue in a project
list     | Show a list of existing issues in a project
update   | Update an issue's information
delete   | Close an issue

## Logs

Function | Description
---------|------------
new      | Create a new time log, reporting work done
list     | Show logs created until now
update   | Not implemented
delete   | Not implemented

## Macros

Function | Description
---------|------------
new      | Create a new macro for an issue
list     | Show all recorded macros
update   | Not implemented
delete   | Delete a macro no longer used
