# switchWpctlDefaultSinkByName 
<h1>switchSinkToAnalog</h1>
Allows changing the default sink set on wpctl to Analog by name - in this case, if it starts with 'Built-in' phrase. Based on the script made by Sebastiaan76: https://github.com/Sebastiaan76/waybar_wireplumber_audio_changer/tree/main

The script fetches the ID of the sink that starts with 'Built-in' phrase, after switches the default sink using that id, like you would normally do with:
<code>wpctl set-default &lt;sinkID&gt;</code>

Useful when assigning the keybinding - instead of manually seeking to find the id of demanded sink in order to switch to it, you can assign a keybinding to run this script that does it automatically.

<h2>Running the script</h2>
<code>python3 switchSinkToAnalog.py</code>
