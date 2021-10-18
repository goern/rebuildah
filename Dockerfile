FROM quay.io/thoth-station/s2i-thoth-ubi8-py38:v0.32.0
LABEL "io.openshift.s2i.build.image"="quay.io/thoth-station/s2i-thoth-ubi8-py38:v0.32.0" \
      "io.openshift.s2i.build.source-location"="."

ENV THAMOS_RUNTIME_ENVIRONMENT="" \
ENABLE_MICROPIPENV=1 \
THOTH_ADVISE=0 \
THOTH_DRY_RUN=0 \
THOTH_PROVENANCE_CHECK=0

USER root
# Copying in source code
COPY . /tmp/src
# Change file ownership to the assemble user. Builder image must support chown command.
RUN chown -R 1001:0 /tmp/src
USER 1001
# Assemble script sourced from builder image based on user input or image metadata.
# If this file does not exist in the image, the build will fail.
RUN /usr/libexec/s2i/assemble
# Run script sourced from builder image based on user input or image metadata.
# If this file does not exist in the image, the build will fail.
CMD /usr/libexec/s2i/run
