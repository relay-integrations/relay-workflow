FROM relaysh/core:latest
RUN apk --no-cache add bash ca-certificates jq
COPY step.sh /relay/step.sh
CMD ["/relay/step.sh"]

LABEL "org.opencontainers.image.title"="workflow-run"
LABEL "org.opencontainers.image.description"="Run another Relay workfow"
LABEL "com.puppet.nebula.sdk.version"="v1"
