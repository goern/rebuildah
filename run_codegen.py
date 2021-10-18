#!/usr/bin/env python3

# Copyright (C) 2021 Christoph Görn
#
# This file is part of rebuldah.
#
# rebuldah is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# rebuldah is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with rebuldah.  If not, see <http://www.gnu.org/licenses/>.

"""Runs protoc with the gRPC plugin to generate messages and gRPC stubs."""

from grpc_tools import protoc

protoc.main(
    (
        "",
        "-I./protos",
        "--python_out=.",
        "--grpc_python_out=.",
        "./protos/release_engineering.proto",
    )
)
