#!/bin/python3


import OS


class ConfigWrapper:

    def __init__(self, *args, **kwargs):
        self.test = 0


    def run(self):
        print(self.test)



def main():
    cm = ConfigWrapper()
    cm.runt()
