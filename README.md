a playing with the python lib, i enjoy very much this tool https://github.com/pytube/pytube , my implementation is for big playlists, for now only audio but you can change this easily, comands for Linux OS: 
First create a venv:
```bash
python -m venv .venv
```
activate this
```bash
source .venv/bin/activate
```
enter in the directory
```bash
cd pytube_implementation
```

and install the dependencies
```bash
pip install -r requirements.txt
```
For personal playlists paste the links in the links.txt 
 and finally run 
 ```bash
 python3 playlist.py
 ```
if you want dowload only one video use:
```bash
python main.py
```
if you want only one music:
```bash
python audio.py
```
For ready-made playlists
```bash 
python playlist_of_yt.py
```
