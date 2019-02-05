from robobrowser import RoboBrowser
import os, time
import pandas as pd
import numpy as np
import multiprocessing as mp
import numpy



browser = RoboBrowser()
login_url = 'https://patricbrc.org/'
browser.open(login_url)
form = browser.get_form(id='loginForm')
form['username'].value = 'gresch' 
form['password'].value = 'sequencing'
browser.submit_form(form)

browser.open('http://rast.nmpdr.org/rast.cgi?page=JobDetails&job='+ str(jobId))
form = browser.get_form(id='download')