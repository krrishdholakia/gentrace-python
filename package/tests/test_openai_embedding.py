import http.client
import json
import os
import re
import uuid
from unittest.mock import create_autospec

import openai
import pytest
import requests
import responses
from urllib3.response import HTTPResponse

import gentrace


def test_openai_embedding_self_contained_pipeline_id(
    mocker, embedding_response, gentrace_pipeline_run_response, setup_teardown_openai
):
    # Setup OpenAI mocked request
    openai_api_key_getter = mocker.patch.object(openai.util, "default_api_key")
    openai_api_key_getter.return_value = "test-key"

    openai_request = mocker.patch.object(requests.sessions.Session, "request")

    response = requests.Response()
    response.status_code = 200
    response.headers["Content-Type"] = "application/json"
    response._content = json.dumps(embedding_response, ensure_ascii=False).encode(
        "utf-8"
    )

    openai_request.return_value = response

    # Setup Gentrace mocked response
    headers = http.client.HTTPMessage()
    headers.add_header("Content-Type", "application/json")

    body = json.dumps(gentrace_pipeline_run_response, ensure_ascii=False).encode(
        "utf-8"
    )

    gentrace_response = HTTPResponse(
        body=body,
        headers=headers,
        status=200,
        reason="OK",
        preload_content=False,
        decode_content=True,
        enforce_content_length=True,
    )

    gentrace_request = mocker.patch.object(gentrace.api_client.ApiClient, "request")
    gentrace_request.return_value = gentrace_response

    result = openai.Embedding.create(
        input="sample text",
        model="text-similarity-davinci-001",
        pipeline_id="testing-value",
    )

    assert uuid.UUID(result["pipelineRunId"]) is not None

    print(setup_teardown_openai)


def test_openai_embedding_self_contained_pipeline_id_with_slug(
    mocker, embedding_response, gentrace_pipeline_run_response, setup_teardown_openai
):
    # Setup OpenAI mocked request
    openai_api_key_getter = mocker.patch.object(openai.util, "default_api_key")
    openai_api_key_getter.return_value = "test-key"

    openai_request = mocker.patch.object(requests.sessions.Session, "request")

    response = requests.Response()
    response.status_code = 200
    response.headers["Content-Type"] = "application/json"
    response._content = json.dumps(embedding_response, ensure_ascii=False).encode(
        "utf-8"
    )

    openai_request.return_value = response

    # Setup Gentrace mocked response
    headers = http.client.HTTPMessage()
    headers.add_header("Content-Type", "application/json")

    body = json.dumps(gentrace_pipeline_run_response, ensure_ascii=False).encode(
        "utf-8"
    )

    gentrace_response = HTTPResponse(
        body=body,
        headers=headers,
        status=200,
        reason="OK",
        preload_content=False,
        decode_content=True,
        enforce_content_length=True,
    )

    gentrace_request = mocker.patch.object(gentrace.api_client.ApiClient, "request")
    gentrace_request.return_value = gentrace_response

    result = openai.Embedding.create(
        input="sample text",
        model="text-similarity-davinci-001",
        pipeline_slug="testing-value",
    )

    assert uuid.UUID(result["pipelineRunId"]) is not None

    print(setup_teardown_openai)


