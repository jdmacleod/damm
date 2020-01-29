from damm import encode, check
import unittest

class GeneralTest(unittest.TestCase):

    def test_some_known_numbers(self):
        self.assertEqual(encode(572), 4)
        self.assertTrue(check(5724))
        self.assertEqual(encode('43881234567'), 9)
        self.assertFalse(check(5723))

class SwitchTest(unittest.TestCase):

    def test_simple_switch(self):
        """Test that a single digit switch changes the result."""

        for i in range(9):
            si = str(i)
            for j in range(i+1, 10):
                sj = str(j)
                self.assertNotEqual(encode(si+sj), encode(sj+si))

    def test_single_switch_offset(self):
        """Test that a single digit switch changes the result, no matter the digit before."""

        for k in range(10):
            sk = str(k)
            for i in range(9):
                si = str(i)
                for j in range(i+1, 10):
                    sj = str(j)
                    self.assertNotEqual(encode(sk+si+sj), encode(sk+sj+si))

class DigitTest(unittest.TestCase):

    def test_simple_digit(self):
        """Check that changing a single digit changes the check-digit."""

        for i in range(10):
            si = str(i)
            for j in range(10):
                sj = str(j)
                for k in range(10):
                    sk = str(k)
                    if j != k:
                        self.assertNotEqual(
                            encode(si+sj),
                            encode(si+sk))

class PhoneticTest(unittest.TestCase):

    def test_phonetic(self):
        """Check that a range of phonetic errors are caught by the check digit."""

        self.assertNotEqual(encode(13), encode(30))
        self.assertNotEqual(encode(14), encode(40))
        self.assertNotEqual(encode(15), encode(50))
        self.assertNotEqual(encode(16), encode(60))
        self.assertNotEqual(encode(17), encode(70))
        self.assertNotEqual(encode(18), encode(80))
        self.assertNotEqual(encode(19), encode(90))

def count_singles():
    """Count the fraction of single-digit errors missed."""

    checks = 0
    errors = 0

    for i in range(10):
        si = str(i)
        for j in range(10):
            sj = str(j)
            for k in range(10):
                sk = str(k)
                if j != k:
                    checks += 1
                    if encode(si+sj) == encode(si+sk):
                        errors += 1

    return errors / float(checks)

def count_switches():
    """Count the fraction of adjacent-digit-switch errors missed."""

    checks = 0
    errors = 0

    for k in range(10):
        sk = str(k)
        for i in range(9):
            si = str(i)
            for j in range(i+1, 10):
                sj = str(j)
                checks += 1
                if encode(sk+si+sj) == encode(sk+sj+si):
                    errors += 1

    return errors / float(checks)

def count_phonetics():
    """Count the fraction of phonetic errors missed."""

    checks = 7
    errors = 0
    if encode(13) == encode(30):
        errors += 1
    if encode(14) == encode(40):
        errors += 1
    if encode(15) == encode(50):
        errors += 1
    if encode(16) == encode(60):
        errors += 1
    if encode(17) == encode(70):
        errors += 1
    if encode(18) == encode(80):
        errors += 1
    if encode(19) == encode(90):
        errors += 1

    return errors / float(checks)

def count_twins():
    """Count the number of twin errors missed (aa -> bb)."""

    checks = 0
    errors = 0

    for k in range(10):
        sk = str(k)
        for i in range(10):
            si = str(i)
            for j in range(10):
                sj = str(j)
                checks += 1
                if encode(sk+si+si) == encode(sk+sj+sj):
                    errors += 1

    return errors / float(checks)

def count_jump_switch():
    """ abc -> cba """

    checks = 0
    errors = 0

    for k in range(10):
        sk = str(k)
        for l in range(10):
            sl = str(l)
            for a in range(9):
                sa = str(a)
                for b in range(a+1,10):
                    sb = str(b)
                    checks += 1
                    if encode(sk+sa+sl+sb) == encode(sk+sb+sl+sa):
                        errors += 1

    return errors / float(checks)


def count_jump_twins():
    """ Xaka -> Xbkb """

    checks = 0
    errors = 0

    for k in range(10):
        sk = str(k)
        for l in range(10):
            sl = str(l)
            for a in range(10):
                sa = str(a)
                for b in range(10):
                    sb = str(b)
                    checks += 1
                    if encode(sk+sa+sl+sa) == encode(sk+sb+sl+sb):
                        errors += 1

    return errors / float(checks)


