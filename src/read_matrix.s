.globl read_matrix

.text
# ==============================================================================
# FUNCTION: Allocates memory and reads in a binary file as a matrix of integers
#
# FILE FORMAT:
#   The first 8 bytes are two 4 byte ints representing the # of rows and columns
#   in the matrix. Every 4 bytes afterwards is an element of the matrix in
#   row-major order.
# Arguments:
#   a0 (char*) is the pointer to string representing the filename
#   a1 (int*)  is a pointer to an integer, we will set it to the number of rows
#   a2 (int*)  is a pointer to an integer, we will set it to the number of columns
# Returns:
#   a0 (int*)  is the pointer to the matrix in memory
# Exceptions:
# - If malloc returns an error,
#   this function terminates the program with error code 88.
# - If you receive an fopen error or eof, 
#   this function terminates the program with error code 90.
# - If you receive an fread error or eof,
#   this function terminates the program with error code 91.
# - If you receive an fclose error or eof,
#   this function terminates the program with error code 92.
# ==============================================================================
read_matrix:

    # Prologue
    addi sp, sp, -32 #for now
    sw s2, 0(sp)
    sw s3, 4(sp)
    sw s4, 8(sp)
    sw s5, 12(sp)
    sw s6, 16(sp)
    sw s7, 20(sp)
    sw s8, 24(sp)
    sw ra, 28(sp)

    # OPEN FILE
    addi s7, a1, 0          # s7 now points to rows
    addi s8, a2, 0          # s8 now points to cols
    
    addi s2, a0, 0          # s2 is pointer to filename string
    addi a1, s2, 0          # set a1 to pointer to string for fopen
    addi a2, x0, 0          # set a2 to 0 = set permission to read only for fopen
    jal ra, fopen           # call fopen
    addi t0, x0, -1
    beq a0, t0, fopen_error 
    addi s3, a0, 0          # now s3 is is the file descriptor returned from fopen

    # READ ROW AND COL FROM FILE

    addi a0, x0, 8          #make a0 = 8 for malloc
    jal ra, malloc          #malloc 8 bytes for row and col ints
    beq a0, x0, malloc_error 
    add a2, x0, a0          #make a2 point to the allocated space
    addi s4, a2, 0          #s4 now points to the number of rows, 4 over is number of cols

    addi a3, x0, 8          #make a3 = 8 for fread
    addi a1, s3, 0          #make a1 the file descriptor
    jal ra, fread
    addi t0, x0, 8
    bne a0, t0, fread_error

    # READ REST OF STUFF FROM FILE
    
    lw t0, 0(s4)            #t0 is num rows
    lw t1, 4(s4)            #t1 is num cols
    mul a3, t0, t1          #a3 is rows x cols
    addi t0, x0, 4
    mul a3, a3, t0          #a3 is now number of bytes to read for fread
    
    addi a0, a3, 0          #a0 is now number of bytes to allocate for malloc
    addi s5, a0, 0          #save the number of bytes in s5 for error check
    jal ra, malloc
    beq a0, x0, malloc_error
    add a2, x0, a0          #we allocated space for our matrix, and now a2 points to that space for fread
    addi s6, a2, 0          #save address of matrix in s6
    addi a1, s3, 0          #make a1 the file descriptor
    jal fread
    bne a0, s5, fread_error

    # FCLOSE NOW
    addi a1, s3, 0
    jal ra, fclose
    bne a0, x0 fclose_error

    # SET UP RETURN PARAMETERS
    addi a0, s6, 0            #make a0 point to matrix in memory
    lw t0, 0(s4)
    sw t0, 0(s7)
    lw t1, 4(s4)
    sw t1, 0(s8)

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

malloc_error:
    addi a1, x0, 88
    jal exit2
fopen_error:
    addi a1, x0, 90
    jal exit2
fread_error:
    addi a1, x0, 91
    jal exit2
fclose_error:
    addi a1, x0, 92
    jal exit2
