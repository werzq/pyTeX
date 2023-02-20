# pyTeX version 0.5 by iamstrawberry

import os
import sys
import json
import easygui

def init_config():
    default_data = {
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
    
    if os.path.exists("config.json"):
        with open("config.json", "r") as f:
            data = json.load(f)
    else:
        with open("config.json", "w") as f:
            json.dump(default_data, f, indent=(6-2))
        data = default_data
    
    main_prefix = data["prefix"]
    info_prefixes = [main_prefix + prefix for prefix in data["commands"]["info"]]
    quit_prefixes = [main_prefix + prefix for prefix in data["commands"]["quit"]]
    open_prefixes = [main_prefix + prefix for prefix in data["commands"]["open"]]
    save_prefixes = [main_prefix + prefix for prefix in data["commands"]["save"]]
    show_prefixes = [main_prefix + prefix for prefix in data["commands"]["show"]]
    clear_prefixes = [main_prefix + prefix for prefix in data["commands"]["clear"]]
    goto_prefixes = [main_prefix + prefix for prefix in data["commands"]["goto"]]
    help_prefixes = [main_prefix + prefix for prefix in data["commands"]["help"]]
    
    return (main_prefix, info_prefixes, quit_prefixes, open_prefixes, save_prefixes, show_prefixes, clear_prefixes, goto_prefixes, help_prefixes)

def editor():
    lines = []
    while True:
        try:
            command = input((f'[{len(lines)+1}]: '))
            if command.startswith(main_prefix):

                if command in help_prefixes:
                    print(info('|    | Name  | Description                     | Commands',
                               '|----|-------|---------------------------------|',
                               '| 1. | Info  | Gives basic info                | ' + ', '.join(info_prefixes),
                               '| 2. | Quit  | Quits the editor                | ' + ', '.join(quit_prefixes),
                               '| 3. | Open  | Opens a local file              | ' + ', '.join(open_prefixes),
                               '| 4. | Save  | Saves the file content          | ' + ', '.join(save_prefixes),
                               '| 5. | Show  | Shows the file content          | ' + ', '.join(show_prefixes),
                               '| 6. | Clear | Clears the file content         | ' + ', '.join(clear_prefixes),
                               '| 7. | Goto  | Goes to the specified line      | ' + ', '.join(goto_prefixes),
                               '| 8. | Help  | Displays all available commands | ' + ', '.join(help_prefixes)))
                elif command in info_prefixes:
                    print(info('pyTeX console editor', 'by iamstrawberry', 'version 0.5'))
                elif command in quit_prefixes:
                    clear_console()
                    sys.exit()
                elif command in save_prefixes:
                    filename = easygui.filesavebox(default=".txt", filetypes=["*.txt"], title="Save File")
                    if filename:
                        with open(filename, 'w') as f:
                            f.write('\n'.join(lines))
                        file = os.path.split(filename)
                        print(info(f'Saved {len(lines)} lines to {file}.'))
                    else:
                        print(info('Cancelled file save'))
                elif command in show_prefixes:
                    print('\n' + ('\n'.join(lines)+('\n')))
                elif command in clear_prefixes:
                    lines = []
                elif any(command.startswith(prefix) for prefix in goto_prefixes):
                    parts = command.split()
                    if len(parts) != 2:
                        print(info(f'Usage: {goto_prefixes[0]} linenumber'))
                    else:
                        try:
                            linenumber = int(parts[1])
                            if linenumber < 1 or linenumber > len(lines):
                                print(info('Line number out of range.'))
                            else:
                                editor_goto(lines, linenumber)
                        except ValueError:
                            print(info('Invalid line number.'))
                elif command in open_prefixes:
                    filename = easygui.fileopenbox()
                    try:
                        if filename is None:
                            print(info('No file selected'))
                        else:
                            file = os.path.split(filename)
                            with open(filename, 'r') as f:
                                lines = f.readlines().splitlines()
                            print(info(f'Opened {file}'))
                    except FileNotFoundError:
                        print(info(f'File not found: {filename}.'))
                
                else:
                    print(info(f'Unknown command {command}', f'For a list of commands do {help_prefixes[0]}'))
            else:
                lines.append(command)

        except KeyboardInterrupt:
            clear_console()
            sys.exit()

def editor_goto(lines, linenumber):
    line = lines[linenumber-1]
    print(info(f'Editing line {linenumber}: {line}'))
    new_line = input(f'[{linenumber}]: ')
    lines[linenumber-1] = new_line

def info(*messages):
    formatted_messages = []
    for i, message in enumerate(messages):
        if i < len(messages) - 1:
            formatted_messages.append("[i]: " + message)
        else:
            formatted_messages.append("[i]: " + message.rstrip())
    return "\n".join(formatted_messages)

def clear_console():
    os.system('cls' if os.name=='nt' else 'clear')

if __name__ == '__main__':
    clear_console()
    (
        main_prefix,
        info_prefixes,
        quit_prefixes,
        open_prefixes, 
        save_prefixes, 
        show_prefixes, 
        clear_prefixes, 
        goto_prefixes, 
        help_prefixes
    ) = init_config()
    print('pyTeX version 0.5\n')
    editor()