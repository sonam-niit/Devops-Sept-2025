# Python Virtual Environment & Dependency Management

- A python virtual environment is an isolated workspace which allows you to install and manage dependencies for different projects without ant conflicts.

- With virtual environments, each project can have its own independent of the global python installation.

---

## Benefits of Virtual Environment
- Keep packages isolated
- prevent from version conflict
- manage different dependencies for different projects.

## Creating Virtual Environment

```bash
mkdir myproject # create folder
cd myproject # move to that folder 
python -m venv myenv #Windows and mac
```
- This will create a folder named myenv containing fully isolated Python Environment
- myenv folder will be created under myproject folder

- If you are using ubuntu or linux
```bash
sudo apt install python3-venv 
python3 -m venv myenv 
```

## Activating Virtual Environment

```bash
# On windows (CMD/ powershell)
myenv\Scripts\activate
# On Mac or Linux or ubuntu
source myenv/bin/activate

# Once it is acivated install dependencies like
pip install requests flask
# It will install 2 libraries request and flask

# To Deactivate
deactivate
```

## Advanced Dependency management using pipenv

- Pipenv combines pip and virtualenv to simplify dependency management

**Benefits**
- Tracks dependencies in pipfile and pipfile.lock
- Simplified version control
- makes project sharing easier

*for Windows/mac user*

- pip install pipenv (this you need to run only once)

- create a folder and move to that folder
- pipenv install flask (this will install isolated flask package)
- for activating: pipenv shell 
- for exit: type exit and enter

**Any command which you run inside this shell will use the virtual environment**

*for linux/ubuntu user*

```bash
sudo apt update && sudo apt install pipenv
pipenv --version
pipenv install flask # install flask
pipenv shell # for activate
exit # to exit
```

### To install many packages 

- create text file by adding all packages in new line
- create file requirements.txt
```txt
flask
requests
pandas
```
- to install all packages
- pipenv install -r requirements.txt

*pipenv graph - to check installed dependencies*

**you can use anyone of these to set up virtual environment venv or pipenv**