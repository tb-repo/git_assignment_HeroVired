# git_assignment_HeroVired
Calculator Plus App -- Git assignment 1 from HeroVired batch 16A:

Steps:

a. Repository named git_assignment_HeroVired created in my Github account - tb-repo

b. This repository is created as private repo 

c. A new folder is created on my machine for this assignment

d. Open VSCode from the new assignment folder created

e. Now clone the main repo from Git to local machine
    git clone git@github.com:tb-repo/git_assignment_HeroVired.git

f. Create a new branch called 'dev'
    git branch dev

g. Move to dev branch
    git checkout dev

h. Create a new file named app.py that will hold the main application code. Make sure that you set the right Python interpretor on the VSCode

i. Add the basic calculator operations (add,sub,mul,div) program code as provided on the assignment

j. Execute the code and check the output (fix any errors):
    (base) PS D:\HeroVired\Assignments\git_assignment_HeroVired\git_assignment_HeroVired> & C:/Users/thiagarajanb/anaconda3/python.exe d:/HeroVired/Assignments/git_assignment_HeroVired/git_assignment_HeroVired/app.py
    16 + 4 = 20
    16 - 4 = 12
    16 * 4 = 64
    16 / 4 = 4.0

k. Commit the version 1 of this app in dev branch and push to repo:
    (base) PS D:\HeroVired\Assignments\git_assignment_HeroVired\git_assignment_HeroVired> git add .
    (base) PS D:\HeroVired\Assignments\git_assignment_HeroVired\git_assignment_HeroVired> git commit -m "Version 1 of calculator plus app"
    [dev 5e902d7] Version 1 of calculator plus app
    3 files changed, 57 insertions(+), 1 deletion(-)
    create mode 100644 .vscode/settings.json
    create mode 100644 app.py
    (base) PS D:\HeroVired\Assignments\git_assignment_HeroVired\git_assignment_HeroVired> git status
    On branch dev
    nothing to commit, working tree clean
    (base) PS D:\HeroVired\Assignments\git_assignment_HeroVired\git_assignment_HeroVired> git push -u origin dev
    Enumerating objects: 11, done.
    Counting objects: 100% (11/11), done.
    Delta compression using up to 8 threads
    Compressing objects: 100% (8/8), done.
    Writing objects: 100% (9/9), 1.67 KiB | 341.00 KiB/s, done.
    Total 9 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
    remote: Resolving deltas: 100% (2/2), done.
    remote: 
    remote: Create a pull request for 'dev' on GitHub by visiting:
    remote:      https://github.com/tb-repo/git_assignment_HeroVired/pull/new/dev
    remote:
    To github.com:tb-repo/git_assignment_HeroVired.git
    * [new branch]      dev -> dev
    branch 'dev' set up to track 'origin/dev'.

l. Merge the dev and main branch and push to git
    (base) PS D:\HeroVired\Assignments\git_assignment_HeroVired\git_assignment_HeroVired> git checkout main
    Switched to branch 'main'
    Your branch is up to date with 'origin/main'.
    (base) PS D:\HeroVired\Assignments\git_assignment_HeroVired\git_assignment_HeroVired> git merge dev
    Updating dec7aaf..752acfd
    Fast-forward
    .vscode/settings.json |  4 ++++
    README.md             | 65 ++++++++++++++++++++++++++++++++++++++++++++++++++-
    app.py                | 19 +++++++++++++++
    3 files changed, 87 insertions(+), 1 deletion(-)
    create mode 100644 .vscode/settings.json
    create mode 100644 app.py
    (base) PS D:\HeroVired\Assignments\git_assignment_HeroVired\git_assignment_HeroVired> git tag v1.0
	(base) PS D:\HeroVired\Assignments\git_assignment_HeroVired\git_assignment_HeroVired> git push origin v1.0
	Total 0 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
	To github.com:tb-repo/git_assignment_HeroVired.git
	* [new tag]         v1.0 -> v1.0
	
m. Implement a feature by creating a new branch called ‘feature/sqrt’

	(base) PS D:\HeroVired\Assignments\git_assignment_HeroVired\git_assignment_HeroVired> git checkout main
	Already on 'main'
	Your branch is up to date with 'origin/main'.
	(base) PS D:\HeroVired\Assignments\git_assignment_HeroVired\git_assignment_HeroVired> git branch feature/sqrt
	(base) PS D:\HeroVired\Assignments\git_assignment_HeroVired\git_assignment_HeroVired> git checkout feature/sqrt
	Switched to branch 'feature/sqrt'
	
n. Add the sqrt code as below and execute it to verify:

	import math
	class Calculator:
		def add(self, a, b):
			return a + b
		def subtract(self, a, b):
			return a - b
		def multiply(self, a, b):
			return a * b
		def divide(self, a, b):
			return a / b
		def square_root(self, x):
			return math.sqrt(x)
	
	if __name__ == "__main__":
		calculator = Calculator()
		num1 = 16
		num2 = 4
		print(f"{num1} + {num2} = {calculator.add(num1, num2)}")
		print(f"{num1} - {num2} = {calculator.subtract(num1, num2)}") 
		print(f"{num1} * {num2} = {calculator.multiply(num1, num2)}")
		print(f"{num1} / {num2} = {calculator.divide(num1, num2)}")
		print(f"√{num1} = {calculator.square_root(num1)}")
		print(f"√{num2} = {calculator.square_root(num2)}")
		
	(base) PS D:\HeroVired\Assignments\git_assignment_HeroVired\git_assignment_HeroVired> & C:/Users/thiagarajanb/anaconda3/python.exe d:/HeroVired/Assignments/git_assignment_HeroVired/git_assignment_HeroVired/app.py
	16 + 4 = 20
	16 - 4 = 12
	16 * 4 = 64
	16 / 4 = 4.0
	√16 = 4.0
	√4 = 2.0

