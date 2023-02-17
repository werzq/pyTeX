# pyTeX version 0.1 by iamstrawberry

import os

def editor():
    lines = []
    while True:
        # Prompt for a new line or a command
        try:
            command = input((f'[{len(lines)+1}]: '))


            if command.startswith('$'):
            # Handle commands
                if command in ('$h', '$help'):
                    print(info('$h - shows this menu', '$q - quits the editor', '$w - saves the file content', '$z - shows the file content', '$x - clears the file content'))
                elif command in ('$i', '$info'):
                    print(info('pyTeX console editor', 'by iamstrawberry', 'version 0.1'))
                elif command in ('$q', '$quit'):
                    clear_console()
                    exit()
                elif command in ('$w', '$s', '$save'):
                    filename = input(info('Save as: '))
                    with open(filename, 'w') as f:
                        f.write('\n'.join(lines))
                    print(info(f'Saved {len(lines)} lines to {filename}.'))
                elif command in ('$z', '$show'):
                    print('\n' + ('\n'.join(lines)+('\n')))
                elif command in ('$x', '$clear'):
                    lines = []
                else:
                    print(info(f'Unknown command {command}', 'For a list of commands do $h'))

            else:
                # Add a new line
                lines.append(command)

        except KeyboardInterrupt:
            clear_console()
            exit()


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
    print('pyTeX version 0.1\n')
    editor()