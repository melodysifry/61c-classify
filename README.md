# Folder Layout

```
.
├── inputs (test inputs)
├── outputs (some test outputs)
├── README.md
├── src
│   ├── argmax.s (partA)
│   ├── classify.s (partB)
│   ├── dot.s (partA)
│   ├── main.s (do not modify)
│   ├── matmul.s (partA)
│   ├── read_matrix.s (partB)
│   ├── relu.s (partA)
│   ├── utils.s (do not modify)
│   └── write_matrix.s (partB)
├── tools
│   ├── convert.py (convert matrix files for partB)
│   └── venus.jar (RISC-V simulator)
└── unittests
    ├── assembly (contains outputs from unittests.py)
    ├── framework.py (do not modify)
    └── unittests.py (partA + partB)
```

## Project Description

Wrote RISC-V assembly code necessary to run a simple Artificial Neural Network (ANN) on the Venus RISC-V simulator. Implemented  basic operations such as a vector dot product, matrix-matrix multiplication, the argmax and an activation function. Then combined these basic functions in order to load a pretrained network and execute it to classify handwritten digits from the MNIST benchmark set.

## Credits
UC Berkeley CS61C Project Classify: 
https://cs61c.org/sp21/projects/proj2/
