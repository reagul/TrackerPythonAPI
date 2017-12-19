# TrackerPythonAPI

This is a (very) simple [Flask](http://flask.pocoo.org/) application that shows how to construct Pivotal Tracker API. 

To deploy this app on PCF type from within the folder.

```
cf push 

```

Use PCF manifest is within this repo or create your own.


To start with if you want to automate Tracker output into a DB / Store, you will iterate over all Projects in your space.

## Get Projects { /projects }

https://www.pivotaltracker.com/services/v5/projects

## Get Stories { /stories }

https://www.pivotaltracker.com/services/v5/
