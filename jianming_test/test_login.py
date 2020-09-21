import pytest


@pytest.mark.parametrize("inr,exp",
                         [("1+3", 4),
                          ("12+13", 25),
                          ("30+38", 68)
                          ])
def test_eval(inr, exp):
    a = inr
    print("\n"+a)
    assert eval(a) == exp
