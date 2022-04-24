## Talk robot
Listen microphone and answer gpt generated text
#### requirements
- [Docker](https://docs.docker.com/engine/install/ubuntu/)
- [Anaconda](https://docs.anaconda.com/anaconda/install/index.html)
#### installation
```
git clone https://github.com/format37/DialoGPT.git
cd DialoGPT
sudo apt install espeak
python3 -m pip install -r requirements.txt
conda install -c anaconda pyaudio
```
#### Run dialogpt docker service:   
```
sh compose.sh
```
#### talk with bot
Connect microphone and in another terminal run:
```
python3 talk.py
```
When message 'say something' appears, say something, and listen for the answer.
