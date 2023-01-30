# System Monitoring Recorder

Monitors the system (cpu, memory, disk, network, process) and records it in a log file
Like the linux top command but recording it in a log file and cross platform

```sh
python3 -m venv venv
source venv/bin/activate 
pip install -r requirements.txt
pyinstaller --onefile monitor.py
```

# Use
```sh
# windows
monitor.exe 
montor.exe --help
montor.exe --interval 5
```

```sh
 # linux
python3 monitor.py 
python3 monitor.py --help
python3 monitor.py --interval 5 # linux
```
