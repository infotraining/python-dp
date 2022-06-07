class Number:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)

    def eval(self, env):
        return self.value


class Variable:
    def __init__(self, varname):
        self.varname = varname

    def __repr__(self):
        return str(self.varname)

    def eval(self, env):
        return env.get(self.varname, 0)


class Sum:
    def __init__(self, *components):
        self.components = components

    def __repr__(self):
        inside = " + ".join(str(c) for c in self.components)
        return "(" + inside + ")"

    def eval(self, env):
        return sum(c.eval(env) for c in self.components)


class Product:
    def __init__(self, *components):
        self.components = components

    def __repr__(self):
        inside = " * ".join(str(c) for c in self.components)
        return "(" + inside + ")"

    def eval(self, env):
        retval = 1
        for c in self.components:
            retval *= c.eval(env)
        return retval


expr = Sum(Product(Number(2), Variable('x')), Number(1))
print(expr.eval({'x': 88}))
