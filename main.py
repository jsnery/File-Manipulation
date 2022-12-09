from abc import ABC, abstractmethod
from shutil import copy2, move

class FolderNotFoundError(Exception): ...

class main(ABC):
    def __init__(self):
        self._dirfile = None
        self._destinationdir = None

    @property
    @abstractmethod
    def file(self) -> str:...
    
    @file.setter
    @abstractmethod
    def file(self, value):...
    
    @property
    @abstractmethod
    def dir(self) -> str:...
    
    @dir.setter
    @abstractmethod
    def dir(self, value):...
        
        
class FileManipulation(main):
    
    @property
    def file(self) -> str:
        if self._dirfile is None:
            return f'File directory not defined'
        return self._dirfile
    
    @file.setter
    def file(self, file):
        self._dirfile = file.replace("'", '')

    @property
    def dir(self) -> str:
        if self._destinationdir is None:
            return f'Directory not defined'
        return self._destinationdir
    
    @dir.setter
    def dir(self, dir):
        self._destinationdir = dir.replace("'", '')
    
    
    def move_file(self):
        if self._dirfile is None or self._dirfile == '':
            raise FileNotFoundError('File not defined, please define!')
        elif self._destinationdir is None or self._destinationdir == '':
            raise FolderNotFoundError('Directory not defined, please define!')
        move(self._dirfile, self._destinationdir)
    
    def copy_file(self):
        if self._dirfile is None or self._dirfile == '':
            raise FileNotFoundError('File not defined, please define!')
        elif self._destinationdir is None or self._destinationdir == '':
            raise FolderNotFoundError('Directory not defined, please define!')
        copy2(self._dirfile, self._destinationdir)
        
        
    

if __name__ == '__main__':
    test = FileManipulation()
    test.file = input('Drag file to here: ')
    test.dir = input('Drag folder to here or type directory: ')
    test.move_file()