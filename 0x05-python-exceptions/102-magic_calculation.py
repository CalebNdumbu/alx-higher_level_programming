def magic_calculation(a, b):
    result = 0  # LOAD_CONST, STORE_FAST

    for i in range(1, 3):  # SETUP_LOOP, GET_ITER, FOR_ITER
        try:  # SETUP_EXCEPT
            if i > a:  # COMPARE_OP, POP_JUMP_IF_FALSE
                raise Exception('Too far')  # LOAD_GLOBAL, LOAD_CONST, CALL_FUNCTION, RAISE_VARARGS
        except Exception:  # POP_TOP, POP_TOP, POP_TOP
            pass
        else:  # LOAD_FAST, BINARY_POWER, LOAD_FAST, BINARY_TRUE_DIVIDE, LOAD_FAST, BINARY_ADD, STORE_FAST
            result = (a ** b) / i + result
        finally:  # POP_BLOCK, JUMP_ABSOLUTE, LOAD_FAST, BINARY_ADD, STORE_FAST, BREAK_LOOP
            result += a + b
            break

    return result  # LOAD_FAST, RETURN_VALUE
