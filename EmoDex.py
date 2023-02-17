import os
import argparse
import requests

banner = """
███████╗███╗   ███╗ ██████╗       ██████╗ ███████╗██╗  ██╗
██╔════╝████╗ ████║██╔═══██╗      ██╔══██╗██╔════╝╚██╗██╔╝
█████╗  ██╔████╔██║██║   ██║█████╗██║  ██║█████╗   ╚███╔╝ 
██╔══╝  ██║╚██╔╝██║██║   ██║╚════╝██║  ██║██╔══╝   ██╔██╗ 
███████╗██║ ╚═╝ ██║╚██████╔╝      ██████╔╝███████╗██╔╝ ██╗
╚══════╝╚═╝     ╚═╝ ╚═════╝       ╚═════╝ ╚══════╝╚═╝  ╚═╝
               Made with <3 by @mkdirlove
"""

def translate_to_english(text):
    lang = detect(text)
    if lang != 'en':
        translator = Translator(to_lang='en', from_lang=lang)
        return translator.translate(text)
    else:
        return text

def analyze_emotions(sentence):
    sentence = translate_to_english(sentence)

    url = "https://emodex-emotions-analysis.p.rapidapi.com/rapidapi/emotions"

    payload = {"sentence": sentence}
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "18140c0733msh4177590f10ca716p1ba0c8jsnd344b761be19",
        "X-RapidAPI-Host": "emodex-emotions-analysis.p.rapidapi.com"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    data = response.json()
    print("Sentence: ", data["sentence"]["text"])
    print()
    print("Anger: ", data["sentence"]["anger"])
    print("Disgust: ", data["sentence"]["disgust"])
    print("Fear: ", data["sentence"]["fear"])
    print("Joy: ", data["sentence"]["joy"])
    print("Love: ", data["sentence"]["love"])
    print("No Emotion: ", data["sentence"]["noemo"])
    print("Sadness: ", data["sentence"]["sadness"])
    print("Surprise: ", data["sentence"]["surprise"])

def main():
    os.system("clear")
    print(banner)
    parser = argparse.ArgumentParser(description='EmoDex - An AI-based text / emotion analysis tool.')
    parser.add_argument("-s", "--sentence", help="Input sentence to analyze emotions", required=True)
    args = parser.parse_args()

    if not args.sentence:
        parser.print_help()
    else:
        analyze_emotions(args.sentence)

if __name__ == '__main__':
    try:
        from langdetect import detect
        from translate import Translator
    except ImportError:
        print("langdetect and translate is not installed. Installing it now...")
        os.system("python3 -m pip install langdetect translate")
    main()
