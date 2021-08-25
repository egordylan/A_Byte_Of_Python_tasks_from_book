import os, zipfile
import time


#  1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
#  Имя, содержащее пробелы, необходимо оборачивать в двойные кавычки.
source = ['D:\FreeCodeCamp\My Documents', 'D:\FreeCodeCamp\Code', 'D:\FreeCodeCamp\py4everyone', 'D:\FreeIT']

#  2. Резервные копии должны храниться в основном каталоге резерва.
target_dir = 'D:\FreeCodeCamp\Backup'

#  3. Файлы помещаются в zip-архив.
#  4. Текущая дата служит именем подкаталога в основном каталоге.
today = target_dir + os.sep + time.strftime('%Y%m%d')
#  Именем для zip-архива служит текущее время.
now = time.strftime('%H%M%S')

#  Запрашиваем комментарий пользователя для имени файла
comment = input('Введите комментарий --> ')
if len(comment) == 0:  #  проверяем, введен ли комментарий
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
             comment.replace(' ', '_') + '.zip'

#  Создаем каталог если его еще нет.
if not os.path.exists(today):
    os.mkdir(today)
    print('Каталог успешно создан', today)

print('Создание нового zip-файла %s...' % target)
#  название папки + w запись в архив + метод сжатия
zip_File = zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED)

#  Обход всего дерева директорий и сжатие файлов в каждой папке
archDirName = ''

for sub_source in source:
    for dir, subdirs, files in os.walk(sub_source):
        print('2', dir)
        print('Добавление файлов из директории %s...' % dir)
        #  Имя текущейдиректории в архиве
        archDirName = ''.join(dir)
        #  Добавить в архив текущую директорию
        zip_File.write(dir, archDirName)

        #  Добавление в архив файлов из текущей директории
        for file in files:
            #  Имя текущего файла в архиве
            archFileName = dir + '/' + file
            zip_File.write(os.path.join(dir, file), archFileName)

zip_File.close()
print('Резервная копия успешна создана в', target)
