# ccdc-dwayneinator-docker
dockerfile and python script to automate dwayneinator


## Dwayneinator Repository Credits

### Dwayne-Inator-5000 Repo

Dwayne-Inator-5000 can be found here:
[Github Repo](https://github.com/DSU-DefSec/DWAYNE-INATOR-5000)

The container uses the following fork of Dwayne-Intaor-5000:
[Github Repo](https://github.com/smayya337/DWAYNE-INATOR-5000)

## How to use

### Injects

#### Before Running the Image
1. All Injects must be stored into the upload folder prior to creating the image and running the image


#### The injects.csv

1. The CSV is used for the python script to automate the upload of each inject and their timesheet

the CSV is ordered as the following `title,body,file,starttime,endtime,rejecttime,points`

#### After running Dwayne

Note the timesheet is based of the the moment dwayne-inator-5000 started running:

i.e.

If you start Dwayne at 12:00PM, therefore the time 00:00:00 (the starting time for the inject) will be 12:00PM.

If the start time is at 00:45:00, then the inject will begin at 12:45PM. 45 Minutes after Dwayne's initialization.



### Docker Image

The docker image is based on ubuntu 22.04. Installs dependencies, clones the repo, builds dwayne, adds files.

NOTE: The time is set to Los Angeles Time Zone cause it's the most REAL time zone

other than that, nano and the injects are also placed in the docker file


#### Build the image

'docker build -t dwayne:latest .'

#### Run the image

'docker run -p 1337:80 -it score:latest'
> this runs dwayne's website on port 1337 instead of 80
> -it just makes it an interactive shell

### Python Script
> Assumes you are in the container's cli

The Script takes two required arguments.

#### Flags

````
 -u number of users/teams for the comp (requiredat least 1 team is needed)
 -t the timesheet for injects (required)
````

#### Usage

`python3 injects.py -u <insert number of teams (1+)> -t <insert injects csv or use injects.csv as default >`

### Running Dwayne

After running the script, and setting everything up. Do the following within the container:

`./DWAYNE-INATOR-5000`

Depending on how you launch the container, dwayne will be listening on http://127.0.0.1:1337 by default

He will be listening until your terminate the process.


