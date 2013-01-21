###Create a new repository on the command line

* touch README.md
* git init
* git add README.md
* git commit -m "first commit"
* git remote add origin https://github.com/imouren/weida.git
* git push -u origin master

###Push an existing repository from the command line

* git remote add origin https://github.com/imouren/weida.git
* git push -u origin master

----------
8、创建本地新项目工作树
# mkdir new-project
# cd new-project
# git init
# touch README
# git add README
# git commit -m 'first commit'
定义远程服务器别名origin
#  git remote add origin git@github.com:xxx/new-project.git   
本地和远程合并，本地默认分支为master
# git push origin master  

GitHub网站上就可以看见了， http://github.com/xxx/new-project

9. 更新文件
# vi README
自动commit更改文件
# git commit -a     
更新至远程
# git push origin master

10. 创建和合并分支
#git branch 显示当前分支是master
#git branch new-feature  创建分支
# git checkout new-feature 切换到新分支
# vi page_cache.inc.php
# git add page_cache.inc.php
Commit 到本地GIT
# git commit -a -m "added initial version of page cache"
合并到远程服务器
# git push origin new-feature

如果new-feature分支成熟了，觉得有必要合并进master
#git checkout master
#git merge new-feature
#git branch
#git push 
则master中也合并了new-feature 的代码