FROM continuumio/miniconda3
RUN conda create -y -n env python=3.13.1
RUN echo "source activate env" > ~/.bashrc
RUN conda install ffmpeg
ENV PATH /opt/conda/envs/env/bin:$PATH
WORKDIR /scripts/pydub
COPY py3-13-1_requirements.txt .
RUN pip install --no-cache-dir -r py3-13-1_requirements.txt