def test_openai_embedding_self_contained_no_pipeline_id(
    mocker, embedding_response, gentrace_pipeline_run_response, setup_teardown_openai
):
    openai.api_key = os.getenv("OPENAI_KEY")

    # Setup OpenAI mocked request
    openai_api_key_getter = mocker.patch.object(openai.util, "default_api_key")
    openai_api_key_getter.return_value = "test-key"

    openai_request = mocker.patch.object(requests.sessions.Session, "request")

    response = requests.Response()
    response.status_code = 200
    response.headers["Content-Type"] = "application/json"
    response._content = json.dumps(embedding_response, ensure_ascii=False).encode(
        "utf-8"
    )

    openai_request.return_value = response

    # Setup Gentrace mocked response
    headers = http.client.HTTPMessage()
    headers.add_header("Content-Type", "application/json")

    body = json.dumps(gentrace_pipeline_run_response, ensure_ascii=False).encode(
        "utf-8"
    )

    gentrace_response = HTTPResponse(
        body=body,
        headers=headers,
        status=200,
        reason="OK",
        preload_content=False,
        decode_content=True,
        enforce_content_length=True,
    )

    gentrace_request = mocker.patch.object(gentrace.api_client.ApiClient, "request")
    gentrace_request.return_value = gentrace_response

    result = openai.Embedding.create(
        input="sample text",
        model="text-similarity-davinci-001",
    )

    assert not hasattr(result, "pipelineRunId")
    print(setup_teardown_openai)


def test_openai_embedding_self_contained_pipeline_id_server(
    mocker, setup_teardown_openai
):
    openai.api_key = os.getenv("OPENAI_KEY")

    responses.add_passthru("https://api.openai.com/v1/")

    result = openai.Embedding.create(
        input="sample text",
        model="text-similarity-davinci-001",
        pipeline_id="testing-value-vivek",
    )

    assert uuid.UUID(result["pipelineRunId"]) is not None

    print("pipeline_id: ", result["pipelineRunId"])
    print(setup_teardown_openai)


def test_openai_embedding_self_contained_no_pipeline_id_server(setup_teardown_openai):
    openai.api_key = os.getenv("OPENAI_KEY")

    responses.add_passthru("https://api.openai.com/v1/")

    result = openai.Embedding.create(
        input="sample text",
        model="text-similarity-davinci-001",
    )

    assert not hasattr(result, "pipelineRunId")
    print(setup_teardown_openai)


def test_openai_embedding_pipeline_server(setup_teardown_openai):
    responses.add_passthru("https://api.openai.com/v1/")

    pipeline = gentrace.Pipeline(
        "test-gentrace-python-pipeline",
        host="http://localhost:3000/api/v1",
        openai_config={
            "api_key": os.getenv("OPENAI_KEY"),
        },
    )

    pipeline.setup()

    runner = pipeline.start()

    openai = runner.get_openai()

    openai.Embedding.create(input="sample text", model="text-similarity-davinci-001")

    info = runner.submit()

    assert uuid.UUID(info["pipelineRunId"]) is not None
    print(setup_teardown_openai)


@responses.activate
def test_openai_embedding_pipeline(
    mocker, embedding_response, gentrace_pipeline_run_response, setup_teardown_openai
):
    # Setup OpenAI mocked request
    responses.add(
        responses.POST,
        "https://api.openai.com/v1/embeddings",
        body=json.dumps(embedding_response, ensure_ascii=False),
        content_type="application/json",
    )

    # Setup Gentrace mocked response
    headers = http.client.HTTPMessage()
    headers.add_header("Content-Type", "application/json")

    body = json.dumps(gentrace_pipeline_run_response, ensure_ascii=False).encode(
        "utf-8"
    )

    gentrace_response = HTTPResponse(
        body=body,
        headers=headers,
        status=200,
        reason="OK",
        preload_content=False,
        decode_content=True,
        enforce_content_length=True,
    )

    gentrace_request = mocker.patch.object(gentrace.api_client.ApiClient, "request")
    gentrace_request.return_value = gentrace_response

    pipeline = gentrace.Pipeline(
        "test-gentrace-python-pipeline",
        host="http://localhost:3000/api/v1",
        openai_config={
            "api_key": os.getenv("OPENAI_KEY"),
        },
    )

    pipeline.setup()

    runner = pipeline.start()

    openai_handle = runner.get_openai()

    result = openai_handle.Embedding.create(
        input="sample text", model="text-similarity-davinci-001"
    )

    assert len(runner.step_runs) == 1

    info = runner.submit()

    assert uuid.UUID(info["pipelineRunId"]) is not None
    print(setup_teardown_openai)


