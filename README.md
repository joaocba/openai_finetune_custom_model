## OpenAi Finetune Model

#### Technology: OpenAi
#### Method: Fine-Tuning (custom model)

#### Description:
This allows to prepare data and upload data to fine-tune a AI model (custom) so it assumes a role that it was trained for. Results with this model are aimed to enhance the way the AI answers or the role it should assume, this require a large input of data (mainly question -> answer) for the model to deliver a proper output. The objective of fine-tuning is to shape the model.

This also features a chatbot web app made with Flask to interact with the custom finetuned model.

### How to run (commands Windows terminal with Python 2.7):

#### Part One: Prepare Data
- **Define necessary parameters (OpenAi API key, ...) and training data on file 'prepare_data.py'**
- Initialize virtual environment and install dependencies run:

	    virtualenv env
	    env\Scripts\activate
	    pip install flask python-dotenv
        pip install openai

- To create a jsonl file with training data run:

	    python prepare_data.py

- After generating output file to normalize the data for proper fine-tune process run: 

		openai tools fine_tunes.prepare_data -f training_data.jsonl

- This will generate a new file called 'training_data_prepared.jsonl'

#### Part Two: Upload Data and Start Fine-Tune
- **First define args and prepared file name on file 'upload_data.py'**
- To upload the file and initiate the fine-tune run: (BEWARE: only run once or it will do multiple fine-tune requests which consume more credit)

		python upload_data.py

- This will prompt info regarding fine-tune ID and the status, example:
	> "message": "Created fine-tune: ft-F3z6F7gZP2KxkZgJlQEKuX3P"

- The "ft-F3z6F7gZP2KxkZgJlQEKuX3P" is the example ID for the current fine-tune process
- To follow its status run:

		openai --api-key <OPENAI API HERE> api fine_tunes.follow -i <FINE-TUNE ID HERE>

- Once its finished it will show a message:
	> "Job complete! Status: succeeded"

- And will show the name of the fine-tune model created:
	> davinci:ft-personal-2023-03-09-23-58-30

- **Note:** in case it doesnt show a success message verify on openai playground page (https://platform.openai.com/playground) if the fine-tune model has been uploaded (may take some time depending on file size)
- Model name is also listed on openai playground page at Model selector (https://platform.openai.com/playground)

#### Part Three: Run the app
- **Define necessary parameters (OpenAi API key, ...) on file 'app.py'**

- Initialize the app:

	    flask run

- Enter "http://localhost:5000" on browser to interact with app


#### Changelog
- v0.1
	- initial build