from protowhat.State import State
from protowhat.sct_syntax import ExGen, F, state_dec_gen
import pytest

state_dec = state_dec_gen(State, {})
Ex = ExGen(State, {})

@pytest.fixture
def addx():
    return lambda state, x: state + x

@pytest.fixture
def f():
    return F._from_func(lambda state, b: state + b, b = 'b')

@pytest.fixture
def f2():
    return F._from_func(lambda state, c: state + c, c = 'c')

def test_f_from_func(f):
    assert f('a') == 'ab'

def test_f_sct_copy_kw(addx):
    assert F()._sct_copy(addx)(x = 'x')('state') == 'statex'

def test_f_sct_copy_pos(addx):
    assert F()._sct_copy(addx)('x')('state') == 'statex'

def test_ex_sct_copy_kw(addx):
    assert Ex('state')._sct_copy(addx)(x = 'x')._state == 'statex'

def test_ex_sct_copy_pos(addx):
    assert Ex('state')._sct_copy(addx)('x')._state == 'statex'

def test_f_2_funcs(f, addx):
    g = f._sct_copy(addx)
    
    assert g(x = 'x')('a') == 'abx'

def test_f_add_unary_func(f):
    g = f >> (lambda state: state + 'c')
    assert g('a') == 'abc'

def test_f_add_f(f, f2):
    g = f >> f2
    assert g('a') == 'abc'

def test_f_from_state_dec(addx):
    dec_addx = state_dec(addx)
    f = dec_addx(x = 'x')
    isinstance(f, F)
    assert f('state') == 'statex'

@pytest.fixture
def ex():
    return Ex('state')._sct_copy(lambda state, x: state + x)('x')

def test_ex_add_f(ex, f):
    (ex >> f)._state = 'statexb'

def test_ex_add_unary(ex):
    (ex >> (lambda state: state + 'b'))._state == 'statexb'

def test_ex_add_ex_err(ex):
    with pytest.raises(BaseException): ex >> ex

def test_f_add_ex_err(f, ex):
    with pytest.raises(BaseException): f >> ex


from protowhat.Reporter import Reporter
def test_state_dec_instant_eval():
    state = State("student_code", "", "", None, None, {}, {}, Reporter())

    @state_dec
    def stu_code(state, x = 'x'):
        return state.student_code + x

    assert stu_code(state) == "student_codex"

