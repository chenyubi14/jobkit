# Jobkit
Have you even felt that it is painful to run job scripts in a cluster? A lot of repetitive works can be done automatically. Jobkit contains a bunch of shell codes to help you run jobs smoothly. You just need to add the commands in .myshrc to your .bashrc or .bash_profile

Remember to read through the file and make necessary changes!

Here is a list of useful commands.

## shell commands abbreviation
use alias to define commands abbreviations. For example, the "q" defined in .myshrc can print your running jobs in queue.

## An entire system for job submissions. 
The usage of every function is written as comments. Please read my comments carefully.

Define a template for submitting jobs.

when you submit jobs, don't just use sbatch! use the function "run" to store the job number and submission time. 

Have you even got confused by what job is running? Use "printjob_direc job_number"! It will bring you to the directory you submitted job_number.

## sync files between servers
How about syncing files? Are you tired of writing scp? These three functions will help you! remote2local, local2remote, remotemulti

remote2local will sync files from a remote computer to a local directory

local2remote will sync locat files to a local computer

remotemulti will generate commands for using remote2local. It also checks whether the file exists.

## update files
Does your cluster clean files every several months? Are you sick of your important files being removed? Use touchall!
