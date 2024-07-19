"""
Команды пишутся только один раз когда вы делаете первый пуш
для соединения vscode с github


git --version

git config --global user.name "YOUR USERNAME ON GITHUB"

git config --global user.email "YOUR EMAIL ON GITHUB"


"""


"""
Команды для пуша на новый репозиторий (первый пуш в новом репохитории)


git init    - создает локальный репозиторий


git add .    - добавляет изменения на локальный репозиторий
# git add lesson_1.py


git commit -m "lessons 1-5"      - подтверждает изменения, создает версию , оставляет комментарий
# git commit -m "Напишите понятное но короткое описание того что вы сделали"
# git commit -m "first commit"


git remote add origin <HTTPS link.git>    - Привязывает локальный репозиторий с удаленным
# git remote add origin https://github.com/Abdykadyrov-S/19-1B.git


git branch -M main 


git push -u origin <название вашей ветки>     - отправляет в удаленный репозиторий 
# git push -u origin main

"""


"""
Команды для пуша на существующий репозиторий с коммитом

git add .


git commit -m "Напишите понятное но короткое описание того что вы сделали"


git push 

"""


"""
Команды для работы с ветками

git branch

git checkout -b <название ветки>   - для создания новой ветки
# git checkout -b syimyk


git checkout <название ветки>    - для переключения на другую ветку
# git checkout syimyk


"""



"""
Команды-помошники

git pull

git status

git clone
"""