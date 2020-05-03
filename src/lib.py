import os,glob,sys
from os.path import join,basename,dirname
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup as bs
import random
import selenium
import time
from tqdm import tqdm,trange
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import matplotlib.pyplot as plt
import seaborn as sns