# python -m venv myenv

# see foler myenv
#  can create diffrernt versions of a python
#  tyo activate


#  if you are very new run command
#  >>> Get-ExecutionPolicy
# Restricted
# to fix this , run command
# >>>  Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

# acvtivated !! ( if you not get any error)

# go in environment by commands

# ls -to see items in folder
# cd - to change directory and to f=go in another directory
# pwd - to see present working directory
# cd ..-to go back in directory
#  for right now this ar esufficient

# 1. virtualenv dir_name  ( in dir_name you can write anything )
# 2. dir_name/Scripts/activate  ( for activating )
# 3. deactivate ( for deactivating )

#  specific  pip install pandas==1.4.4
#  pandas will installed


# sample ::: (I coppy pasted my termina directly)

# (myenv) PS D:\THE  PROGRAMING\the Python programing laungage\learning\virt_env> python
# Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import pandas as pd
# >>> pd.__version__
# '2.0.3'
# >>>


#  to deactivate
# run command after exiting -deactivate

# (myenv) PS D:\THE  PROGRAMING\the Python programing laungage\learning\virt_env> deactivate
# PS D:\THE  PROGRAMING\the Python programing laungage\learning\virt_env>

#  to activate again
# myenv\Scripts\activate      run this command

# ALERT :
# if you enter and work in your environment , it is always recommanded to close it . means if being in virtual env if you try to access your original python it will not work

# https://replit.com/@codewithharry/43-Day43-Virtual-Environment#.tutorial/Tutorial.md
# https://www.youtube.com/watch?v=nt6LlFTWOkg&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=43
# rather than ""mathapacchi""  go there

# >>> pip freesze
#  to see all packages install in env
# >>> pip freesze > requirement.txt
# $ all packages name will it in this file
#  to install all packages in requirement.txt for your friend
# >>> pip freesze > -r requirement.txt
#  all packages in the txt file will install in friends computer


# If you are using window, you can use below commands :)

# 1. virtualenv dir_name  ( in dir_name you can write anything )
# 2. dir_name/Scripts/activate  ( for activating )
# 3. deactivate ( for deactivating )
