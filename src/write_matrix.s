.globl write_matrix

.text
# ==============================================================================
# FUNCTION: Writes a matrix of integers into a binary file
# FILE FORMAT:
#   The first 8 bytes of the file will be two 4 byte ints representing the
#   numbers of rows and columns respectively. Every 4 bytes thereafter is an
#   element of the matrix in row-major order.
# Arguments:
#   a0 (char*) is the pointer to string representing the filename
#   a1 (int*)  is the pointer to the start of the matrix in memory
#   a2 (int)   is the number of rows in the matrix
#   a3 (int)   is the number of columns in the matrix
# Returns:
#   None
# Exceptions:
# - If you receive an fopen error or eof,
#   this function terminates the program with error code 93.
# - If you receive an fwrite error or eof,
#   this function terminates the program with error code 94.
# - If you receive an fclose error or eof,
#   this function terminates the program with error code 95.
# ==============================================================================
write_matrix:

    # Prologue
    addi sp, sp, -32
    sw s2, 0(sp)
    sw s3, 4(sp)
    sw s4, 8(sp)
    sw s5, 12(sp)
    sw s6, 16(sp)
    sw s7, 20(sp)
    sw s8, 24(sp)
    sw ra, 28(sp)

    # save args
    addi s2, a0, 0          # s2 is the pointer to string representing the filename
    addi s3, a1, 0          # s3 = a1 is the pointer to the start of the matrix in memory
    addi s4, a2, 0          # s4 = # rows
    addi s5, a3, 0          # s5 = # cols
    
    # OPEN FILE
    addi a1, s2, 0          # set a1 to pointer to string for fopen
    addi a2, x0, 1          # set a2 to 1 = set permission to write only for fopen
    jal ra, fopen           # call fopen
    addi t0, x0, -1
    beq a0, t0, fopen_error 
    addi s6, a0, 0          # now s6 is is the file descriptor returned from fopen

    # WRITE ROW AND COLS
    # Mallocing space for row and col in memory
    addi a0, x0, 8          # make a0 = 8 for malloc
    jal ra, malloc          # malloc 8 bytes for row and col ints
    beq a0, x0, malloc_error 

    addi a2, a0, 0          # make a2 point to the allocated space
    sw s4, 0(a2)            # a2 now points to row and col in memory
    sw s5, 4(a2)
    addi s8, a2, 0          # save a2 to be freed
    
    addi a1, s6, 0          # a1 is file descriptor
    addi a3, x0, 2          # a3 is 2 elements
    addi a4, x0, 4          # a4 is number of bytes per element
    jal ra, fwrite
    addi t0, x0, 2
    bne a0, t0, fwrite_error 

    addi a0, s8, 0          #a0 points to memory to be freed
    jal ra, free


    # WRITE MATRX
    addi a1, s6, 0          # a1 is file descriptor
    addi a2, s3, 0          # a2 is pointer to matrix
    mul a3, s4, s5          # a3 is number of elements, row*col
    addi s7, a3, 0          # store a3 num elems in s7 to check
    addi a4, x0, 4          # a4 is number of bytes per element
    
    jal ra, fwrite
    bne a0, s7, fwrite_error 
    
    # CLOSE
    addi a1, s6, 0
    jal ra, fclose
    bne a0, x0, fclose_error

    # Epilogue
    lw s2, 0(sp)
    lw s3, 4(sp)
    lw s4, 8(sp)
    lw s5, 12(sp)
    lw s6, 16(sp)
    lw s7, 20(sp)
    lw s8, 24(sp)
    lw ra, 28(sp)
    addi sp, sp, 32
    ret

fopen_error:
    addi a1, x0, 93
    jal exit2
    
fwrite_error:
    addi a1, x0, 94
    jal exit2
    
fclose_error:
    addi a1, x0, 95
    jal exit2

malloc_error:
    addi a1, x0, 88
    jal exit2
