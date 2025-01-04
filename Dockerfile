# OS
FROM ubuntu:22.04

#Install dependencies
RUN apt update && apt upgrade -y
RUN apt-get upgrade -y
RUN apt install -y wget
RUN apt install -y openssh-server
run apt-get  -y install golang-go
run apt install gcc -y
run apt install build-essential -y
run apt install -y sqlite3
run apt install git -y

# Running that dwayne

run git clone https://github.com/smayya337/DWAYNE-INATOR-5000.git

workdir "/DWAYNE-INATOR-5000"
run go build
add dwayne.conf .
add injects.conf .

RUN DEBIAN_FRONTEND=noninteractive TZ=America/Los_Angeles apt-get -y install tzdata

run apt install nano -y
add injects.py .
add injects.csv .
add upload ./upload