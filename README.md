# <img src='https://github.com/iamstrawberry/pyTeX/blob/02fec35101cd3c34312182baf978620b0b024388/logo.ico' height='26'> <b>pyTeX</b>
<h6>a console-based text editor</h6>

#### Requirements:
- Python
- Two brain cells

#### How to setup
- **Step 1:** Clone/download this repo


      git clone https://github.com/iamstrawberry/pyTeX


- **Step 2:** Change directory to pyTeX


      cd pyTeX
      

- **Step 3:** run `start.bat`


      start.bat      
      
### Info
some basic info about using pyTeX text editor.
#### Config system
pyTeX has a config system for customizing commands.<br>
All configurations are stored in `config.json`
> If there is no such file as `config.json`, A new file is generated with **default** settings.<br>The config file is always stored in the same folder as the main script.

These are the contents with default settings in `config.json`
```json
{
    "prefix": "$",
    "commands": {
        "info": ["i", "info"],
        "quit": ["q", "quit"],
        "open": ["o", "open"],
        "save": ["w", "s", "save"],
        "show": ["z", "show"],
        "clear": ["x", "clear"],
        "goto": ["g", "gt", "goto"],
        "help": ["h", "help"]
    }
}
```
- **prefix:** It is used to indicate the beginning of a command.
> **Tip -** It is best to keep the prefix as a symbol that isnt common yet easy to reach. eg: $, !, ~, etc.
- **commands:** list of instructions that you can use to interact with pyTeX and perform various actions. As of version `0.5` there are **8** commands. They are:

| •  | Name  | Description                     | Default Commands |
|----|-------|---------------------------------|------------------|
| 1. | Info  | Gives basic info                | $i, $info        |
| 2. | Quit  | Quits the editor                | $q, $quit        |
| 3. | Open  | Opens a local file              | $o, $open        |
| 4. | Save  | Saves the file content          | $w, $s, $save    |
| 5. | Show  | Shows the file content          | $z, $show        |
| 6. | Clear | Clears the file content         | $x, $clear       |
| 7. | Goto  | Goes to the specified line      | $g, $gt, $goto   |
| 8. | Help  | Displays all available commands | $h, $help        |

> **Tip -** It is best to leave the first prefixes for commands as it is.
<h6 align='right'>by iamstrawberry</h6>
