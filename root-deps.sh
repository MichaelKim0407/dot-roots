#!/bin/bash

sudo apt-rdepends --dotty $(apt list --installed | grep -oP "^.+?(?=/)") | ./dot-roots.py
