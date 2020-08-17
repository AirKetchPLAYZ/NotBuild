# Addons
default addons for NotBuild. Feel free to add any for any languages  
Addons can do anything, they are given a CSVreader of the project and return a list of commands to run.  
The build system will run the addon in the project dir but will run the commands in the build dir  
Because of this, make sure you use absolute paths in the commands you return, except for the output files  
The addon must also have an id  
See CBuild.py for a basic example  
