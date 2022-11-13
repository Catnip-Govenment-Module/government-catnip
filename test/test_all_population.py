# from fastapi.testclient import TestClient
# from fastapi import FastAPI
# from ..app.main import *
# from flask import url_for
# import pytest,sys


# client = TestClient(app)

# def test_population_endpoint():
#     response = client.get("/api/v1/populations")
#     assert response.status_code == 200

# def test_invalid_id1():
#     response = client.get("/fruit/99")
#     assert response.status_code == 404