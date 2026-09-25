""" primeCalc.py - 2026 by MFH

In reply to the (obvious) question:
Is it possible to give the set of primes the structure of a field,
P(#,×) such that 2 and 3 are the additive & multiplicative identity?

This implements the class Prime() with operations + and @
(and also unary & binary -, **, ~ = inverse, hence @~ = division).

It uses global lists `primes = [2, 3, ...]` and `rationals = [0, 1, ...]`
that are dynamically extended as required.

Ref: https://fr.quora.com/Est-il-possible-de-d%C3%A9finir-deux-op%C3%A9rations-times-avec-les-%C3%A9l%C3%A9ments-neutres-respectifs-2-et-3-sur-l-ensemble-des-nombres-premiers-P-de-mani%C3%A8re-que-P-times-forme-un-corps-commutatif/answer/Fred-Rich-18
"""
import math # for gcd
from fractions import Fraction

class Prime(int):
    """Utiliser les opérateurs + et @ pour l'addition et la multiplication
dans P(#,×). p.rational() donne la fraction associée à p ;
Prime.from_rational(f) donne le nombre premier associé à la fraction f.
"""
    #def __init__(self, n):
    #    #if not isprime(n): raise ValueError(f"{n = } isn't prime!")
    def __add__(self, other): return Prime.from_rational(self.rational()
        + Prime.rational(other)) if isprime(other) else self+other
    def __sub__(self, other): return Prime.from_rational(self.rational()
        - Prime.rational(other)) if isprime(other) else self-other
    def __neg__(self): return Prime.from_rational(-self.rational())
    def __invert__(self): return self**-1
    def __pow__(self, exponent): return Prime.from_rational(
        self.rational()**exponent) if exponent != 1 else self
    def __matmul__(self, other):
        return Prime.from_rational(self.rational() * Prime.rational(other))
    def rational(self) -> int | Fraction:
        "Return the unique rational corresponding to the prime p."
        #if not isprime(p): raise ValueError("p must be prime!")
        while self > primes[-1]: prime(len(primes)+10)
        pi = primes.index(self) # si l'indice est trop grand, on remplit
        while pi >= len(rationals): m = max(rationals)//1+2; rationals.extend(
            f for n in range(m-1, -m, -1) if (d := m-abs(n)) and
            math.gcd(n, d)==1 and (f := Fraction(n,d)) not in rationals)
        return rationals[pi]
    def from_rational(f: Fraction) -> 'Prime':
        "Return the unique prime corresponding to the fraction f."
        try: return prime(rationals.index(f)+1)
        except ValueError: rationals.append(f)
        return prime(len(rationals))

def prime(n: int) -> 'Prime':
    "Return the n-th prime."
    while n > len(primes): primes.append(next(p for p
        in range(primes[-1]+2, 1<<53, 2) if isprime(p)))
    return Prime(primes[n-1])

primes = [2, 3] ; rationals = [0, 1]
l = Fraction(1)

def isprime(n: int):
    if not n.is_integer() or n < 2: return False
    while n > primes[-1]:
        for p in vars().get('new',primes):
            if p**2 > n: return True
            if n % p == 0: return False
        L = len(primes); prime(L+10); new = primes[L:]
    return n in primes

### from here on, applications:

def table(n=10):
    prime(n)
    print(" P×Q:2", *[f"{p:3d}" for p in primes[1:n]])
    for p in primes[:n]:
        print(f"{p:2d}", *[f"{Prime(p)@q:3d}" for q in primes[:n]])
if __name__=="__main__":
 table(9)    
 print("Liste des rationnels:\n", *rationals)
