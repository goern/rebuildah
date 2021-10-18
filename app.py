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

"""The implementation ..."""

import asyncio
import logging

import grpc
import semver

import release_engineering_pb2
import release_engineering_pb2_grpc


from tornado import httpclient, escape
from tornado.httputil import HTTPHeaders, url_concat


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

_QUAY_URL_TEMPLATE = "https://quay.io/api/v1/repository/{repo}/tag/"


class ReleaseEngineeringServicer(release_engineering_pb2_grpc.ReleaseEngineering):
    """Provides methods that implement functionality of ReleaseEngineering."""

    def GetCurrentRelease(  # noqa: N802
        self, repository: release_engineering_pb2.ContainerRepository, unuser_context
    ) -> release_engineering_pb2.SemanticVersion:
        """Get the current release of a Container Registry as a SemVer."""
        logger.debug("received a request to get the current release semver tag...")

        # let's get the list of tags of the requested repo
        if repository is not None:
            release_tags = []
            http_client = httpclient.HTTPClient()

            _headers = HTTPHeaders({"content-type": "application/json"})
            _params = {"onlyActiveTags": True}
            _url = url_concat(_QUAY_URL_TEMPLATE.format(repo=repository.RepositoryURI), _params)
            logger.debug(_url)

            try:
                response = http_client.fetch(
                    _url,
                    headers=_headers,
                )

                # convert response to a list of release tags,
                # filter out pr builds etc, cut off leading 'v' as it is not part of a semver
                _json = escape.json_decode(response.body)
                all_tags = [tag["name"] for tag in _json["tags"]]
                release_tags = [semver.parse(tag[1:]) for tag in all_tags if tag.startswith("v")]

                logger.debug(release_tags)
            except httpclient.HTTPError as e:
                logger.error("Error: " + str(e))
                return None

            except Exception as e:
                logger.error("Error: " + str(e))
                return None

            http_client.close()

            # now that we got all the release tags,
            # let's find the latest/greatest
            # as release_tags is an OrderedDict, its easy...
            logger.debug(release_tags[0])
            latest_release = release_tags[0]

            # as the latest release should just have x.y.z
            return release_engineering_pb2.SemanticVersion(
                major=latest_release["major"], minor=latest_release["minor"], patch=latest_release["patch"]
            )
        else:
            return None


async def serve() -> None:
    """Implement the main server loooop."""
    server = grpc.aio.server()
    release_engineering_pb2_grpc.add_ReleaseEngineeringServicer_to_server(ReleaseEngineeringServicer(), server)
    server.add_insecure_port("[::]:50051")
    await server.start()
    await server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    logger.info("starting...")
    asyncio.get_event_loop().run_until_complete(serve())
