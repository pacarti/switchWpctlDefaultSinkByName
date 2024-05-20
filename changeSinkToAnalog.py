#!/usr/bin/env python
import subprocess


# function to parse output of command "wpctl status" and return a dictionary of sinks with their id and name.
def parse_wpctl_status():
    # Execute the wpctl status command and store the output in a variable.
    output = str(subprocess.check_output("wpctl status", shell=True, encoding='utf-8'))

    # remove the ascii tree characters and return a list of lines
    lines = output.replace("├", "").replace("─", "").replace("│", "").replace("└", "").splitlines()

    # get the index of the Sinks line as a starting point
    sinks_index = None
    for index, line in enumerate(lines):
        if "Sinks:" in line:
            sinks_index = index
            break

    # return sinks_index

    # start by getting the lines after "Sinks:" and before the next blank line and store them in a list
    sinks = []
    for line in lines[sinks_index +1:]:
        
        if not line.strip():  # line.strip() is empty when there is no characters in the line or only whitespaces. Then, in boolean context it is treated as False. So the break executes when it's negation is gives True.
            break

        # print(line)
        sinks.append(line.strip())

    # return sinks

    # remove the "[vol:" from the end of the sink name
    for index, sink in enumerate(sinks):
        sinks[index] = sink.split("[vol:")[0].strip() # split on "[vol:", take the first element([0]) of the list and remove the whitespaces(strip)
        # print(sinks[index])

    # strip the * from the default sink and instead append "- Default" to the end. Looks neater in the wofi list this way.
    for index, sink in enumerate(sinks):
        if sink.startswith("*"):
            # print(sink.strip().replace('*', '').strip() + ' - Default')
            sinks[index] = sink.strip().replace("*", "").strip() + " - Default"    

    # make the dictionary in this format {'sink_id': <int>, 'sink_name': <str>}
    # sinks_dict = [{"sink_id": int(sink.split(".")[0]), "sink_name": sink.split(".")[1].strip()} for sink in sinks]
    sinks_dict = [{int(sink.split(".")[0]): sink.split(".")[1].strip()} for sink in sinks]

    return sinks_dict

def detectAnalogID(sinks_dict):
    for sink in sinks_dict:
        for k, v in sink.items():
            # print(str(k) + ': ' + v)
            if str(v).startswith('Built-in'):
                analog_id = k
                return analog_id

# print(parse_wpctl_status())


sinks_dict = parse_wpctl_status()

analog_id = detectAnalogID(sinks_dict)

# print(analog_id)

subprocess.run('wpctl set-default ' + str(analog_id), shell=True, encoding='utf-8')
# subprocess.run("wpctl set-default 48", shell=True, encoding='utf-8')
