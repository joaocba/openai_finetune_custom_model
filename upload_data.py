import json
import openai
import os


# set openai API key
# openai.api_key = ''
# os.environ["OPENAI_API_KEY"] = ''
# in case it is already defined on windows path variables
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY", "")


# set file name with prepared data for upload
file_name = "training_data_prepared.jsonl"


# upload prepared jsonl file
upload_response = openai.File.create(
  file=open(file_name, "rb"),
  purpose='fine-tune'
)
file_id = upload_response.id
print(upload_response)


# start fine-tune process
fine_tune_response = openai.FineTune.create(training_file=file_id, model="davinci")
print(fine_tune_response)


# verify events
fine_tune_events = openai.FineTune.list_events(id=fine_tune_response.id)
print(fine_tune_events)

# run 'python upload_data.py' to upload the file and initiate the fine-tune - BEWARE: only run once or it will do multiple fine-tune requests which consume credit

# this will prompt info regarding fine-tune ID, example -> "message": "Created fine-tune: ft-F3z6F7gZP2KxkZgJlQEKuX3P"
# the "ft-F3z6F7gZP2KxkZgJlQEKuX3P" is the ID for the current fine-tune process
# to follow its status run the command 'openai --api-key <OPENAI API HERE> api fine_tunes.follow -i <FINE-TUNE ID HERE>'
# once its finished it will show a message "Job complete! Status: succeeded" and will show the name of the fine-tune model created
# example: davinci:ft-personal-2023-03-09-23-58-30
    ## in case it doesnt show a success message verify on openai playground page (https://platform.openai.com/playground) if the fine-tune model has been uploaded (may take some time depending on file size)
# model name can also be listed on openai playground page at model selector (https://platform.openai.com/playground)


# switch to 'app.py' to test the aplication file