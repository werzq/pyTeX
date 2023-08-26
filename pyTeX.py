# pyTeX version 0.6 by iamstrawberry

import os
import sys
import json
import easygui

# Constants and Configurations
CONFIG_FILE = "config.json"
DEFAULT_CONFIG = {
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

# Functions

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    else:
        with open(CONFIG_FILE, "w") as f:
            json.dump(DEFAULT_CONFIG, f, indent=4)
        return DEFAULT_CONFIG

def get_prefixed_commands(data, command_key):
    main_prefix = data["prefix"]
    prefixes = data["commands"][command_key]
    return [main_prefix + prefix for prefix in prefixes]

def show_help(commands):
    help_text = "\nAvailable commands:\n"
    for idx, (command, prefixes) in enumerate(commands.items(), start=1):
        help_text += f"{idx}. {command.capitalize():<10} - {', '.join(prefixes)}\n"
    print(help_text)

def save_lines_to_file(lines, filename):
    with open(filename, 'w') as f:
        f.write('\n'.join(lines))
    print(f"\nSaved {len(lines)} lines to {filename}\n")

def open_file_and_load_lines():
    filename = easygui.fileopenbox()
    if filename:
        with open(filename, 'r') as f:
            lines = f.read().splitlines()
        print(f"\nOpened {filename}\n")
        return lines
    else:
        print("\nNo file selected\n")
        return []

def clear_console():
    os.system('cls' if os.name=='nt' else 'clear')

# Main Editor Function

def editor():
    lines = []
    while True:
        try:
            command = input(f"[{len(lines)+1}]: ")
            if command.startswith(main_prefix):
                if command in commands["help"]:
                    show_help(commands)
                elif command in commands["info"]:
                    print("\npyTeX console editor\nby iamstrawberry\nversion 0.6\n")
                elif command in commands["quit"]:
                    clear_console()
                    sys.exit()
                elif command in commands["save"]:
                    filename = easygui.filesavebox(default=".txt", filetypes=["*.txt"], title="Save File")
                    if filename:
                        save_lines_to_file(lines, filename)
                elif command in commands["show"]:
                    print('\n ' + ('\n '.join(lines)) +'\n')
                elif command in commands["clear"]:
                    lines = []
                elif any(command.startswith(prefix) for prefix in commands["goto"]):
                    parts = command.split()
                    if len(parts) != 2:
                        print(f'\nUsage: {commands["goto"][0]} linenumber\n')
                    else:
                        try:
                            linenumber = int(parts[1])
                            if linenumber < 1 or linenumber > len(lines):
                                print('\nLine number out of range.\n')
                            else:
                                editor_goto(lines, linenumber)
                        except ValueError:
                            print('\nInvalid line number.\n')
                elif command in commands["open"]:
                    lines = open_file_and_load_lines()
                else:
                    print(f'\nUnknown command {command}. For a list of commands do {commands["help"][0]}\n')
            else:
                lines.append(command)

        except KeyboardInterrupt:
            clear_console()
            sys.exit()

def editor_goto(lines, linenumber):
    line = lines[linenumber-1]
    print(f'\nEditing line {linenumber}: {line}\n')
    new_line = input(f'[{linenumber}]: ')
    lines[linenumber-1] = new_line

# Main Execution

if __name__ == '__main__':
    clear_console()
    
    config_data = load_config()
    main_prefix = config_data["prefix"]
    commands = {
        "info": get_prefixed_commands(config_data, "info"),
        "quit": get_prefixed_commands(config_data, "quit"),
        "open": get_prefixed_commands(config_data, "open"),
        "save": get_prefixed_commands(config_data, "save"),
        "show": get_prefixed_commands(config_data, "show"),
        "clear": get_prefixed_commands(config_data, "clear"),
        "goto": get_prefixed_commands(config_data, "goto"),
        "help": get_prefixed_commands(config_data, "help")
    }
    
    print('pyTeX version 0.6\n')
    editor()