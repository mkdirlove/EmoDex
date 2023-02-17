<h1 align="center">
  <br>
  <a href="https://github.com/mkdirlove/EmoDex"><img src="https://github.com/mkdirlove/EmoDex/blob/main/logo.png" alt="EmoDex"></a>
  <br>
  An AI-based text / emotion analysis tool.
  <br>
</h1>

#### Installation

Copy-paste this into your terminal:

```
git clone https://github.com/mkdirlove/EmoDex.git
```
```
cd EmoDex
```
```
python3 EmoDex.py -h
```

#### Usage
```
███████╗███╗   ███╗ ██████╗       ██████╗ ███████╗██╗  ██╗
██╔════╝████╗ ████║██╔═══██╗      ██╔══██╗██╔════╝╚██╗██╔╝
█████╗  ██╔████╔██║██║   ██║█████╗██║  ██║█████╗   ╚███╔╝ 
██╔══╝  ██║╚██╔╝██║██║   ██║╚════╝██║  ██║██╔══╝   ██╔██╗ 
███████╗██║ ╚═╝ ██║╚██████╔╝      ██████╔╝███████╗██╔╝ ██╗
╚══════╝╚═╝     ╚═╝ ╚═════╝       ╚═════╝ ╚══════╝╚═╝  ╚═╝
               Made with <3 by @mkdirlove

usage: EmoDex.py [-h] -s SENTENCE

EmoDex - An AI-based text / emotion analysis tool.

optional arguments:
  -h, --help            show this help message and exit
  -s SENTENCE, --sentence SENTENCE
                        Input sentence to analyze emotions
```
#### Sample Usage #1
```
python3 EmoDex.py -s 'I love Python <3'
```
```
███████╗███╗   ███╗ ██████╗       ██████╗ ███████╗██╗  ██╗
██╔════╝████╗ ████║██╔═══██╗      ██╔══██╗██╔════╝╚██╗██╔╝
█████╗  ██╔████╔██║██║   ██║█████╗██║  ██║█████╗   ╚███╔╝ 
██╔══╝  ██║╚██╔╝██║██║   ██║╚════╝██║  ██║██╔══╝   ██╔██╗ 
███████╗██║ ╚═╝ ██║╚██████╔╝      ██████╔╝███████╗██╔╝ ██╗
╚══════╝╚═╝     ╚═╝ ╚═════╝       ╚═════╝ ╚══════╝╚═╝  ╚═╝
               Made with <3 by @mkdirlove

Sentence:  I love Python <3

Anger:  0.03
Disgust:  0.0
Fear:  0.06
Joy:  0.45
Love:  0.3433333333333334
No Emotion:  0.06166666666666667
Sadness:  0.035
Surprise:  0.065
┌
```
