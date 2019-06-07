#!/usr/bin/python3
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,'/var/www/elbarto/')
sys.path.insert(0,"/var/www/elbarto/elbarto/")
from elbarto import app as application
