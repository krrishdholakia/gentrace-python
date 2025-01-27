import os

import gentrace
import openai
from dotenv import load_dotenv

load_dotenv()

gentrace.init(
    api_key=os.getenv("GENTRACE_API_KEY"),
    host="http://localhost:3000/api/v1",
    log_level="info",
)

gentrace.configure_openai()

openai.api_key = os.getenv("OPENAI_KEY")

result = openai.Completion.create(
    pipeline_slug="text-generation-test-2",
    model="text-davinci-003",
    prompt_template="Hello world {{ name }}",
    prompt_inputs={"name": "test"},
)

gentrace.flush()

print("Result: ", result["pipelineRunId"])
