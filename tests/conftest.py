import pytest

import jwt
import responses

from amocrm.v2.tokens import default_token_manager, TokensStorage


class FakeStorage(TokensStorage):

    def get_access_token(self):
        return jwt.encode({}, "tests").decode()


@pytest.fixture(autouse=True)
def _token():
    default_token_manager(client_id="", client_secret="", subdomain="test", redirect_url="", storage=FakeStorage())


@pytest.fixture(name="response_mock")
def _mock():
    with responses.RequestsMock() as _responses:
        yield _responses