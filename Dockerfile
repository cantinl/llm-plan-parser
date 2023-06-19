FROM aiplanning/planutils:latest

# Install solvers and tools
RUN planutils install -y val
RUN planutils install -y lama-first

COPY requirements.txt requirements.txt
RUN python3 -m pip install -r requirements.txt

COPY . .
