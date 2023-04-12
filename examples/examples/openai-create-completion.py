import os
import gentrace
from dotenv import load_dotenv

load_dotenv()

pipeline = gentrace.Pipeline("test-gentrace-python-pipeline", os.getenv("GENTRACE_API_KEY"), host="http://localhost:3000/api/v1", openai_config={
    "api_key": os.getenv('OPENAI_KEY'),
})

pipeline.setup()

runner = pipeline.start()

openai = runner.get_openai()

result = openai.Completion.create(model="text-davinci-003", promptTemplate="Hello world {{ name }}", promptInputs={"name": "test"})

print("Result: ", result)

info = runner.submit()

print("Response: ", info["pipelineRunId"])