o. Commit the feature branch changes and push it to feature branch repo:

	(base) PS D:\HeroVired\Assignments\git_assignment_HeroVired\git_assignment_HeroVired> git add .
	(base) PS D:\HeroVired\Assignments\git_assignment_HeroVired\git_assignment_HeroVired> git commit -m "Added square root feature"
	[feature/sqrt fb9be53] Added square root feature
	1 file changed, 6 insertions(+), 1 deletion(-)
	(base) PS D:\HeroVired\Assignments\git_assignment_HeroVired\git_assignment_HeroVired> git push origin feature/sqrt
	Enumerating objects: 5, done.
	Counting objects: 100% (5/5), done.
	Delta compression using up to 8 threads
	Compressing objects: 100% (3/3), done.
	Writing objects: 100% (3/3), 419 bytes | 419.00 KiB/s, done.
	Total 3 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
	remote: Resolving deltas: 100% (2/2), completed with 2 local objects.      
	remote: 
	remote: Create a pull request for 'feature/sqrt' on GitHub by visiting:    
	remote:      https://github.com/tb-repo/git_assignment_HeroVired/pull/new/feature/sqrt
	remote:
	To github.com:tb-repo/git_assignment_HeroVired.git
	* [new branch]      feature/sqrt -> feature/sqrt
	
p. Fix the critical bug reported in dev branch:

	(base) PS D:\HeroVired\Assignments\git_assignment_HeroVired\git_assignment_HeroVired> git checkout dev
	Switched to branch 'dev'
	Your branch is up to date with 'origin/dev'.
	
q. Add the required fixes for the critical bug:

	import math
	class Calculator:
		def add(self, a, b):
			return a + b
		def subtract(self, a, b):
			return a - b
		def multiply(self, a, b):
			return a * b
		def divide(self, a, b):
			if b == 0:
				raise ValueError("Cannot divide by zero.")
			return a / b
	
	if __name__ == "__main__":
		calculator = Calculator()
		num1 = 16
		num2 = 0
		print(f"{num1} + {num2} = {calculator.add(num1, num2)}")
		print(f"{num1} - {num2} = {calculator.subtract(num1, num2)}") 
		print(f"{num1} * {num2} = {calculator.multiply(num1, num2)}")
		print(f"{num1} / {num2} = {calculator.divide(num1, num2)}")
		
r. Run the code to validate it and commit the changes and push it to the repo on dev branch:

	(base) PS D:\HeroVired\Assignments\git_assignment_HeroVired\git_assignment_HeroVired> git add .
	(base) PS D:\HeroVired\Assignments\git_assignment_HeroVired\git_assignment_HeroVired> git commit -m "Fix division by zero bug" 
	[dev b3f3020] Fix division by zero bug
	1 file changed, 3 insertions(+), 1 deletion(-)
	(base) PS D:\HeroVired\Assignments\git_assignment_HeroVired\git_assignment_HeroVired> git push origin dev
	Enumerating objects: 5, done.
	Counting objects: 100% (5/5), done.
	Delta compression using up to 8 threads
	Compressing objects: 100% (3/3), done.
	Writing objects: 100% (3/3), 375 bytes | 375.00 KiB/s, done.
	Total 3 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
	remote: Resolving deltas: 100% (2/2), completed with 2 local objects.      
	To github.com:tb-repo/git_assignment_HeroVired.git
	87fa118..b3f3020  dev -> dev
	
s. Create a PR via console from main branch to feature/sqrt branch:

	PR Title: Add square root feature to CalculatorPlus
	Description: Please review the feature branch code with the sqrt function added and confirm if it can be merged with main branch

	(base) PS D:\HeroVired\Assignments\git_assignment_HeroVired\git_assignment_HeroVired> git checkout main
	Switched to branch 'main'
	Your branch is up to date with 'origin/main'.
	(base) PS D:\HeroVired\Assignments\git_assignment_HeroVired\git_assignment_HeroVired> git pull
	remote: Enumerating objects: 1, done.
	remote: Counting objects: 100% (1/1), done.
	remote: Total 1 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
	Unpacking objects: 100% (1/1), 952 bytes | 158.00 KiB/s, done.
	From github.com:tb-repo/git_assignment_HeroVired
	7103c99..f2fa123  main       -> origin/main
	Updating 7103c99..f2fa123
	Fast-forward
	app.py | 2 ++
	1 file changed, 2 insertions(+)
	
t. Create a new PR for merging dev and feature/sqrt branch and request it to be reviewed by a collaborator

	Title: Merging the sqrt functionality and critical bug of div by zero
	Description: Please review the code to confirm if we can merge the sqrt functionality and the div by zero critical bug fix
	Reviewer: sanjuwatson-del