<h1>Setup</h1>

<h3>Make a new Virtual Environment and activate it</h3>
<pre>virtualenv -p python3 venv
source venv/bin/activate</pre>

<h3>Install the required modules</h3>
<pre>pip install -r requirements.txt</pre>

<h3>Add your channel's keys in keyconfig.py</h3>
<pre>
TBOT_TOKEN = "________ BOT TOKEN ________"
TBOT_CHAT_ID = "________ CHAT ID ________"
</pre>

<h3>Run the script (root access required)</h3>
<pre>sudo venv/bin/python main.py</pre>
