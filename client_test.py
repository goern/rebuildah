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


"""A tiny manual test client."""


import sys
import asyncio
import logging

import grpc
import release_engineering_pb2
import release_engineering_pb2_grpc


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


async def main() -> None:  # noqa: D103
    async with grpc.aio.insecure_channel("localhost:50051") as channel:
        stub = release_engineering_pb2_grpc.ReleaseEngineeringStub(channel)

        test_repo_name = "thoth-station/user-api"
        if len(sys.argv) == 2:
            test_repo_name = sys.argv[1]

        current_release = await stub.GetCurrentRelease(
            release_engineering_pb2.ContainerRepository(RepositoryURI=test_repo_name)
        )
        logging.info(f"getting current release of {test_repo_name}, got '{current_release}'!")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())
