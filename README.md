# Jupview, a simplistic terminal jupyter notebook viewer


Jupview is a terminal-based Jupyter notebook viewer that allows you to view the contents of Jupyter notebooks in the terminal without the need to launch a browser.

## Installation

To install Jupview, use the following command:

```pip install jupview```


After installing the package, you need to ensure that ~/.local/bin is included in your system's PATH. This allows your terminal to recognize the jupview command.

If you're using bash as your shell, you can add the path to your PATH environment variable by adding the following line to your ~/.bashrc file:



```export PATH=$PATH:~/.local/bin```


Don't forget to source your ~/.bashrc or restart your terminal session for changes to take effect.

shell

```source ~/.bashrc```

## Usage

To open a Jupyter notebook using Jupview, simply run the following command:


jupview <path to .ipynb file>

This will open the .ipynb file in the terminal where you can view its contents and interact with cells using the keyboard.

This will open the notebook in the terminal, displaying the content with syntax highlighting. You can navigate the notebook using the arrow keys. To exit the viewer, simply press 'q'.
