SHELL := /bin/bash

# Colors
CCGREEN=\033[0;32m
CCEND=\033[0m

.PHONY:
all: install-pip install-pip run

.PHONY:
install-pip:
	@echo -e "${CCGREEN}Installing pip...${CCEND}"
	@curl -sS https://bootstrap.pypa.io/get-pip.py | python3.10
	@python3.10 -m pip install --upgrade pip
	@echo -e "${CCGREEN}Done!${CCEND}"

.PHONY:
install-tabulate:
	@echo -e "${CCGREEN}Installing tabulate...${CCEND}"
	@pip install tabulate
	@echo -e "${CCGREEN}Done!${CCEND}"

.PHONY:
run:
	@echo -e "${CCGREEN}Running main...${CCEND}"
	@echo -e "${CCGREEN}And it will probably take a while.${CCEND}"
	@echo -e "${CCGREEN}  > Note: treat False at Fermat as True at Miller-Rabin,${CCEND}"
	@echo -e "${CCGREEN}  > as the first tests primality and the latter tests if a number is composite.${CCEND}"

	@python3.10 main.py > output.txt
