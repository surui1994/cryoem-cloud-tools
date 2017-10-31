#!/usr/bin/env python
import pickle
import datetime 
import shutil
import optparse
from sys import *
import os,sys,re
from optparse import OptionParser
import glob
import subprocess
from os import system
import linecache
import time
import string
from fabric.operations import run, put
from fabric.api import env,run,hide,settings
from fabric.context_managers import shell_env

#=========================
def setupParserOptions():
        parser = optparse.OptionParser()
        parser.set_usage("This program will submit a rosetta atomic model refinement to AWS for refinement. Specify input pdb file(s), FASTA file and cryo-EM maps below.\n\n%prog --pdb_list=<.txt file with the list of input pdbs and their weights> --fasta=<FASTA file with protein sequence> --em_map=<EM map in .mrc format> --num=<number of atomic structures per CPU process (default:5) -r (flag to run relax instead of CM)")
        parser.add_option("--em_map",dest="em_map",type="string",metavar="FILE",
                    help="EM map in .mrc format")
	parser.add_option("--fasta",dest="fasta",type="string",metavar="FILE",
                    help="FASTA sequence file (not required for rosetta relax)")
	parser.add_option("--hhr",dest="hhr",type="string",metavar="FILE",default='',
                    help=".hhr sequence alignment file")
	parser.add_option("--AMI",dest="AMI",type="string",metavar="AMI",
                    help="AMI for Rosetta software environment on AWS. (Read more here: cryoem-tools.cloud/rosetta-aws)")
	parser.add_option("-r", action="store_true",dest="relax",default=False,
                    help="run rosetta relax instead of CM")
	parser.add_option("--pdb_list",dest="pdb_list",type="string",metavar="FILE",default='',
                    help="PDB reference file OR .txt file with the input pdbs and their weights. List is required Only required if no .hhr file provided")
	parser.add_option("--num",dest="num_models",type="int",metavar="INT",default=216,
                    help="Number of structures to calculate. (Default = 216)")
	parser.add_option("--outdir",dest="outdir",type="string",metavar="DIR",default='',
		    help="Optional: Name of output directory. Otherwise, output directory will be automatically generated")
	parser.add_option("--nocheck", action="store_true",dest="nocheck",default=False,
                    help="Include this option to not stop after preparing PDB files, instead continuing straight into Rosetta-CM")
	options,args = parser.parse_args()

        if len(args) > 0:
                parser.error("Unknown commandline options: " +str(args))
        if len(sys.argv) <= 2:
                parser.print_help()
                sys.exit()
        params={}
        for i in parser.option_list:
                if isinstance(i.dest,str):
                        params[i.dest] = getattr(options,i.dest)
        return params

#=============================
def checkConflicts(params,outdir):

	if os.path.exists(outdir): 
		print "\nError: Output directory already exists. Exiting" %(outdir)
		sys.exit()

	if not params['AMI']: 
		print '\nError: No AMI specified. Exiting\n'
		sys.exit()

	awsregion=subprocess.Popen('echo $AWS_DEFAULT_REGION', shell=True, stdout=subprocess.PIPE).stdout.read().split()[0]
        if len(awsregion) == 0:
                writeToLog('Error: Could not find default region specified as $AWS_DEFAULT_REGION. Please set this environmental variable and try again.','%s/run.err' %(outdir))
                sys.exit()

        #Get AWS ID
        AWS_ID=subprocess.Popen('echo $AWS_ACCOUNT_ID',shell=True, stdout=subprocess.PIPE).stdout.read().strip()
        key_ID=subprocess.Popen('echo $AWS_ACCESS_KEY_ID',shell=True, stdout=subprocess.PIPE).stdout.read().strip()
        secret_ID=subprocess.Popen('echo $AWS_SECRET_ACCESS_KEY',shell=True, stdout=subprocess.PIPE).stdout.read().strip()
        teamname=subprocess.Popen('echo $RESEARCH_GROUP_NAME',shell=True, stdout=subprocess.PIPE).stdout.read().strip()
        keypair=subprocess.Popen('echo $KEYPAIR_PATH',shell=True, stdout=subprocess.PIPE).stdout.read().strip()

        #Get AWS CLI directory location
        awsdir=subprocess.Popen('echo $AWS_CLI_DIR', shell=True, stdout=subprocess.PIPE).stdout.read().split()[0]
        rosettadir='%s/../rosetta/' %(awsdir)

	if len(awsdir) == 0:
                print 'Error: Could not find AWS scripts directory specified as $AWS_CLI_DIR. Please set this environmental variable and try again.'
                sys.exit()
	
	if len(AWS_ID) == 0: 
		print 'Error: Could not find the environmental variable $AWS_ACCOUNT_ID. Exiting'
		sys.exit()
	if len(key_ID) == 0: 
		print 'Error: Could not find the environmental variable $AWS_ACCESS_KEY_ID. Exiting'
                sys.exit()
	if len(secret_ID) == 0:
		print 'Error: Could not find the environmental variable $AWS_SECRET_ACCESS_ID. Exiting'
                sys.exit()
	if len(teamname) == 0: 
		print 'Error: Could not find the environmental variable $RESEARCH_GROUP_NAME. Exiting'
                sys.exit()
	if len(keypair) == 0: 
		print 'Error: Could not find the environmental variable $KEYPAIR_PATH. Exiting'
                sys.exit()

	return awsregion,AWS_ID,key_ID,secret_ID,teamname,keypair,awsdir

