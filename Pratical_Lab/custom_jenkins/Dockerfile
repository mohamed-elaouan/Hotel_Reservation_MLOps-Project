# Use the Jenkins LTS image
FROM jenkins/jenkins:lts

# Switch to root user
USER root

# Install Docker properly (modern method, no apt-key)
RUN apt-get update && \
    apt-get install -y ca-certificates curl gnupg && \
    install -m 0755 -d /etc/apt/keyrings && \
    curl -fsSL https://download.docker.com/linux/debian/gpg \
        | gpg --dearmor -o /etc/apt/keyrings/docker.gpg && \
    chmod a+r /etc/apt/keyrings/docker.gpg && \
    echo \
    "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian trixie stable" \
        > /etc/apt/sources.list.d/docker.list && \
    apt-get update && \
    apt-get install -y docker-ce docker-ce-cli containerd.io && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Add Jenkins user to docker group
RUN groupadd -f docker && \
    usermod -aG docker jenkins

# Create Docker directory
RUN mkdir -p /var/lib/docker

# Switch back to Jenkins user
USER jenkins







# Use the Jenkins image as the base image
# FROM jenkins/jenkins:lts

# # Switch to root user to install dependencies
# USER root

# # Install prerequisites and Docker
# RUN apt-get update -y && \
#     apt-get install -y apt-transport-https ca-certificates curl gnupg software-properties-common && \
#     curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - && \
#     echo "deb [arch=amd64] https://download.docker.com/linux/debian bullseye stable" > /etc/apt/sources.list.d/docker.list && \
#     apt-get update -y && \
#     apt-get install -y docker-ce docker-ce-cli containerd.io && \
#     apt-get clean

# # Add Jenkins user to the Docker group (create if it doesn't exist)
# RUN groupadd -f docker && \
#     usermod -aG docker jenkins

# # Create the Docker directory and volume for DinD
# RUN mkdir -p /var/lib/docker
# VOLUME /var/lib/docker

# # Switch back to the Jenkins user
# USER jenkins