@pytest.mark.asyncio
async def test_openai_embedding_self_contained_no_pipeline_id_server_async(
    setup_teardown_openai,
):
    openai.api_key = os.getenv("OPENAI_KEY")

    result = await openai.Embedding.acreate(
        input="sample text",
        model="text-similarity-davinci-001",
    )

    assert not hasattr(result, "pipelineRunId")
    print(setup_teardown_openai)


@pytest.mark.asyncio
async def test_openai_embedding_self_contained_pipeline_id_server_async(
    setup_teardown_openai,
):
    openai.api_key = os.getenv("OPENAI_KEY")

    result = await openai.Embedding.acreate(
        input="sample text",
        model="text-similarity-davinci-001",
        pipeline_id="testing-value",
    )

    assert uuid.UUID(result["pipelineRunId"]) is not None

    print(setup_teardown_openai)


@pytest.mark.asyncio
async def test_openai_embedding_pipeline_async(
    mocker,
    mockaio,
    embedding_response,
    gentrace_pipeline_run_response,
    setup_teardown_openai,
):
    # Setup OpenAI mocked request
    mockaio.post(
        "https://api.openai.com/v1/embeddings",
        status=200,
        body=json.dumps(embedding_response, ensure_ascii=False).encode("utf-8"),
    )

    # Setup Gentrace mocked response
    headers = http.client.HTTPMessage()
    headers.add_header("Content-Type", "application/json")

    body = json.dumps(gentrace_pipeline_run_response, ensure_ascii=False).encode(
        "utf-8"
    )

    gentrace_response = HTTPResponse(
        body=body,
        headers=headers,
        status=200,
        reason="OK",
        preload_content=False,
        decode_content=True,
        enforce_content_length=True,
    )

    gentrace_request = mocker.patch.object(gentrace.api_client.ApiClient, "request")
    gentrace_request.return_value = gentrace_response

    pipeline = gentrace.Pipeline(
        "test-gentrace-python-pipeline",
        host="http://localhost:3000/api/v1",
        openai_config={
            "api_key": "test-api-key",
        },
    )

    pipeline.setup()

    runner = pipeline.start()

    openai_handle = runner.get_openai()

    await openai_handle.Embedding.acreate(
        input="sample text", model="text-similarity-davinci-001"
    )

    assert len(runner.step_runs) == 1

    info = await runner.asubmit()

    print("info", info)

    assert uuid.UUID(info["pipelineRunId"]) is not None

    print(setup_teardown_openai)


def test_openai_embedding_pipeline_server_with_slug_param(setup_teardown_openai):
    responses.add_passthru("https://api.openai.com/v1/")

    pipeline = gentrace.Pipeline(
        slug="test-gentrace-python-pipeline",
        host="http://localhost:3000/api/v1",
        openai_config={
            "api_key": os.getenv("OPENAI_KEY"),
        },
    )

    pipeline.setup()

    runner = pipeline.start()

    openai = runner.get_openai()

    openai.Embedding.create(input="sample text", model="text-similarity-davinci-001")

    info = runner.submit()

    assert uuid.UUID(info["pipelineRunId"]) is not None
    print(setup_teardown_openai)


# @deprecated: this test uses the id parameter
def test_openai_embedding_pipeline_server_with_id_param(setup_teardown_openai):
    responses.add_passthru("https://api.openai.com/v1/")

    pipeline = gentrace.Pipeline(
        id="test-gentrace-python-pipeline",
        host="http://localhost:3000/api/v1",
        openai_config={
            "api_key": os.getenv("OPENAI_KEY"),
        },
    )

    pipeline.setup()

    runner = pipeline.start()

    openai = runner.get_openai()

    openai.Embedding.create(input="sample text", model="text-similarity-davinci-001")

    info = runner.submit()

    assert uuid.UUID(info["pipelineRunId"]) is not None
    print(setup_teardown_openai)
