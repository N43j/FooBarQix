"""Unit tests for :mod:`model`.

* :class:`Test_FooBarQix`
| Unit tests for :class:`~model.FooBarQix`."""

from unittest import TestCase

from model import *

class Test_FooBarQix (TestCase):
  """Unit tests for :class:`~model.FooBarQix`.
  
  * :func:`test_that_3_foo_5_bar_7_qix_transcription_of_92_gives_92`
  | Unit test for :func:`~model.FooBarQix.transcribe`.
  * :func:`test_that_3_foo_5_bar_7_qix_transcription_of_52_gives_Bar`
  | Unit test for :func:`~model.FooBarQix.transcribe`.
  * :func:`test_that_minus_1_yub_3_foo_5_bar_7_qix_transcription_of_35_gives_BarQixFooBar`
  | Unit test for :func:`~model.FooBarQix.transcribe`.
  * :func:`test_that_0_yub_3_foo_5_bar_7_qix_transcription_of_37_gives_FooQix`
  | Unit test for :func:`~model.FooBarQix.transcribe`.
  * :func:`test_that_9_yub_3_foo_5_bar_7_qix_transcription_of_90_gives_YubFooBarYub`
  | Unit test for :func:`~model.FooBarQix.transcribe`.
  * :func:`test_that_3_foo_5_bar_7_qix_transcription_of_0_gives_FooBarQix`
  | Unit test for :func:`~model.FooBarQix.transcribe`."""
  
  def test_that_3_foo_5_bar_7_qix_transcription_of_92_gives_92( self ):
    """Unit test for :func:`~model.FooBarQix.transcribe`."""
    
    foo_bar_qix = FooBarQix( )
    self.assertEqual( foo_bar_qix.transcribe( 92 ), '92' )
  
  def test_that_3_foo_5_bar_7_qix_transcription_of_52_gives_Bar( self ):
    """Unit test for :func:`~model.FooBarQix.transcribe`."""
    
    foo_bar_qix = FooBarQix( )
    self.assertEqual( foo_bar_qix.transcribe( 52 ), 'Bar' )
  
  def test_that_minus_1_yub_3_foo_5_bar_7_qix_transcription_of_35_gives_BarQixFooBar( self ):
    """Unit test for :func:`~model.FooBarQix.transcribe`."""
    
    foo_bar_qix = FooBarQix( {-1: 'Yub', 3: 'Foo', 5: 'Bar', 7: 'Qix'} )
    self.assertEqual( foo_bar_qix.transcribe( 35 ), 'BarQixFooBar' )
  
  def test_that_0_yub_3_foo_5_bar_7_qix_transcription_of_37_gives_FooQix( self ):
    """Unit test for :func:`~model.FooBarQix.transcribe`."""
    
    foo_bar_qix = FooBarQix( {0: 'Yub', 3: 'Foo', 5: 'Bar', 7: 'Qix'} )
    self.assertEqual( foo_bar_qix.transcribe( 37 ), 'FooQix' )
  
  def test_that_9_yub_3_foo_5_bar_7_qix_transcription_of_90_gives_YubFooBarYub( self ):
    """Unit test for :func:`~model.FooBarQix.transcribe`."""
    
    foo_bar_qix = FooBarQix( {9: 'Yub', 3: 'Foo', 5: 'Bar', 7: 'Qix'} )
    self.assertEqual( foo_bar_qix.transcribe( 90 ), 'YubFooBarYub' )
  
  def test_that_3_foo_5_bar_7_qix_transcription_of_0_gives_FooBarQix( self ):
    """Unit test for :func:`~model.FooBarQix.transcribe`."""
    
    foo_bar_qix = FooBarQix( )
    self.assertEqual( foo_bar_qix.transcribe( 0 ), 'FooBarQix' )