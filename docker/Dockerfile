FROM ubuntu:20.04

RUN apt-get update && apt-get install -y openssh-server
RUN apt-get -y install git python3 vim python3-pip

RUN mkdir /var/run/sshd
RUN echo 'root:1q2w3e4r' | chpasswd
RUN sed -i 's/#*PermitRootLogin prohibit-password/PermitRootLogin yes/g' /etc/ssh/sshd_config

RUN sed -i 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' /etc/pam.d/sshd

ENV NOTVISIBLE="in users profile"
RUN echo "export VISIBLE=now" >> /etc/prifile

RUN git clone https://github.com/arumia/6nights_21_capston app

WORKDIR /root/app

RUN pip install -r requirments.txt

WORKDIR /root/app/template


EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]