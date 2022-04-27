FROM relaysh/core:latest-python
COPY step.py /relay/step.py
COPY ./relay-sdk-python /relay-sdk-python
RUN pip install --editable /relay-sdk-python
CMD /usr/local/bin/python /relay/step.py

LABEL "org.opencontainers.image.title"="workflow-run"
LABEL "org.opencontainers.image.description"="Run another Relay workfow (python version)"
LABEL "com.puppet.nebula.sdk.version"="v1"
