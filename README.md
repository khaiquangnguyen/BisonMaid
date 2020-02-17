#Installation (Windows )

####1. Install python 
BisonMaid uses Python 3.8 as the base programming language, so we will need to install python first.

- Download python 3.8 from https://www.python.org/ftp/python/3.8.1/python-3.8.1-amd64.exe
- Double click on the downloaded file to install. When the first installation screen appear, 
 if you are not familiar with Python installation process, remember to turn on the box **Add Python. 3.8 to PATH**
- Click on install now to install python 3.8 and it's associated files

To confirm that Python is installed and added to PATH, open CMD (or Powershell) and type **python --version**. 
It should display Python 3.8.1.

####2. Install pipenv (not absolutely necessary but recommended)

Since Python allows multiple versions to run at the same time on the same computer, it can be difficult to manage
all the Python versions on a computer (No one taught us this back then =.=). To overcome this, we can use a virtual environment management system. For this project,
we will use pipenv (because it's easy). If you already have your own environment, such as pyenv-virtualenv or virtualenv, then 
just use it.

- Install pipenv by open the Command line (CMD) or Powershell and type **pip install pipenv**. 

To confirm that pipenv is installed, stay in the same CMD or Powershell window and type  **pipenv --version**. It should 
show some version of Pipenv. As if right now, the latest version is pipenv, version 2018.11.26.

####3. Get a code editor (Not absolutely necessary but really recommended)

There are many editors out there to work with Python. There is the good and free Visual Studio Code which is superb, but require 
some configure to work well with Python (so not recommended for newcomers). I suggest Pycharm since 
it's free for students (we are students, right?) for a number of years, and require much less configure. 
For example, Khoi manages to sign up using his Bucknell account for 10 years. 

To download Pycharm, go to https://www.jetbrains.com/pycharm/, sign up for a education account and download the 
professional version. 

####4. Install git command line. 
We need git to interact with Github, so we need to install Git on Windows. There are two ways to use Github on Windows,
either through the command line or through the GUI. Strongly recommend the command line since we will have to work with the 
command a lot anyway. 

- To install, download it from this link https://git-scm.com/download/win.
- Double click to install.Click Next until it is installed.

####5. Download the project
Once install, open Powershell. (I don't know CMD commands so let's go with Powershell or Git Bash).

- Chose the destination folder for the project. By default, Powershell will open the User folder as root. To make this simple,
let's put our project in Desktop (someone with experience here can just ignore this). Type in Powershell **cd ~/Desktop**. 
Powershell will now point to Desktop
- Type in **git clone https://github.com/khaiquangnguyen/BisonMaid.git**. Your Desktop should now have a folder called BisonMaid.

Git commands are complicated, but you don't need to know all of them. The basic ones are:
- git clone
- git commit
- git pull
- git push
- git checkout
- git branch
- git merge

Since this is a pet project, who cares about proper open source management anyway. So for now, we don't need to use things 
like pull request or whatever. Just use git branch and push the branch to master, I will handle the merging. 

####6. Open and run the project
- If use Pycharm, start Pycharm, click on "Open a project", and points it to the folder you just downloaded. 

When Pycharm opens, got to set up the Python environment in Pycharm properly. By default, Pycharm will use the Python version
we installed. We don't want this since it's hard to manage all the Python versions out there(remember why we install pipenv).
- To set up Pycharm, Click on File/Settings. Search **Project Interpreter**. 
- Click on the Gear next to the Project Interpreter -> Add. 
- Chose **Pipenv environment**. Click **OK** to set up pipenv. 

Now, PyCharm will always open this pipenv environment when run the project.

####7. Install dependencies
Now that we have finished set up all of our environment. Let's first download all the necessary package for the project.

- Click on the Terminal icon at the bottom of Pycharm to open Pycharm Terminal (it's recommended to use this one if you are not 
familiar with terminal since this terminal will automatically switch to Pipenv. If you use external terminal, you got to turn on 
pipenv for this project yourself).
- Just to make sure, let's just type in **pipenv shell** to turn on pipenv for this project
- Type in **pipenv install** to install all the dependencies
- Ask me for the .env file

####8. Run it
In Pycharm, click on **Run -> Run 'Maid'**. Or just press Shift+F10.