#================================================
if __name__ == "__main__":

	params=setupParserOptions()

	instance='t2.micro'
        numthreads=1
	numToRequest=numthreads

	if len(params['outdir']) == 0:
	        startTime=datetime.datetime.utcnow()
 		params['outdir']=startTime.strftime('%Y-%m-%d-%H%M%S')
	
	awsregion,AWS_ID,key_ID,secret_ID,teamname,keypair,awsdir=checkConflicts(params,params['outdir'])

	#Make output directory
	os.makedirs(params['outdir'])
	
	project=''
        #Get project name if exists
        if os.path.exists('.aws_relion_project_info'):
                project=linecache.getline('.aws_relion_project_info',1).split('=')[-1]

        #Launch instance
	cmd='%s/launch_AWS_instance.py --noEBS --instance=t2.micro --availZone=%sa --AMI=%s > %s/awslog_%i.log' %(awsdir,awsregion,params['AMI'],params['outdir'],counter)
        print '\n...booting up instance to format input files...\n' 
	subprocess.Popen(cmd,shell=True)
	time.sleep(20)
	counter=counter+1
      
        counter=0
     	instanceIDlist=[]
        instanceIPlist=[]
        
	isdone=0
        qfile='%s/awslog_%i.log' %(params['outdir'],counter)
       	while isdone == 0:
        	r1=open(qfile,'r')
                for line in r1:
                	if len(line.split()) == 2:
                        	if line.split()[0] == 'ID:':
                                	isdone=1
                r1.close()
       	        time.sleep(10)
        instanceIDlist.append(subprocess.Popen('cat %s/awslog_%i.log | grep ID'%(params['outdir'],counter), shell=True, stdout=subprocess.PIPE).stdout.read().split('ID:')[-1].strip())
	keypair=subprocess.Popen('cat %s/awslog_%i.log | grep ssh'%(params['outdir'],counter), shell=True, stdout=subprocess.PIPE).stdout.read().split()[3].strip()
        instanceIPlist.append(subprocess.Popen('cat %s/awslog_%i.log | grep ssh'%(params['outdir'],counter), shell=True, stdout=subprocess.PIPE).stdout.read().split('@')[-1].strip())

	#Move up files for preparing
	sys.exit()
	filesToUpload=['rosetta_prepare_initial_alignment.py','thread.sh','prepare_hybridize_from_hhsearch.pl']

	for uploadFile in filesToUpload: 

		cmd='scp -q -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -i %s %s/%s ubuntu@%s:~/'%(keypair,rosettadir,uploadFile,instanceIPlist[0])
        	subprocess.Popen(cmd,shell=True).wait()

	cmd='scp -q -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -i %s %s ubuntu@%s:~/'%(keypair,params['hhr'],instanceIPlist[0])
        subprocess.Popen(cmd,shell=True).wait()

	cmd='scp -q -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -i %s %s ubuntu@%s:~/'%(keypair,params['fasta'],instanceIPlist[0])
        subprocess.Popen(cmd,shell=True).wait()

