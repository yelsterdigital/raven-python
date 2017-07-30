import pytest

from .models import MyTestModel

import ipdb; ipdb.set_trace()

@pytest.fixture
def mytest_model():
    return MyTestModel


@pytest.fixture(scope='function', autouse=False)
def user_instance(request, admin_user):
    request.cls.user = admin_user

