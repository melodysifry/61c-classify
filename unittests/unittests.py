from unittest import TestCase
from framework import AssemblyTest, print_coverage


class TestAbs(TestCase):
    def test_minus_one(self):
        t = AssemblyTest(self, "abs.s")
        t.input_scalar("a0", -1)
        t.call("abs")
        t.check_scalar("a0", 1)
        t.execute()
    def test_zero(self):
        t = AssemblyTest(self, "abs.s")
        # load 0 into register a0
        t.input_scalar("a0", 0)
        # call the abs function
        t.call("abs")
        # check that after calling abs, a0 is equal to 0 (abs(0) = 0)
        t.check_scalar("a0", 0)
        # generate the `assembly/TestAbs_test_zero.s` file and run it through venus
        t.execute()

    def test_one(self):
        # same as test_zero, but with input 1
        t = AssemblyTest(self, "abs.s")
        t.input_scalar("a0", 1)
        t.call("abs")
        t.check_scalar("a0", 1)
        t.execute()

    @classmethod
    def tearDownClass(cls):
        print_coverage("abs.s", verbose=False)


class TestRelu(TestCase):
    def test_simple(self):
        t = AssemblyTest(self, "relu.s")
        # create an array in the data section
        array0 = t.array([1, -2, 3, -4, 5, -6, 7, -8, 9])
        # load address of `array0` into register a0
        t.input_array("a0", array0)
        # set a1 to the length of our array
        t.input_scalar("a1", len(array0))
        # call the relu function
        t.call("relu")
        # check that the array0 was changed appropriately
        t.check_array(array0, [1, 0, 3, 0, 5, 0, 7, 0, 9])
        # generate the `assembly/TestRelu_test_simple.s` file and run it through venus
        t.execute()

    def test_empty(self):
        t = AssemblyTest(self, "relu.s")
        # create an array in the data section
        array0 = t.array([])
        # load address of `array0` into register a0
        t.input_array("a0", array0)
        # set a1 to the length of our array
        t.input_scalar("a1", len(array0))
        # call the relu function
        t.call("relu")
        # check that the array0 was changed appropriately
        # t.check_array(array0, [])
        # generate the `assembly/TestRelu_test_simple.s` file and run it through venus
        t.execute(code=78)
    
    def test_all_neg(self):
        t = AssemblyTest(self, "relu.s")
        # create an array in the data section
        array0 = t.array([-2, -3, -4])
        # load address of `array0` into register a0
        t.input_array("a0", array0)
        # set a1 to the length of our array
        t.input_scalar("a1", len(array0))
        # call the relu function
        t.call("relu")
        # check that the array0 was changed appropriately
        t.check_array(array0, [0, 0, 0])
        # generate the `assembly/TestRelu_test_simple.s` file and run it through venus
        t.execute()

    def test_zeroes(self):
        t = AssemblyTest(self, "relu.s")
        # create an array in the data section
        array0 = t.array([0, 0, 0])
        # load address of `array0` into register a0
        t.input_array("a0", array0)
        # set a1 to the length of our array
        t.input_scalar("a1", len(array0))
        # call the relu function
        t.call("relu")
        # check that the array0 was changed appropriately
        t.check_array(array0, [0, 0, 0])
        # generate the `assembly/TestRelu_test_simple.s` file and run it through venus
        t.execute()

    def test_all_pos(self):
        t = AssemblyTest(self, "relu.s")
        # create an array in the data section
        array0 = t.array([1, 2, 3])
        # load address of `array0` into register a0
        t.input_array("a0", array0)
        # set a1 to the length of our array
        t.input_scalar("a1", len(array0))
        # call the relu function
        t.call("relu")
        # check that the array0 was changed appropriately
        t.check_array(array0, [1, 2, 3])
        # generate the `assembly/TestRelu_test_simple.s` file and run it through venus
        t.execute()

    @classmethod
    def tearDownClass(cls):
        print_coverage("relu.s", verbose=False)


