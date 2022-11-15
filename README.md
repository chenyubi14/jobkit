# Jobkit
Have you ever felt that it is painful to run job scripts in a cluster? A lot of repetitive works can be done automatically. Jobkit contains a bunch of shell codes to help you run jobs smoothly. You just need to add the commands in `.myshrc` to your .bashrc or .bash_profile

Remember to read through the `.myshrc` file and make necessary changes! You may need to `source .bashrc` to make the functions take effect

Here is a list of useful commands.

## shell commands abbreviation
Are you sick of typing `squeue -u username`? Define some commands abbreviations. For example, the `q` defined in .myshrc can print your running jobs in queue.

## job management and submission
The usage of every function is written as comments. Please read my comments carefully.

Define a template for submitting jobs. You can use the same template for every job submission. I offered one job template in the `submit.job` file

When you submit jobs, don't just use `sbatch`! Use the function `run` to store the job number and submission time. 

Have you ever been confused by what job is running? Use `printjob_direc job_number`! It will bring you to the directory you submitted the job with job_number.

The jobs you submitted are saved in $HOME/jobs.number (should use the `run` function to have jobs.number)
The jobs you finished are saved in $HOME/finished.jobs.number (should use the submit.job template to have finished.jobs.number)

## sync files between servers
How about syncing files? Are you tired of writing `scp`? These three functions will help you! `remote2local`, `local2remote`, `remotemulti`

`remote2local` will sync files from a remote computer to a local directory

`local2remote` will sync local files to a remote computer

`remotemulti` will generate commands for using `remote2local`. It also checks whether the file exists.

Example usage: 

`local2remote pod /directory/on/pod/ local_files_1 local_files_2 ` will sync local files 1,2,... to the remote cluster saved as pod.

`remote2local pod ./ a_file_on_pod` will sync a file on pod to the local folder './', which is equivalent to `scp -r $username@pod-login1.cnsi.ucsb.edu:a_file_on_pod ./`. You may know that `scp` only sync one file at a time. However, you can also sync multiple files simultaneously by one command. As indicated by this website (https://stackoverflow.com/questions/16886179/scp-or-sftp-copy-multiple-files-with-single-command), it is done by `scp -r $username@pod-login1.cnsi.ucsb.edu:{file1,file2,file3,file4} ./`


`remotemulti file1 file2 file3` will output a job script for you.

## update files
Does your cluster clean files every several months? Are you sick of your important files being removed? Use `touchall`!

## sshconfig
The file sshconfig has two tricks to save typing passwords frequently

## draw.datafile_template.py
Use `python draw.datafile_template.py yourdata.txt` to plot a data file
