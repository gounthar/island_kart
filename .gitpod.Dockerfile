FROM gitpod/workspace-python

USER root

RUN apt-get update && apt-get install -y gcc-11 && \
    python3 -m venv /workspace/island_kart && /workspace/island_kart/pip install pynput emoji