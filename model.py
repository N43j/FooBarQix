"""Module offering a model dedicated to the first step of the FooBarQix kata (http://codingdojo.org/kata/FooBarQix).

* :class:`FooBarQix`
| Class allowing to transcribe numbers into strings based on an internal dictionary."""

class FooBarQix:
  """Class allowing to transcribe numbers into strings based on an internal dictionary.
  
  :var dictionary: The internal dictionary. Keys represent numbers, values represent strings.
  
  * :func:`transcribe`
  | Transcribes a positive number into a string, following a set of rules."""
  
  def __init__( self, dictionary = {3: 'Foo', 5: 'Bar', 7: 'Qix'} ):
    """Initializes the object.
    
    :param dictionary: The internal dictionary. Keys represent numbers, values represent strings.
    :type dictionary:  ``dict`` (keys are ``int``, values are ``str``)
    
    .. warning:: The dictionary keys must neither contain zero nor negative numbers. Such keys will be removed."""
    
    self.dictionary = {key: value for key, value in dictionary.items( ) if key > 0}
  
  def transcribe( self, number ):
    """Transcribes a positive number into a string, following a set of rules.
    
    Rules are:
    
    1. If the number is divisible by one of the dictionary keys, add the corresponding dictionary value to the string.
    2. If a digit of the number is one of the dictionary keys, add the corresponding dictionary value to the string.
    3. The first rule is applied before the second on all the dictionary keys, following the keys order.
    4. The second rule applies in the order of the number’s digits (left to right).
    5. If neither of the first two rules may apply to the number, then the transcription string is the number itself.
    
    :param number: The number to transcribe. Must be positive.
    :type number:  ``int``
    
    :return:       The transcription of the number.
    :rtype:        ``str``
    
    :Example:
    
    >>> foo_bar_qix = FooBarQix( )   # The dictionary is: ``{3: 'Foo', 5: 'Bar', 7: 'Qix'}``.
    >>> foo_bar_qix.transcribe( 3 )  # 3 is divisible by 3 and contains the digit 3.
    'FooFoo'
    >>> foo_bar_qix.transcribe( 51 ) # 51 is divisible by 3 and contains the digit 5. The first rule has precedence.
    'FooBar'
    >>> foo_bar_qix.transcribe( 41 ) # 41 is not divisible by any of 3, 5 or 7, and none of its digits is 3, 5 or 7.
    '41'
    
    .. note:: Negative numbers won’t raise an error. Instead, they will be converted into their absolute value."""
    
    number        = abs( number )
    transcription = ''
    
    for divisor in self.dictionary.keys( ):
      if number % divisor == 0:
        transcription += self.dictionary[ divisor ]
    
    for digit in str( number ):
      for divisor in self.dictionary.keys( ):
        if int( digit ) == divisor:
          transcription += self.dictionary[ divisor ]
    
    return transcription if transcription else str( number )