from abc import ABC,abstractmethod

class Button(ABC):
    
    #constructor
    def __init__(self,set_link):
        self.link = set_link

    #abstractmethod
    @abstractmethod
    def click(self):
        pass

    #decorator property
    @property
    @abstractmethod
    def link(self):
        pass

class PushButton(Button):
    
    def click(self):
        print("Go To: {}".format(self.link))

    #membuat method setter
    @Button.link.setter
    def  link(self,input):
        self.__link = input

    #membuat method getter
    @link.getter
    def link(self):
        return self.__link
tombol1 = PushButton("www.google.com")
tombol1.click()