from dotenv import load_dotenv

from fixtures.aioresponse import mockaio
from fixtures.completion import completion_response
from fixtures.embedding import embedding_response
from fixtures.gentrace import gentrace_pipeline_run_response


def pytest_configure():
    load_dotenv()
