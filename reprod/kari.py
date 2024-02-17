import rsuanalyzer as ra

ra.visualize_chain("RRFBRRFB", 0)
ra.visualize_chain("LRFFLLBF", 0)
ra.visualize_chain("RRFBRRFB", 0)
ra.visualize_chain("LLBFLRFF", 0)

print(ra.calc_rsu("RRFBRRFB", 0, delta_=87))
print(ra.calc_rsu("LRFFLLBF", 0, delta_=87))
