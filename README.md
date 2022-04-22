# SSH PY
```
 ________   ________  ___  ___  ________  ___    ___ 
|\   ____\ |\   ____\|\  \|\  \|\   __  \|\  \  /  /|
\ \  \___|_\ \  \___|\ \  \\\  \ \  \|\  \ \  \/  / /
 \ \_____  \\ \_____  \ \   __  \ \   ____\ \    / / 
  \|____|\  \\|____|\  \ \  \ \  \ \  \___|\/  /  /  
    ____\_\  \ ____\_\  \ \__\ \__\ \__\ __/  / /    
   |\_________\\_________\|__|\|__|\|__||\___/ /     
   \|_________\|_________|              \|___|/
 ```
A ssh host manager for the windows terminal 

![](https://raw.githubusercontent.com/awesomelewis2007/SSHPY/master/documentation/Main.png)

## Setup 
First you need to install python to run this program. 

Then download this repository to a folder on your computer.

Open windows terminal and go to settings.

Click open settings.json.

Paste the following json profile into the settings.json at the bottom of your profile lists.

```json
{
    "commandline": "python <location to main.py file use \\ to define a slash>",
    "hidden": false,
    "icon": "https://cdn3.iconfinder.com/data/icons/logos-and-brands-adobe/512/267_Python-512.png",
    "name": "SSH PY",
    "startingDirectory": "Put this to where you installed SSH PY's main.py file ",
    "tabTitle": "SSH PY"
}
```

On the profile you pasted edit `commandline` to `python` and then the location of the main.py file e.g `python C:\SSHPY\main.py` then do the same on the `startingDirectory` but without the `python` and the `main.py` e.g `C:\SSHPY\`

Then save the profile.

Reopen the terminal and you should be able to see the SSH PY tab with a python icon.

![](https://github.com/awesomelewis2007/SSHPY/blob/master/documentation/Select.png?raw=true)

Now run the program from the drop down menu. It should take you so a setup that asks you for your hosts.

![](https://github.com/awesomelewis2007/SSHPY/blob/master/documentation/Setup.png?raw=true)
