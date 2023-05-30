#import abstract base class
#abc = abstract base class

from abc import ABC,abstractmethod

#membuat parent class dengan inherit dari abstract class
class Button(ABC):
    
    #membuat method abstract class
    @abstractmethod
    def click(self):
        pass
    
#membuat class turunan/inheritance dari class Button
class PushButton(Button):
    
    #membuat method function
    def click(self):
        print("push button click")
        
#membuat class turunan/inheritance dari class Button
class RadioButton(Button):
    def click(self):
        print("radio button click")
        
#membuat object dari class PushButton
tombol1 = PushButton()
tombol2 = RadioButton()

tombol1.click()
tombol2.click()