class TestArgmax(TestCase):
    def test_simple(self):
        t = AssemblyTest(self, "argmax.s")
        # create an array in the data section
        array0 = t.array([1, 2, 9])
        # load address of the array into register a0
        t.input_array("a0", array0)
        # set a1 to the length of the array
        t.input_scalar("a1", len(array0))
        # call the `argmax` function
        t.call("argmax")
        # check that the register a0 contains the correct output
        t.check_scalar("a0", 2)
        # generate the `assembly/TestArgmax_test_simple.s` file and run it through venus
        t.execute()

    def test_empty(self):
        t = AssemblyTest(self, "argmax.s")
        # create an array in the data section
        array0 = t.array([])
        # load address of `array0` into register a0
        t.input_array("a0", array0)
        # set a1 to the length of our array
        t.input_scalar("a1", len(array0))
        # call the relu function
        t.call("argmax")
        # check that the array0 was changed appropriately
        # t.check_array(array0, [])
        # generate the `assembly/TestRelu_test_simple.s` file and run it through venus
        t.execute(code=77)
        
    def test_all_neg(self):
        t = AssemblyTest(self, "argmax.s")
        # create an array in the data section
        array0 = t.array([-2, -3, -4])
        # load address of `array0` into register a0
        t.input_array("a0", array0)
        # set a1 to the length of our array
        t.input_scalar("a1", len(array0))
        # call the argmax function
        t.call("argmax")
        # check that the array0 was changed appropriately
        t.check_scalar("a0", 0)
        # generate the `assembly/TestRelu_test_simple.s` file and run it through venus
        t.execute()

    def test_zeroes(self):
        t = AssemblyTest(self, "argmax.s")
        # create an array in the data section
        array0 = t.array([0, 0, 0])
        # load address of `array0` into register a0
        t.input_array("a0", array0)
        # set a1 to the length of our array
        t.input_scalar("a1", len(array0))
        # call the argmax function
        t.call("argmax")
        # check that the array0 was changed appropriately
        t.check_scalar("a0", 0)
        # generate the `assembly/TestRelu_test_simple.s` file and run it through venus
        t.execute()

    def test_mixed(self):
        t = AssemblyTest(self, "argmax.s")
        # create an array in the data section
        array0 = t.array([-1, 2, 3, -4])
        # load address of `array0` into register a0
        t.input_array("a0", array0)
        # set a1 to the length of our array
        t.input_scalar("a1", len(array0))
        # call the relu function
        t.call("argmax")
        # check that the array0 was changed appropriately
        t.check_scalar("a0", 2)
        # generate the `assembly/TestRelu_test_simple.s` file and run it through venus
        t.execute()

    @classmethod
    def tearDownClass(cls):
        print_coverage("argmax.s", verbose=False)


