#!/usr/bin/python3
import pathlib
import tkinter as tk
import pygubu
from .pygubuexampleui import ExampleAppUI


class ExampleApp(ExampleAppUI):
    def __init__(self, master=None):
        super().__init__(master)

    def clickMe(self):
        pass

def main():
    app = ExampleApp()
    app.run()

if __name__ == "__main__":
    main()
