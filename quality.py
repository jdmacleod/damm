"""Check the quality of the Damm check digit implementation."""


from test_damm import count_singles, count_switches, count_phonetics
from test_damm import count_twins
from test_damm import count_jump_twins, count_jump_switch

print "Single-digit errors:    ", 1-count_singles()
print "Neighbour-switch errors:", 1-count_switches()
print "Phonetic errors:        ", 1-count_phonetics()
print "Twin digit errors:      ", 1-count_twins()
print "Jump-switch errors:     ", 1-count_jump_switch()
print "Jump-twin errors:       ", 1-count_jump_twins()

