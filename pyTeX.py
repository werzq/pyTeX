# pyTeX version 0.3 by iamstrawberry

import os
import easygui

def editor():
    lines = []
    while True:
        try:
            command = input((f'[{len(lines)+1}]: '))
            if command.startswith('$'):
            # Handle commands
                if command in ('$h', '$help'):
                    print(info('|    | Name  | Description                     | Commands      |',
                               '|----|-------|---------------------------------|---------------|',
                               '| 1. | Info  | Gives basic info                | $i, $info     |',
                               '| 2. | Quit  | Quits the editor                | $q, $quit     |',
                               '| 3. | Open  | Opens a local file              | $o, $open     |',
                               '| 4. | Save  | Saves the file content          | $w, $s, $save |',
                               '| 5. | Show  | Shows the file content          | $z, $show     |',
                               '| 6. | Clear | Clears the file content         | $x, $clear    |',
                               '| 7. | Goto  | Goes to the specified line      | $g, $gt, $goto|',
                               '| 8. | Help  | Displays all available commands | $h, $help     |'))
                elif command in ('$i', '$info'):
                    print(info('pyTeX console editor', 'by iamstrawberry', 'version 0.3'))
                elif command in ('$q', '$quit'):
                    clear_console()
                    exit()
                elif command in ('$w', '$s', '$save'):
                    filename = easygui.filesavebox(default=".txt", filetypes=["*.txt"], title="Save File")
                    if filename:
                        with open(filename, 'w') as f:
                            f.write('\n'.join(lines))
                        file = filename.split('\\')[-1]
                        print(info(f'Saved {len(lines)} lines to {file}.'))
                    else:
                        print(info('Cancelled file save'))
                elif command in ('$z', '$show'):
                    print('\n' + ('\n'.join(lines)+('\n')))
                elif command in ('$x', '$clear'):
                    lines = []
                elif command.startswith('$g') or command.startswith('$gt') or command.startswith('$goto'):
                    parts = command.split()
                    if len(parts) == 0:
                        print(info('Usage: $g linenumber'))
                    elif len(parts) != 2:
                        print(info('Usage: $g linenumber'))
                    else:
                        try:
                            linenumber = int(parts[1])
                            if linenumber < 1 or linenumber > len(lines):
                                print(info('Line number out of range.'))
                            else:
                                editor_goto(lines, linenumber)
                        except ValueError:
                            print(info('Invalid line number.'))
                elif command in ('$o', '$open'):
                    filename = easygui.fileopenbox()
                    try:
                        if filename is None:
                            print(info('No file selected'))
                        else:
                            file = filename.split('\\')[-1]
                            with open(filename, 'r') as f:
                                lines = f.read().splitlines()
                            print(info(f'Opened {file}'))
                    except FileNotFoundError:
                        print(info(f'File not found: {filename}.'))
                
                else:
                    print(info(f'Unknown command {command}', 'For a list of commands do $h'))
            else:
                lines.append(command)

        except KeyboardInterrupt:
            clear_console()
            exit()

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
    print('pyTeX version 0.3\n')
    editor()