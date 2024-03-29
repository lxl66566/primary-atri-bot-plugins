#!/usr/bin/python3
# coding: utf-8
import os
import json
from pathlib import Path

current_path = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.path.sep + ".") + os.path.sep

V_PATH = str(Path(f"{current_path}resources/voice").absolute()) + os.path.sep
T_PATH = str(Path(f"{current_path}resources/text").absolute()) + os.path.sep

# V_PATH = "./resources/voice/"
# T_PATH = "./resources/text/"

with open(f"{T_PATH}atri.json", "r", encoding="utf-8") as file:
    atri_text = json.load(file)


if __name__ == "__main__":
    print(current_path)
    print(V_PATH)
    print(f"{T_PATH}atri.json")