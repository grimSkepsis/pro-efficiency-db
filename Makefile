FLASK_APP = main2.py

.PHONY: run_dev
run_dev:
	@echo "Running development server"
	FLASK_ENV=development flask --app $(FLASK_APP) --debug run 

	
.PHONY: run_prod
run_prod:
	@echo "Running prod server"
	FLASK_ENV=prod flask --app $(FLASK_APP) run