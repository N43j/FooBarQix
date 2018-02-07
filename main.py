"""Script dedicated to the first step of the FooBarQix kata (http://codingdojo.org/kata/FooBarQix)."""

from model import *

foo_bar_qix = FooBarQix( )
for number in range( 0, 101 ):
  print( foo_bar_qix.transcribe( number ) )