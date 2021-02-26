# Setup

### Clone the repository
```git clone https://github.com/sp35/Pika.git```
### Shift to the project repository
```cd Pika/```

### Make a new Virtual Environment and activate it
```bash
virtualenv -p python3 venv
source venv/bin/activate
```

### Install the required modules
```pip install -r requirements.txt```

### Add your channel's keys in `keyconfig.py`
```python
TBOT_TOKEN = "________ BOT TOKEN ________"
TBOT_CHAT_ID = ["________ CHAT ID 1________", "________ CHAT ID 2 ________"]
```

### Run the script (root access required)
```sudo venv/bin/python main.py```

## Output
```
(venv) ~/Projects/Pika$ sudo venv/bin/python main.py [sudo] password for user: 
Press Shift+F1 anytime to take a ss
Press Ctrl+C to quit
Image saved at ss/pic_61e9c554-37f3-4a87-8802-dbfe58bdd82b.png
File Uploaded to Channel
```

# Optional
### Run in background (root access required)
```sudo ./pika_bg.bash```

## Output
```
~/Projects/Pika $ sudo ./pika_bg.bash
start?  y
end?    n
y
Starting...
Started 2920618
```
```
~/Projects/Pika $ sudo ./pika_bg.bash
start?  y
end?    n
y
Killing prev process...
Killed 2920618

Starting...
Started 2920689
```
```
~/Projects/Pika $ sudo ./pika_bg.bash
start?  y
end?    n
n
Ending...

Killing prev process...
Killed 2920689
```
