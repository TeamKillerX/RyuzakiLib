#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2020-2023 (c) Randy W @xtdevs, @xtsea
#
# from : https://github.com/TeamKillerX
# Channel : @RendyProjects
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

# JANGAN COPAS INI LU KEK KONTOL
# TANYA KE SUPPORT @KillerXSupport

import requests
import json
from flask import Flask

app = Flask(__name__)

BLACKLIST = [
    -1001050982793,
    -1001387666944,
    -1001030379032,
    -1001042324135,
    -1001612784732,
    -1001361294038,
    -1001108308377,
    -1001113421561,
    -1001349472891,
    -1001084578942,
    -1001067163791,
    -1001779729857,
    -1001554560763,
    -1001307868573,
    -1001504193825,
    -1001311056733,
]


@app.route("/", methods=["GET"])
def root():
    return "Check Api Endpoint: https://download.randydev.my.id"


@app.route("/blacklist", methods=["GET"])
def group_blacklist():
    data_set = {"randydev": 1191668125, "gcast_blacklist": BLACKLIST}
    return json.dumps(data_set)
