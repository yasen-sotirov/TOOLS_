"GIT"  # https://www.youtube.com/watch?v=tRZGeaHPoaw&ab_channel=KevinStratvert


"""
ЕТАПИ НА РАБОТА
    Working directory 
        работното IDE, със git commit качва в staging area
    
    Staging area
        с git push записва промените в облака
        
    Repository
        репото в облака



LOGING
    # логва
        git config --global user.name "Yasen Sotirov"
        git config --global user.email ia.sotirov@gmail.com
    # показва кой е логнат
        git config --global user.name
        git config --global user.email
        
        
REPOSITORY
    # инициализиране на ново репо - git започва да следи текущата папка
        git init
    
    # показва адреса на репото на сървъра - има два адреса за fech  и за push
        git remote -v


STAGING AREA - track files
    # проверява статуса на staging area -дали има нови неща за commit
        git status
    # качва всички промени в staging-а
        git add .   
        git add --all
        git add -A
    # качва конкретен файл
        git add main.py
    # сваля от staging-a
        git restore --staged <file_name>
        git reset   
        git reset path/fail_name
    # undo всички последните след последния commit == Discard changes
        git checkout --.
        git checkout --<file name.py>
    # спиране следенето на файл (tracking)   
        git rm --cached <name>  
        

COMMIT == VERSION
    # от staging area качва в самия гит
        git commit -m "<message>"
    # редактиране на последния commit - файлове, иmе на commit-a
        git commit -m "<message>" --amend
    # преглед на commit
        git log
    # преглед на всички commit + подробности
        git log
    # отваря предишен commit по име 
        git checkout <commit name> 
    # трие последния commit и връща на предходния, трябва да се push-не
        git reset --hard HEAD^
        git push --force         

BRANCH
    # задаване на главния branch - за ново репо
        git config --global init.branch main
    # показва всички branch       
        git branch
    # създава нов бранч и прехвърля на него
        git switch -c <name>
    # създава нов бранч без да прехвърля на него
        git branch <name>
    # създава нов бранч и се прехвърля на него
        git switch -c <name>
    # прехвърля на друг branch
        git switch <name>
    # прехвърля на предишния branch
        git checkout -git branch
    # трие branch - обикновено след merge
        git branch -d <name>
    # качва branch в облака
        git push -u origin <branch_name>
    # качва всички branch в облака
        git push --all
    # създаване на default branch
        git config --global init.default branch main
    # обединяване branch merge
        git merge -m "<message>" <branch name>        

ФАЙЛОВЕ
    # трие файл
        git rm "file_name"
    # връща изтрит файл
        git restore "file_name"
    # преименува move
        git mv "old_file_name" "new_file_name"

    



КАЧВАНЕ ОТ ЛОКАЛНОТО РЕПО В ОБЛАКА  
    # прави връзка на локалното репо с облака
        git remote aa origin url://
    # указва кой е основния branch
        git branch -M main
    # качва цялото локално репо в новото място в облака
        git push -u origin main
    # качване на последните commit
        git push
        

СВАЛЯНЕ ОТ ОБЛАКА
    # сваля промените
        git fetch
    # преглед на промените
         
    # записване на свалените промени в локаното репо
        git merge
    # сваля и записва едновремено 
        git pull
    
    
ПОДРОБНО ИНФО ЗА ДАДЕНА КОМАНДА
    git help <command>



ПРОВЕРЯВА КОНФЛИКТИТЕ
    git  checkout matches



"""