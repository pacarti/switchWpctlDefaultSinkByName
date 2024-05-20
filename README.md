# switchWpctlDefaultSinkByName 
Allows changing the default sink set on wireplumber by name. Based on the script made by Sebastiaan76: https://github.com/Sebastiaan76/waybar_wireplumber_audio_changer/tree/main

Useful when assigning the keybinding - instead of manually seeking to find the id of demanded sink in order to switch to it, you can assign a keybinding to run this script that does it automatically.

The script fetches the ID of the demanded sink, after switches the default sink using that id, like you would normally do with:<br>
<code>wpctl set-default &lt;sinkID&gt;</code>
<br><br>
<h1>switchSinkToAnalog</h1>
Allows changing the default sink set on wpctl to Analog - in this case, if it starts with 'Built-in' phrase. 

<h2>Running the script</h2>
<code>python3 switchSinkToAnalog.py</code>
<br><br><br>
<h1>switchSinkToHDMI</h1>
Allows changing the default sink set on wpctl to HDMI - in this case, if it starts with 'Baffin' phrase. 

<h2>Running the script</h2>
<code>python3 switchSinkToHDMI.py</code>
