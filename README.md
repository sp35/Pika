<h1>Setup</h1>

<h3>Clone the repository</h3>
<pre>git clone https://github.com/sp35/Pika.git</pre>
<h3>Shift to the project repository</h3>
<pre>cd Pika/</pre>

<h3>Make a new Virtual Environment and activate it</h3>
<pre>virtualenv -p python3 venv
source venv/bin/activate</pre>

<h3>Install the required modules</h3>
<pre>pip install -r requirements.txt</pre>

<h3>Add your channel's keys in keyconfig.py</h3>
<pre>
TBOT_TOKEN = "________ BOT TOKEN ________"
TBOT_CHAT_ID = ["________ CHAT ID 1________", "________ CHAT ID 2 ________"]
</pre>

<h3>Run the script (root access required)</h3>
<pre>sudo venv/bin/python main.py</pre>
