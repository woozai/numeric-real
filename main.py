
import sympy as sp

l = sp.symbols('l')
ln = sp.log
var = 0

f1 = 4.86 + 0.018 * l
f2 = l / 3000
f3 = (0.0012 + 0.0001 * sp.ln(l) + 0.000002 * sp.ln(l) ** 2) * l
f3_numeric_result = f3.subs(l, var).evalf()
f4 = 4.2 + 0.0015 * l ** (4/3)
f5 = 0.069 + 0.00156 * l + 0.00000047 * l ** 2

var = int(0.9189385986328126 * 1000)
print(f'var is {var}')
print(f'result for L1 D1 is {f1.subs(l, var)}')
print(f'result for L1 D2 is {f2.subs(l, var)}')
print(f'result for L1 D3 is {f3.subs(l, var).evalf()}')
print(f'result for L1 D4 is {f4.subs(l, var)}')
print(f'result for L1 D5 is {f5.subs(l, var)}\n')


var = int(66.71348487286782 * 100)
print(f'var is {var}')
print(f'result for L2 D1 is {f1.subs(l, var)}')
print(f'result for L2 D2 is {f2.subs(l, var)}')
print(f'result for L2 D3 is {f3.subs(l, var).evalf()}')
print(f'result for L2 D4 is {f4.subs(l, var)}')
print(f'result for L2 D5 is {f5.subs(l, var)}\n')

var = int(0.13014649785622756 * 1400)
print(f'var is {var}')
print(f'result for L3 D1 is {f1.subs(l, var)}')
print(f'result for L3 D2 is {f2.subs(l, var)}')
print(f'result for L3 D3 is {f3.subs(l, var).evalf()}')
print(f'result for L3 D4 is {f4.subs(l, var)}')
print(f'result for L3 D5 is {f5.subs(l, var)}\n')

var = 1200
print(f'var is {var}')
print(f'result for L4 D1 is {f1.subs(l, var)}')
print(f'result for L4 D2 is {f2.subs(l, var)}')
print(f'result for L4 D3 is {f3.subs(l, var).evalf()}')
print(f'result for L4 D4 is {f4.subs(l, var)}')
print(f'result for L4 D5 is {f5.subs(l, var)}\n')

var = int(0.6583747863769531 *1000)
print(f'var is {var}')
print(f'result for L56D1 is {f1.subs(l, var)}')
print(f'result for L56D2 is {f2.subs(l, var)}')
print(f'result for L56D3 is {f3.subs(l, var).evalf()}')
print(f'result for L56D4 is {f4.subs(l, var)}')
print(f'result for L56D5 is {f5.subs(l, var)}\n')

var = 3.8425 * 400
print(f'var is {var}')
print(f'result for L6 D1 is {f1.subs(l, var)}')
print(f'result for L6 D2 is {f2.subs(l, var)}')
print(f'result for L6 D3 is {f3.subs(l, var).evalf()}')
print(f'result for L6 D4 is {f4.subs(l, var)}')
print(f'result for L6 D5 is {f5.subs(l, var)}')

