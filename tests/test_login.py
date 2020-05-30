import pytest

from xing import Xing


def test_login_success(caplog):
    Xing.login()
    assert "login success" in caplog.text


@pytest.mark.parametrize(
    "params",
    [{"id_": "WRONG"}, {"pw": "WRONG"}, {"cert_pw": "WRONG"}],
    ids=["wrong_id", "wrong_pw", "wrong_cert_pw"],
)
@pytest.mark.parametrize("demo", [True, False], ids=["demo-server", "real-server"])
def test_login_fail(params, demo, caplog):
    Xing.login(demo=demo, **params)
    if not (demo is True and "cert_pw" in params):
        assert "login fail" in caplog.text

    # avoid invalidation of certificate
    Xing.login()
