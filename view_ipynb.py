#!/usr/bin/python3

import json
import re
import sys

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import TerminalFormatter

def escape_ansi(line):
    ansi_escape = re.compile(r'(?:\x1B[@-_]|[\x80-\x9F])[0-?]*[ -/]*[@-~]')
    return ansi_escape.sub('', line)

def escape_ansi_len(line):
    ansi_escape = re.compile(r'(?:\x1B[@-_]|[\x80-\x9F])[0-?]*[ -/]*[@-~]')
    return len(ansi_escape.sub('', line))

   
def text_in_box(text: str, box_width: int=0, max_line_len: int=0) -> str:
    lines = text.split("\n")
    
    max_len = max(escape_ansi_len(line) for line in lines)
    max_len = max(box_width, max_len)
    top_line = "┌" + "─" * (max_len) + "┐"
    inner_lines = "\n".join("│" + line + " " * (max_len - escape_ansi_len(line)) + "│" for line in lines)
    bottom_line = ("└" + "─" * (max_len) + "┘")
    return top_line + "\n" + inner_lines + "\n" + bottom_line
    



with open(sys.argv[1], "r", encoding="utf8") as f:
    j = json.load(f)
    
terminal_formatter = TerminalFormatter()
python_lexer = PythonLexer()

for code in j["cells"]:
    print("\n" + "_"*50)
    source = "".join(code["source"])
    highlighted_source = highlight(source, python_lexer, terminal_formatter)
    print(text_in_box(highlighted_source, max_line_len=80))
