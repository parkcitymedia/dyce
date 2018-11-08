#!/bin/python3
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from random import randint

class MyWindow(Gtk.Window):

    def __init__(self):
        coin = ["heads", "tails"]
        Gtk.Window.__init__(self, title="DYCE Tabletop")
        self.box = Gtk.Box(spacing=0)
        self.add(self.box)
        # dice buttons
        ## Coin (50/50, 2 faces)
        self.c2 = Gtk.Button(label="Coin")
        self.c2.connect("clicked", self.cointoss)
        ## 3point
        self.abc3 = Gtk.Button(label="3-Point")
        self.abc3.connect("clicked", self.r3p)
        ## D4
        self.d4 = Gtk.Button(label="D4")
        self.d4.connect("clicked", self.rd4)
        ## D6
        self.d6 = Gtk.Button(label="D6")
        self.d6.connect("clicked", self.rd6)
        ## D8
        self.d8 = Gtk.Button(label="D8")
        self.d8.connect("clicked", self.rd8)
        ## D12
        self.d12 = Gtk.Button(label="D12")
        self.d12.connect("clicked", self.rd12)
        # organize and display buttons
        self.box.pack_start(self.abc3, True, True, 0)
        self.box.pack_start(self.d4, True, True, 0)
        self.box.pack_start(self.d6, True, True, 0)
        self.box.pack_start(self.d8, True, True, 0)
        self.box.pack_start(self.d10, True, True, 0)
        self.box.pack_start(self.d12, True, True, 0)
        #self.box.pack_start(self.p100, True, True, 0)
        self.box.pack_start(self.c2, True, True, 0)

    def r3p(self, widget):
        print("3-point: ",int(randint(1, 3)))
    
    def rd4(self, widget):
        print("D4: ",int(randint(1, 4)))

    def rd6(self, widget):
        print("D6: ",int(randint(1, 6)))
    
    def rd8(self, widget):
        print("D8: ",int(randint(1, 8)))
    
    def rd10(self, widget):
        print("D10: ",int(randint(1,10))
    
    def rd12(self, widget):
        print("d12: ",int(randint(1,12)))

    def cointoss(self, widget):
        print("Coin Flip: ",coin[randint(0, 1)])

w = MyWindow()
w.connect("destroy", Gtk.main_quit)
w.show_all()
Gtk.main()
