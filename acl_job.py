from pyats.easypy import run
import os

def main():

    path = os.path.dirname(__file__)
    #run(testscript = os.path.join(path,'acl_testcases.py'),datafile = os.path.join(path,'acl_datafile.yaml'))
    run('acl_testcases.py', datafile = 'acl_datafile.yaml',pdb=True)
    #run(acl_testcases.py, datafile = 'testbed.yaml',pdb=True)
