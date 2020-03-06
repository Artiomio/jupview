#!/usr/bin/python3

import json
from math import ceil
import re
import shutil
import sys

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import TerminalFormatter
from pygments.styles import get_style_by_name
get_style_by_name("emacs")



def escape_ansi(line):
    ansi_escape = re.compile(r"(?:\x1B[@-_]|[\x80-\x9F])[0-?]*[ -/]*[@-~]")
    return ansi_escape.sub("", line)


def escape_ansi_len(line):
    ansi_escape = re.compile(r"(?:\x1B[@-_]|[\x80-\x9F])[0-?]*[ -/]*[@-~]")
    return len(ansi_escape.sub("", line))


def text_in_box(
    text: str, box_width: int = 0, max_line_len: int = 0, min_line_len: int = None
) -> str:
    lines = text.split("\n")

    max_len = max(escape_ansi_len(line) for line in lines)
    line_len = max(box_width, max_len)

    if min_line_len is not None:
        line_len = min_line_len - 1

    top_line = "┌" + "─" * (line_len) + "┐"
    inner_lines = "\n".join(
        "│" + line + " " * (line_len - escape_ansi_len(line)) + "│" for line in lines
    )
    bottom_line = "└" + "─" * (line_len) + "┘"
    return top_line + "\n" + inner_lines + "\n" + bottom_line


def limit_python_source_lines(source: str, max_len) -> str:
    lines = source.split("\n")
    new_lines = []
    for line_n, line in enumerate(lines):
        if len(line) > max_len:
            n = ceil(len(line) / max_len)
            lines_cut = [
                line[i * max_len : i * max_len + max_len] + "\\" for i in range(n)
            ]
            new_lines.extend(lines_cut)
        else:
            new_lines.append(line)
    return "\n".join(new_lines)



file_name = sys.argv[1]
with open(file_name, "r", encoding="utf8") as f:
    j = json.load(f)

terminal_formatter = TerminalFormatter()
python_lexer = PythonLexer()




MAX_SYMB_IN_LINE = 80


print(f"Viewing {file_name}:\n")
for code in j["cells"]:
    source = "".join(code["source"])
    if not source.replace("\n", "").replace(" ", ""):
        continue
    
    source = limit_python_source_lines(source, MAX_SYMB_IN_LINE - 2)
    highlighted_source = highlight(source, python_lexer, terminal_formatter)
    print(
        text_in_box(
            highlighted_source,
            max_line_len=MAX_SYMB_IN_LINE,
            min_line_len=MAX_SYMB_IN_LINE,
        )
    )
    print()
