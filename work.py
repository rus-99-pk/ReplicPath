import os
import datetime
import time
class Work():
    """Класс для работы с выводами логов на экран и в файл"""
    def __init__(self, source_dir, replic_dir, log_dir, slash, backup_delay):
        """Модуль инициализации пользовательских директорий"""
        self.source_dir = source_dir
        self.replic_dir = replic_dir
        self.log_dir = log_dir
        self.slash = slash
        self.backup_delay = backup_delay

    def timework(self):
        """Модуль работы с датой и временем"""
        now = datetime.datetime.now()
        day = now.day
        month = now.month
        self.year = str(now.year)
        hour = now.hour
        minute = now.minute
        second = now.second

        # Условия проверки сделаны для удобного вывода дат и времени.
        #  Пример:
        #   Вместо "1.2.2022 I 13:1:45" будет "01.02.2022 I 13:01:45"
        if (day < 10):
            self.day = '0' + str(day)
        else:
            self.day = str(day)
            
        if (month < 10):
            self.month = '0' + str(month)
        else:
            self.month = str(month)
        
        if (hour < 10):
            self.hour = '0' + str(hour)
        else:
            self.hour = str(hour)
            
        if (minute < 10):
            self.minute = '0' + str(minute)
        else:
            self.minute = str(minute)
            
        if (second < 10):
            self.second = '0' + str(second)
        else:
            self.second = str(second)

        # Переменная, содержащая дату и время
        self.logtime = self.day + '-' + self.month + '-' + self.year + '|'
        self.logtime += self.hour + ':' + self.minute + ':' + self.second

    def print_create(self):
        """Создание файла логов"""
        self.timework()
        # Вывод информации о создании файла
        message = self.logtime + '    Создан файл логов.\n'
        
        # Условия, в зависимости от которого будет выбраны команды для каждой ОС,
        if (os.sys.platform == 'win32'):
            full_log_path = self.log_dir + self.slash + 'backup_logs_' + self.logtime[:-9] + '.log'
        else:
            full_log_path = self.log_dir + self.slash + 'backup_logs_' + self.logtime + '.log'

        # Создание файла логов
        self.logfile = open(full_log_path, 'w+')
        self.logfile.write(message)
        print (message)

        # Вывод информации о периодичности создания логов (в теле программы вопрос к пользователю)
        message = self.logtime + '    Репликация будет выполняться с периодичностью в ' + str(self. backup_delay) + ' секунд.\n'
        self.logfile.write(message)
        print (message)

    def scan_folders(self):
        """Модуль выполняет сравнение директорий Источника и Реплики"""
        source_objects = os.listdir(self.source_dir)
        replic_objects = os.listdir(self.replic_dir)

        # Условия удаления объектов в реплике
        for replic_object in replic_objects:
            if (replic_object not in source_objects):
                message = self.logtime + '    "' + replic_object + '" удален из "' + self.replic_dir + '", т.к. отсутствует в "' + self.source_dir + '".\n'
                self.logfile.write(message)
                print (message)

                # Условия выбора команды взависимости от ОС
                if (os.sys.platform == 'win32'):
                    if (os.path.isfile(self.replic_dir + self.slash + replic_object) == True):
                        os.system('del /s/q "' + self.replic_dir + self.slash + replic_object + '"')
                    else:
                        os.system('rd /s/q "' + self.replic_dir + self.slash + replic_object + '"')
                else:
                    os.system('rm -rf ' + '"' + self.replic_dir + self.slash + replic_object + '"')

        # Условия обновления объектов в реплике
        for source_object in source_objects:
            if (source_object in replic_objects):
                message = self.logtime + '    "' + source_object + '" обновлен в "' + self.replic_dir + '".\n'
                self.logfile.write(message)
                print (message)

                # Условия выбора команды взависимости от ОС
                if (os.sys.platform == 'win32'):
                    if (os.path.isfile(self.replic_dir + self.slash + source_object) == True):
                        os.system('del /s/q "' + self.replic_dir + self.slash + source_object + '"')
                        os.system('xcopy "' + self.source_dir + self.slash + source_object + '" "' + self.replic_dir + '" /E')
                    else:
                        os.system('rd /s/q "' + self.replic_dir + self.slash + source_object + '"')
                        os.system('mkdir "' + source_object + '"')
                        os.system('xcopy "' + self.source_dir + self.slash + source_object + '" "' + self.replic_dir + self.slash + source_object + self.slash + '" /E /S')
                        
                else:
                    os.system('rm -rf ' + '"' + self.replic_dir + self.slash + source_object + '"')
                    os.system('cp -rf ' + '"' + self.source_dir + self.slash + source_object + '" "' + self.replic_dir + '"')

        # Условия создания объектов в реплике
        for source_object in source_objects:
            if (source_object not in replic_objects):
                message = self.logtime + '    "' + source_object + '" создан в "' + self.replic_dir + '".\n'
                self.logfile.write(message)
                print (message)
                
                # Условия выбора команды взависимости от ОС
                if (os.sys.platform == 'win32'):
                    if (os.path.isfile(self.source_dir + self.slash + source_object) == True):
                        os.system('xcopy "' + self.source_dir + self.slash + source_object + '" "' + self.replic_dir + '" /E /Q')
                    else:
                        os.system('mkdir "' + source_object + '"')
                        os.system('xcopy "' + self.source_dir + self.slash + source_object + '" "' + self.replic_dir + self.slash + source_object + self.slash + '" /E /S')
                else:
                    os.system('cp -rf ' + '"' + self.source_dir + self.slash + source_object + '" "' + self.replic_dir + '"')

        print ('\nДля завершения работы программы нажмите "CTRL+C"\n')
