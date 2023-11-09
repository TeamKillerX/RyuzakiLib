
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2020-2023 (c) Randy W @xtdevs, @xtsea
#
# from : https://github.com/TeamKillerX
# Channel : @RendyProjects
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU as Affero General Public License published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FOR A PARTICULAR PURPOSE FITNESS.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

FROM rendyprojects/python:latest

# Set the working directory to /app/
WORKDIR /app/

# Update package list and install required packages
RUN apt-get -qq update && \
    apt-get -qq install -y --no-install-recommends \
    curl \
    git \
    gnupg2 \
    unzip \
    wget \
    python3-pip \
    ffmpeg \
    neofetch && \
    rm -rf /var/lib/apt/lists/*  # Remove the package lists after installation to reduce Docker image size

# Copy the current directory contents into the container at /app/
COPY . .

# Upgrade pip and setuptools
RUN pip3 install --upgrade pip setuptools
RUN pip3 install -r requirements.txt

CMD [ "python3", "-m", "buildbot"]