class TestDot(TestCase):
    def test_simple(self):
        t = AssemblyTest(self, "dot.s")
        # create arrays in the data section
        array0 = t.array([1, 2, 3, 4])
        array1 = t.array([2, 3, 4, 5])
        # load array addresses into argument registers
        t.input_array("a0", array0)
        t.input_array("a1", array1)
        # load array attributes into argument registers
        t.input_scalar("a2", len(array0))
        t.input_scalar("a3", 1)
        t.input_scalar("a4", 1)
        # call the `dot` function
        t.call("dot")
        # check the return value
        t.check_scalar("a0", 40)
        t.execute()

    def test_stride(self): 
        t = AssemblyTest(self, "dot.s")
        # create arrays in the data section
        array0 = t.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
        array1 = t.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
        t.input_array("a0", array0)
        t.input_array("a1", array1)
        t.input_scalar("a2", 3)
        t.input_scalar("a3", 1)
        t.input_scalar("a4", 2)
        t.call("dot")
        t.check_scalar("a0", 22)
        t.execute()

    def test_my_strides(self):
        t = AssemblyTest(self, "dot.s")
        # create arrays in the data section
        array0 = t.array([1, 4])
        array1 = t.array([2, -3, 4, -5])
        # load array addresses into argument registers
        t.input_array("a0", array0)
        t.input_array("a1", array1)
        # load array attributes into argument registers
        t.input_scalar("a2", len(array0))
        t.input_scalar("a3", 1)
        t.input_scalar("a4", 2)
        # call the `dot` function
        t.call("dot")
        # check the return value
        t.check_scalar("a0", 18)
        t.execute()

    def test_empty(self):
        t = AssemblyTest(self, "dot.s")
        # create arrays in the data section
        array0 = t.array([])
        array1 = t.array([])
        # load array addresses into argument registers
        t.input_array("a0", array0)
        t.input_array("a1", array1)
        # load array attributes into argument registers
        t.input_scalar("a2", len(array0))
        t.input_scalar("a3", 1)
        t.input_scalar("a4", 1)
        # call the `dot` function
        t.call("dot")
        # check the return value
        t.execute(code=75)

    def test_null_stride_1(self):
        t = AssemblyTest(self, "dot.s")
        # create arrays in the data section
        array0 = t.array([1, 2])
        array1 = t.array([1, 4])
        # load array addresses into argument registers
        t.input_array("a0", array0)
        t.input_array("a1", array1)
        # load array attributes into argument registers
        t.input_scalar("a2", len(array0))
        t.input_scalar("a3", 0)
        t.input_scalar("a4", 1)
        # call the `dot` function
        t.call("dot")
        # check the return value
        t.execute(code=76)
    
    def test_null_stride_2(self):
        t = AssemblyTest(self, "dot.s")
        # create arrays in the data section
        array0 = t.array([1, 2])
        array1 = t.array([2, 3])
        # load array addresses into argument registers
        t.input_array("a0", array0)
        t.input_array("a1", array1)
        # load array attributes into argument registers
        t.input_scalar("a2", len(array0))
        t.input_scalar("a3", 1)
        t.input_scalar("a4", 0)
        # call the `dot` function
        t.call("dot")
        # check the return value
        t.execute(code=76)

    
    @classmethod
    def tearDownClass(cls):
        print_coverage("dot.s", verbose=False)


