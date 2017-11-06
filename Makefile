cpu-single-cycle:
	cp alu.circ cpu_tests
	cp regfile.circ cpu_tests
	cp mem.circ cpu_tests
	cp cpu.circ cpu_tests
	cd cpu_tests && python2.7 autograder_cpu.py -here
	mv cpu_tests/TEST_LOG TEST_LOG_SINGLE_CYCLE

cpu-pipelined:
	cp alu.circ tests/pipelined
	cp regfile.circ tests/pipelined
	cp mem.circ tests/pipelined
	cp cpu.circ tests/pipelined
	cd tests/pipelined && python2.7 autograder_cpu.py -here
	mv tests/pipelined/TEST_LOG TEST_LOG_PIPELINED