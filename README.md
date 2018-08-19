# MusicAIComposer
Using AI to compose music

# The prerequisites below are for running MIDI_Crawler.py for crawling MIDI files from FreeMidi.org

# IDE and Python version used

IDE used for running the program is Anaconda 1.5.2 and Spyder 3.2.8.<br/>
(Optional: Visual Studio Code with Python plugins）<br/>
The python version used is Python 3.6.<br/>

# Instructions for Headless Chrome

Please copy and paste the chromedriver_win32 folder in C:\ drive.

# Instructions to install selenium

1. Install Anaconda for Python 3.6 version following this link:https://www.anaconda.com/download/
2. Install Spyder IDE in Anaconda.
3. Once you have installed Anaconda, you can straightly run Windows default CMD as administrator and execute the following command to install selenium:
    pip install selenium
4. You can also install selenium through Anaconda Navigator -> Environment -> Not installed and then search for selenium.

# For training data set, please put the selected MIDI files into data folder and then change the respective code in the constants.py (genre and styles)

# Instructions to run the DeepJ A.I. Music Composer in Google Colab
Please execute the following code in your Google Colab's Jupyter Notebook:

1.
!apt-get install -y -qq software-properties-common python-software-properties module-init-tools
!add-apt-repository -y ppa:alessandro-strada/ppa 2>&1 > /dev/null
!apt-get update -qq 2>&1 > /dev/null
!apt-get -y install -qq google-drive-ocamlfuse fuse
from google.colab import auth
auth.authenticate_user()
from oauth2client.client import GoogleCredentials
creds = GoogleCredentials.get_application_default()
import getpass
!google-drive-ocamlfuse -headless -id={creds.client_id} -secret={creds.client_secret} < /dev/null 2>&1 | grep URL
vcode = getpass.getpass()
!echo {vcode} | google-drive-ocamlfuse -headless -id={creds.client_id} -secret={creds.client_secret}

2.
!mkdir -p drive
!google-drive-ocamlfuse drive

3.
!pip install keras==2.0
!apt-get install swig
!apt-get install libasound2-dev
!pip install git+https://github.com/vishnubob/python-midi@feature/python3
!pip install -r drive/app/DeepJ/requirements.txt
!pip install --upgrade tensorflow-gpu==1.4

4.
!python drive/app/DeepJ/train.py

5. 
!python drive/app/DeepJ/generate.py
