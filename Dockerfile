############################################################
# Dockerfile to run a Django-based web application
# Based on an Ubuntu Image
############################################################

# Set the base image to use to Ubuntu
FROM centos:7

# Set the file maintainer (your name - the file's author)
MAINTAINER Marc Velay

# Set env variables used in this Dockerfile (add a unique prefix, such as ONBOARDING)
# Local directory with project source
ENV ONBOARDING_SRC=/
# Directory in container for all project files
ENV ONBOARDING_SRVHOME=/srv
# Directory in container for project source files
ENV ONBOARDING_SRVPROJ=/srv

# Update the default application repository sources list
RUN yum -y update
RUN yum -y upgrade
RUN yum -y install epel-release
RUN yum install -y python34
RUN curl -O https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py


# Create application subdirectories
#WORKDIR $ONBOARDING_SRVHOME
#RUN mkdir media static logs
#VOLUME ["$ONBOARDING_SRVHOME/media/", "$ONBOARDING_SRVHOME/logs/"]

# Copy application source code to SRCDIR
COPY $ONBOARDING_SRC $ONBOARDING_SRVPROJ
RUN ls  $ONBOARDING_SRVPROJ

# Install Python dependencies
RUN pip3 install -r $ONBOARDING_SRVPROJ/requirements.txt

# Port to expose
EXPOSE 8000

# Copy entrypoint script into the image
WORKDIR $ONBOARDING_SRVPROJ
COPY ./docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]