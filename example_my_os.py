import os
import datetime
import time
class ExampleMyOS():
    """Для создания экземпляров ОС пользователя и дальнейшей обработки"""
    def __init__(self, path_circle, disk_source='', disk_replic='', disk_log=''):
        """Инициализация ОС пользователя, чтобы персонализировать
           команды оболочки.
        """
        # Инициализация path_circle, чтобы программа понимала
        #  какие команды оболочки использовать.
        self.path_circle = path_circle
        if (os.sys.platform == 'win32'):
            self.slash = chr(92)
            self.ls_user_os = 'dir'
            self.disk_source = disk_source + ':' + chr(92)
            self.default_path = self.disk_source
            self.disk_replic = disk_replic + ':' + chr(92)
            self.disk_log = disk_log + ':' + chr(92)
            self.cls = 'cls'
        else:
            self.slash = '/'
            self.ls_user_os = 'ls'
            self.default_path = '/'
            self.cls = 'clear'
            
    def user_source(self, path_circle=''):
        """
        Здесь производится работа с пользовательскими директориями.
         Запрашиваются пути к каждой из директорий, выбор
         директории зависит от номера выполняемого цикла в теле
         программы.
        """
        
        # Выбор директории
        self.path_circle = path_circle
        if (self.path_circle == 1):
            print_source = 'источника'
        if (self.path_circle == 2):
            print_source = 'реплики'
        if (self.path_circle == 3):
            print_source = 'логов'
            
        # Выбор пути к присвоенным именам директорий
        os.system(self.cls)
        if (os.sys.platform == 'win32'):
            if (self.path_circle == 1):
                path = self.disk_source
            if (self.path_circle == 2):
                path = self.disk_replic
            if (self.path_circle == 3):
                path = self.disk_log
        else:
            path = self.default_path

        # Работа с пользовательским интерфейсом выбора директории
        prev_path = ''
        circle = 1
        active = True
        while active:
            os.system(self.cls)
            print ('\t===========================')
            print ('\tВыберите директорию для ' + print_source + '.')
            print ('\t===========================')
            os.system('cd ' + '"' + path + '"')
            os.system(self.ls_user_os + ' "' + path + '""')
            print ('\n ПРИМЕЧАНИЕ: Если вы закончили ввод, нажмите "Q"')
            print ('Чтобы вернуться в начальную директорию, введите ".."')
            print ('\nКаталог ' + print_source + ': ' + path)

            user_path = input (': ')
            if (user_path == 'q') or (user_path == 'Q'):
                active = False
            elif (user_path == '..'):
                path = self.default_path
                circle = 1
            elif (circle == 1):
                path += user_path
                circle += 1
            elif (circle != 1):
                path += self.slash + user_path
            path = path.replace ('//', '/')
            path = path.replace ('C:\C:', 'C:')
            os.system(self.cls)
            self.my_path = path
        
