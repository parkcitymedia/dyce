# coding=<UTF-8>
import random
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Dice Util 0.0.1")
        self.box = Gtk.Box(spacing=0)
        self.add(self.box)
        self.d20 = Gtk.Button(label="D20")
        self.d20.connect("clicked", self.rd20)
        self.box.pack_start(self.d20, True, True, 0)
        self.d6 = Gtk.Button(label="D6")
        self.d6.connect("clicked", self.rd6)
        self.box.pack_start(self.d6, True, True, 0)

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