.globl matmul

.text
# =======================================================
# FUNCTION: Matrix Multiplication of 2 integer matrices
# 	d = matmul(m0, m1)
# Arguments:
# 	a0 (int*)  is the pointer to the start of m0 
#	a1 (int)   is the # of rows (height) of m0
#	a2 (int)   is the # of columns (width) of m0
#	a3 (int*)  is the pointer to the start of m1
# 	a4 (int)   is the # of rows (height) of m1
#	a5 (int)   is the # of columns (width) of m1
#	a6 (int*)  is the pointer to the the start of d
# Returns:
#	None (void), sets d = matmul(m0, m1)
# Exceptions:
#   Make sure to check in top to bottom order!
#   - If the dimensions of m0 do not make sense,
#     this function terminates the program with exit code 72.
#   - If the dimensions of m1 do not make sense,
#     this function terminates the program with exit code 73.
#   - If the dimensions of m0 and m1 don't match,
#     this function terminates the program with exit code 74.
# =======================================================
matmul:
    # Error checks
    addi t1, x0, 1
    blt a1, t1, exit_72
    blt a2, t1, exit_72
    blt a4, t1, exit_73
    blt a5, t1, exit_73
    bne a2, a4, exit_74
    # Prologue
    addi sp, sp, -36 
    sw s2, 0(sp)
    sw s3, 4(sp)
    sw s4, 8(sp)
    sw s5, 12(sp)
    sw s6, 16(sp)
    sw s7, 20(sp)
    sw s8, 24(sp)
    sw s9, 28(sp)
    sw ra, 32(sp)
    
    addi s2, a1, 0 #is the # of rows (height) of m0
    addi s3, a5, 0 #is the # of columns (width) of m1
    addi s4, a0, 0 #pointer to the start of m0
    addi s5, a3, 0 #pointer to the start of m1
    addi s6, a6, 0 #pointer to the start of d
    addi s7, x0, 0 #outer loop counter 
    addi s9, a2, 0 #number of cols in m0 = number of rows in m1


outer_loop_start:
    beq s7, s2, outer_loop_end
    addi s8, x0, 0 #inner loop counter
    j inner_loop_start


inner_loop_start:
    
    beq s8, s3, inner_loop_end
    beq s7, s2, outer_loop_end

    li t3, 4 
    mul t3, t3, s7
    mul t3 t3, s9 
    add a0, s4, t3 #a0 is the pointer to v0 

    li t0, 4
    mul t0, s8, t0 
    add a1, s5, t0 #a1 is the pointer to v1 

    addi a2, s9, 0 #a2 is the length of the vectors 

    addi a3, x0, 1 #stride of v0 
    add a4, x0, s3 #stride of v1

    jal dot 

    mul t0, s7, s3 #row * max cols 
    add t0, t0, s8 #index of d that we just found == t0 + col
    
    li t2 4 #t2 = 4
    mul t0, t0, t2 #t0 * 4 = t0
    add t1, s6, t0 #s6 -- pointer to start of d -- 

    sw a0, 0(t1)

    addi s8, s8, 1

    j inner_loop_start

inner_loop_end:
    addi s8, x0, 0 
    addi s7, s7, 1
    j outer_loop_start

outer_loop_end:
    # Epilogue
    lw s2, 0(sp)
    lw s3, 4(sp)
    lw s4, 8(sp)
    lw s5, 12(sp)
    lw s6, 16(sp)
    lw s7, 20(sp)
    lw s8, 24(sp)
    lw s9, 28(sp)
    lw ra, 32(sp)
    addi sp, sp, 36
    
    ret


exit_72: 
    addi a1, x0, 72
    jal exit2
exit_73: 
    addi a1, x0, 73
    jal exit2
exit_74: 
    addi a1, x0, 74
    jal exit2