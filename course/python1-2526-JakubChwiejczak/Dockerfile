FROM condaforge/miniforge3:latest

WORKDIR /app  

# Zainstaluj make (nie ma go w miniforge3)
RUN apt-get update && apt-get install -y make && rm -rf /var/lib/apt/lists/*

CMD ["/bin/bash", "-l"] 


COPY conda-lock-dev.yml .

# Zainstaluj conda-lock (nie ma go w miniforge3) i środowisko
RUN mamba install -y -n base conda-lock && \
    conda-lock install --mamba -n python1course-env conda-lock-dev.yml && \
    mamba clean --all -f -y

# Inicjalizuj mamba i aktywuj środowisko domyślnie
RUN mamba shell init --shell bash --root-prefix=/opt/conda && \
    echo "mamba activate python1course-env" >> ~/.bashrc
ENV PATH="/opt/conda/envs/python1course-env/bin:$PATH"

CMD ["/bin/bash", "-l"]