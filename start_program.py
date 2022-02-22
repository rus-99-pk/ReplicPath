# Импорт библиотек
import os
import datetime
import time
import modules as m

# Переменные для заполнения пустоты в классе "ExampleMyOS"
#  в случае, если ОС - *nix.
disk_source = ''
disk_replic = ''
disk_log = ''
            
#=====================================================

# Если ОС - Windows, то будут запрошены имена Томов для директорий
if (os.sys.platform == 'win32'):
    my_os = 'Windows'
    disk_source = input ('Диск, который будет использоваться для источника: ')
    disk_replic = input ('Диск, который будет использоваться для реплики: ')
    disk_log = input ('Диск, который будет использоваться для файла логирования: ')

#  Заполнение списка пулом путей к директориям
paths = []
for circle in range(1, 4):
    directory = m.ExampleMyOS(circle, disk_source, disk_replic, disk_log)
    directory.user_source(circle)
    paths.append(directory.my_path)

# 0 - Директория-источник, 1 - Директория-реплика, 2 - Директория логов.
source_dir = paths[0]
replic_dir = paths[1]
log_dir = paths[2]

#=====================================================

# Запрос периодичности бэкапов и
#  дальнейшее преобразование единиц времени.
backup_delay = input('С какой периодичностью выполнять бэкапы?\nПримеры: 10s/10m/10c\n')
backup_value = backup_delay[-1]
backup_delay = int(backup_delay[:-1])
os.system(directory.cls)
if (backup_value == 'm'):
    backup_delay = int(backup_delay) * 60
if (backup_value == 'c'):
    backup_delay = int(backup_delay) * 60**2

# Выполнение бэкапов и вывод логов
filework = m.Work(source_dir, replic_dir, log_dir, directory.slash, backup_delay)
filework.print_create()
active = True
while active:
    filework.timework()
    filework.scan_folders()
    time.sleep(backup_delay)
