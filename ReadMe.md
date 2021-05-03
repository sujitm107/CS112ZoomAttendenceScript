## CS 112 Python Script Tallier

This script takes in zoom reports can be found in Zoom: Reports > Usage > Select Date Range. Make sure when you downloadthe csv you have unique names selected.

Please create a directory for each section and place all the reports in that directory. In addition, in order to run, make sure you have Pandas installed, as it is used to read the csvs.

## How To Run

`python3 attendence.py <DirectoryName> <SHORT / LONG>`

When LONG is specified all the csv in which that username was found will be printed out, so it might be useful to name your csvs by the date. When SHORT is specified only the total attendence count will be displayed.

Example:
`python3 attendence.py Section12 SHORT`
