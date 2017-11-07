#!/usr/bin/env python

import autograder_base
import os.path

from autograder_base import file_locations, AbsoluteTestCase, FractionalTestCase, main

tests = [
  ("Pipelined CPU add/lui/sll test",FractionalTestCase(os.path.join(file_locations,'CPU-add_lui_sll.circ'),os.path.join(file_locations,'reference_output/CPU-add_lui_sll.out'),1)),
  ("Pipelined CPU memory test",FractionalTestCase(os.path.join(file_locations,'CPU-mem.circ'),os.path.join(file_locations,'reference_output/CPU-mem.out'),1)),
  ("Pipelined CPU branch test",FractionalTestCase(os.path.join(file_locations,'CPU-branch.circ'),os.path.join(file_locations,'reference_output/CPU-branch.out'),1)),
  ("Pipelined CPU jump test",FractionalTestCase(os.path.join(file_locations,'CPU-jump.circ'),os.path.join(file_locations,'reference_output/CPU-jump.out'),1))
]

if __name__ == '__main__':
  main(tests)