class TestMatmul(TestCase):

    def do_matmul(self, m0, m0_rows, m0_cols, m1, m1_rows, m1_cols, result, code=0):
        t = AssemblyTest(self, "matmul.s")
        # we need to include (aka import) the dot.s file since it is used by matmul.s
        t.include("dot.s")

        # create arrays for the arguments and to store the result
        array0 = t.array(m0)
        array1 = t.array(m1)
        array_out = t.array([0] * len(result))

        # load address of input matrices and set their dimensions
        t.input_array("a0", array0)
        t.input_array("a3", array1)
        t.input_scalar("a1", m0_rows)
        t.input_scalar("a2", m0_cols)
        t.input_scalar("a4", m1_rows)
        t.input_scalar("a5", m1_cols)
        # load address of output array
        t.input_array("a6", array_out)

        # call the matmul function
        t.call("matmul")

        # check the content of the output array
        print(array_out)
        if m0_rows>=1 and m0_cols<=1 and m1_rows<=1 and m1_cols<=1:
            t.check_array(array_out, result)

        # generate the assembly file and run it through venus, we expect the simulation to exit with code `code`
        t.execute(code=code)

    def test_simple(self):
        self.do_matmul(
            [1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 3,
            [1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 3,
            [30, 36, 42, 66, 81, 96, 102, 126, 150]
        )
    def test_nonsense_m0_row(self):
        self.do_matmul(
            [1, 2, 3, 4], 0, 3, 
            [1, 2, 3, 4], 2, 2,
            [], 72
        )
    def test_nonsense_m0_col(self):
        self.do_matmul(
            [1, 2, 3, 4], 2, 0, 
            [1, 2, 3, 4], 2, 2,
            [], 72
        )
    def test_nonsense_m1_row(self):
        self.do_matmul(
            [1, 2, 3, 4], 1, 4, 
            [1, 2, 3, 4], 0, 2,
            [], 73
        )
    def test_nonsense_m1_col(self):
        self.do_matmul(
            [1, 2, 3, 4], 1, 4, 
            [1, 2, 3, 4], 2, 0,
            [], 73
        )
    def test_mismatch(self):
        self.do_matmul(
            [1, 2, 3, 4], 1, 4, 
            [1, 2, 3, 4], 2, 2,
            [], 74
        )

    def test_zero(self):
        self.do_matmul(
            [0, 0, 0, 0], 2, 2, 
            [1, 2, 3, 4], 2, 2,
            [0, 0, 0, 0]
        )

    def test_identity(self):
        self.do_matmul(
            [1, 0, 1, 0], 2, 2, 
            [1, 2, 3, 4], 2, 2,
            [1, 2, 3, 4]
        )
    def test_rando(self):
        self.do_matmul(
            [2, 1, 4, 0, 1, 1], 2, 3, 
            [6, 3, -1, 0, 1, 1, 0, 4, -2, 5, 0, 2], 3, 4,
            [5, 27, -2, 12, -1, 6, 0, 6]
        )

    @classmethod
    def tearDownClass(cls):
        print_coverage("matmul.s", verbose=False)


class TestReadMatrix(TestCase):

    def do_read_matrix(self, fail='', code=0, file="inputs/test_read_matrix/test_input.bin", row=3, col=3, a_0=[1, 2, 3, 4, 5, 6, 7, 8, 9]):
        t = AssemblyTest(self, "read_matrix.s")
        # load address to the name of the input file into register a0
        t.input_read_filename("a0", file)

        # allocate space to hold the rows and cols output parameters
        rows = t.array([-1])
        cols = t.array([-1])

        # load the addresses to the output parameters into the argument registers
        t.input_array("a1", rows)
        t.input_array("a2", cols)

        # call the read_matrix function
        t.call("read_matrix")

        # check the output from the function
        t.check_array(rows, [row])
        t.check_array(cols, [col])
        t.check_array_pointer("a0", a_0)

        # generate assembly and run it through venus
        t.execute(fail=fail, code=code)

    def test_simple(self):
        self.do_read_matrix()
    def test_fail_malloc(self):
        self.do_read_matrix(fail='malloc', code=88)
    def test_fail_fopen(self):
        self.do_read_matrix(fail='fopen', code=90)
    def test_ail_fread(self):
        self.do_read_matrix(fail='fread', code=91)
    def test_fail_fclose(self):
        self.do_read_matrix(fail='fclose', code=92)
    def test_basic(self):
        self.do_read_matrix(file="inputs/test_read_matrix/test_basic.bin", row=1, col=2, a_0=[1, 2])
    @classmethod
    def tearDownClass(cls):
        print_coverage("read_matrix.s", verbose=False)


class TestWriteMatrix(TestCase):
    def do_write_matrix(self, fail='', code=0):
        t = AssemblyTest(self, "write_matrix.s")
        outfile = "outputs/test_write_matrix/student.bin"
        # load output file name into a0 register
        t.input_write_filename("a0", outfile)
        # load input array and other arguments
        matrix = t.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
        row = 3
        col = 3
        t.input_array("a1", matrix)
        t.input_scalar("a2", row)
        t.input_scalar("a3", col)
        # call `write_matrix` function
        t.call("write_matrix")
        # generate assembly and run it through venus
        t.execute(fail=fail, code=code)
        # compare the output file against the reference
        if code == 0:
            t.check_file_output(outfile, "outputs/test_write_matrix/reference.bin")
       
    def test_simple(self):
        self.do_write_matrix()

    def test_fail_malloc(self):
        self.do_write_matrix(fail='malloc', code=88)
    def test_fail_fopen(self):
        self.do_write_matrix(fail='fopen', code=93)
    def test_fail_fwrite(self):
        self.do_write_matrix(fail='fwrite', code=94)
    def test_fail_fclose(self):
        self.do_write_matrix(fail='fclose', code=95)

    @classmethod
    def tearDownClass(cls):
        print_coverage("write_matrix.s", verbose=False)


class TestClassify(TestCase):

    def make_test(self):
        t = AssemblyTest(self, "classify.s")
        t.include("argmax.s")
        t.include("dot.s")
        t.include("matmul.s")
        t.include("read_matrix.s")
        t.include("relu.s")
        t.include("write_matrix.s")
        return t

    
    #ref_file = outputs/test_classify/simple{0}/bin/{output0}.bin
    def do_classify(self, classification, input_i, simple_i, code=0, fail='', p=0):
        #input_i is an int from [0, 1, 2]
        #simple_i is an int from [0, 1, 2]

        t = self.make_test()
        out_file = f"outputs/test_classify/OUTPUTS/simple{simple_i}_output{input_i}.bin"

        ref_file = f"outputs/test_classify/simple{simple_i}/bin/output{input_i}.bin"

        args = [f"inputs/simple{simple_i}/bin/m0.bin", f"inputs/simple{simple_i}/bin/m1.bin",
                f"inputs/simple{simple_i}/bin/inputs/input{input_i}.bin", out_file]

        t.input_scalar("a2", p)
        # call classify function
        t.call("classify")
        # generate assembly and pass program arguments directly to venus
        t.execute(args=args, code=code, fail=fail)

        # compare the output file and
        t.check_file_output(out_file, ref_file)
        
        # compare the classification output with `check_stdout`
        if code==0:
            t.check_stdout(classification)

    def test_simple0(self): 
        for i in [0, 1, 2]:
            self.do_classify(classification="2", input_i=i, simple_i=0)

    def test_simple1_input0(self): 
        self.do_classify(classification="1", input_i=0, simple_i=1)
    
    def test_simple1_input1(self): 
        self.do_classify(classification="4", input_i=1, simple_i=1)

    def test_simple1_input2(self): 
        self.do_classify(classification="1", input_i=2, simple_i=1)

    def test_simple2_input0(self): 
        self.do_classify(classification="7", input_i=0, simple_i=2)
    
    def test_simple2_input1(self): 
        self.do_classify(classification="4", input_i=1, simple_i=2)
    
    def test_fail_malloc(self): 
        self.do_classify(classification="4", input_i=1, simple_i=2, fail='malloc', code=88, p=1)
    
    def do_mnist(self, num, classification, p=0):
        args = ["inputs/mnist/bin/m0.bin", "inputs/mnist/bin/m1.bin", f"inputs/mnist/bin/inputs/mnist_input{num}.bin",
                "outputs/test_mnist_main/student_mnist_outputs.bin"]
        t = self.make_test()
        t.input_scalar("a2", p)
        # call classify function
        t.call("classify")
        # generate assembly and pass program arguments directly to venus
        t.execute(args=args)
        
        # compare the classification output with `check_stdout`
        t.check_stdout(classification)

    def test_mnist_1(self):
        self.do_mnist(num=1, classification="9")
    def test_mnist_2(self):
        self.do_mnist(num=2, classification="9")
    def test_mnist_3(self):
        self.do_mnist(num=3, classification="2")
    def test_mnist_4(self):
        self.do_mnist(num=4, classification="9")
    def test_mnist_5(self):
        self.do_mnist(num=5, classification="4")
    def test_mnist_6(self):
        self.do_mnist(num=6, classification="4")
    def test_mnist_7(self):
        self.do_mnist(num=7, classification="8")
    def test_mnist_8(self):
        self.do_mnist(num=8, classification="7")
    def test_mnist_0(self):
        self.do_mnist(num=0, classification="6")

    @classmethod
    def tearDownClass(cls):
        print_coverage("classify.s", verbose=False)


class TestMain(TestCase):

    def run_main(self, inputs, output_id, label):
        args = [f"{inputs}/m0.bin", f"{inputs}/m1.bin", f"{inputs}/inputs/input0.bin",
                f"outputs/test_basic_main/student{output_id}.bin"]
        reference = f"outputs/test_basic_main/reference{output_id}.bin"
        t = AssemblyTest(self, "main.s", no_utils=True)
        t.call("main")
        t.execute(args=args, verbose=False)
        t.check_stdout(label)
        t.check_file_output(args[-1], reference)

    def test0(self):
        self.run_main("inputs/simple0/bin", "0", "2")

    def test1(self):
        self.run_main("inputs/simple1/bin", "1", "1")
    

    