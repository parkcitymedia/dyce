#!/bin/python3
import random
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):
### todo: get the rolled number actually in the window, not just output to the console.

    def __init__(self):
        Gtk.Window.__init__(self, title="DYCE Tabletop")
        self.box = Gtk.Box(spacing=0)
        self.add(self.box)
        # dice buttons
        ## Coin (50/50, 2 faces)
	coin = ["heads","tails"]
	self.c2 = Gtk.Button(label="Coin")
	self.c2.connect("clicked", self.cointoss)
	## D4
        self.d4 = Gtk.Button(label="D4")
        self.d4.connect("clicked", self.rd4)
        ## D6
        self.d6 = Gtk.Button(label="D6")
        self.d6.connect("clicked", self.rd6)
        ## D8
        self.d8 = Gtk.button(label="D8")
        self.d8.connect("clicked", self.rd8)
	## D12
	self.d12 = Gtk.Button(label="D12")
	self.d12.connect("clicked", se
	# organize and display buttons
        self.box.pack_start(self.d4, True, True, 0)
        self.box.pack_start(self.d6, True, True, 0)
        self.box.pack_start(self.d8, True, True, 0)
        self.box.pack_start(self.d10, True, True, 0)
        self.box.pack_start(self.d12, True, True, 0)
        self.box.pack_start(self.p100, True, True, 0)
        self.box.pack_start(self.c2, True, True, 0)

    def rd4(self, widget):
        rollnum = int(rand.randint(1, 4))

    def rd6(self, widget):
        rollnum = int(random.randint(1, 6))
        print(rollnum)
    
    def rd20(self, widget):
        rollnum = int(random.randint(1, 20))
        print(rollnum)
    


w = MyWindow()
w.connect("destroy", Gtk.main_quit)
w.show_all()
Gtk.main()
