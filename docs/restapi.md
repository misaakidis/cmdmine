# cmdmine functions

Cmdmine managed three resources:

1. Issues
2. Logs
3. Macros

and there exist functions for manipulating each. Below are descriptions
of each of the functions available for each resource.

Note that all functions will be invoked via a command of the form

    cmdmine <resource> <function> [-arg1 value1] [-arg2 value2] [...]

## Issues

Function | Description
---------|-------------
new      | Create a new issue in a project
list     | List existing issues in a project
close    | Close an issue
update   | Update an issue's information

## Logs

Function | Description
---------|------------
new      | Create a new time log, reporting work done
list     | Show logs created until now

## Macros
Function | Description
---------|------------
new      | Create a new macro for an issue
delete   | Delete an existing macro
