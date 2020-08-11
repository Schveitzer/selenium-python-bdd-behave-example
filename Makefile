DOCKER_SELENIUM_VERSION=3.141.59-vanadium
DOCKER_ZALENIUM_VERSION=3.141.59-p25
CURRENT_PATH=$(shell pwd)
REPORT_DIRECTORY=test-report
REPORT_LOCAL_PATH=${CURRENT_PATH}/${REPORT_DIRECTORY}
DOWNLOAD_DIRECTORY=${REPORT_DIRECTORY}/Downloads

all: help

help:
	@echo ""
	@echo "-- Help Menu"
	@echo ""
	@echo "   1. make tests            - Starts testing"
	@echo "   2. make code.lint       - Code lint check files"
	@echo "   3. make report.generate - Generates the execution report"
	@echo "   4. make report.open     - Opens the report"
	@echo "   5. make zalenium        - Starts Zalenium service"
	@echo "   6. make down            - Stop Zalenium or Selenium service"
	@echo ""

tests:
	@behave

report.generate:
	@allure generate --clean ./test-report/allure-result/ -o ./test-report/allure-report

report.open:
	@allure open test-report/allure-report

code.lint:
	pylint tests

zalenium:
	@docker pull dosel/zalenium
	@docker pull elgalu/selenium:${DOCKER_ZALENIUM_VERSION}
	docker-compose up -d zalenium

remove:
	@docker rm -f zalenium

down:
	@docker network disconnect -f selenium-network selenium || true
	docker-compose down

setup:
	@pip install -r requirements.txt