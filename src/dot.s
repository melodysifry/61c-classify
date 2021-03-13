.globl dot

.text
# =======================================================
# FUNCTION: Dot product of 2 int vectors
# Arguments:
#   a0 (int*) is the pointer to the start of v0
#   a1 (int*) is the pointer to the start of v1
#   a2 (int)  is the length of the vectors
#   a3 (int)  is the stride of v0
#   a4 (int)  is the stride of v1
# Returns:
#   a0 (int)  is the dot product of v0 and v1
# Exceptions:
# - If the length of the vector is less than 1,
#   this function terminates the program with error code 75.
# - If the stride of either vector is less than 1,
#   this function terminates the program with error code 76.
# =======================================================
dot:
    addi t1, x0, 1
    blt a2, t1, error_75
    blt a3, t1, error_76
    blt a4, t1, error_76
    # Prologue
    addi sp, sp, -36
    sw s2, 0(sp) # num of elems
    sw s3, 4(sp) #
    sw s4, 8(sp)
    sw s5, 12(sp)
    sw s6, 16(sp)
    sw s7, 20(sp)
    sw s8, 24(sp)
    sw s9, 28(sp)
    sw s10, 32(sp)
    addi s2, a2, 0 #s2 is number of elements in array
    addi s3, a0, 0 #s3 is pointer to start of v0
    addi s4, a1, 0 #s4 is pointer to start of v1
    addi s5, x0, 0 #s5 is our counter, starts at 0
    addi s6, a3, 0 #make s6 stride of v0
    
    li t1, 4

    mul s6, s6, t1 #now s6 is actual amount we need to increment addresses by
    addi s7, a4, 0 #make s7 stride of v1
    
    mul s7, s7, t1 #now s7 is actual amount we need to increment addresses by
    addi s10, x0, 0 #s10 will be the dot product
    j loop_start


loop_start:
    beq s5, s2, loop_end
    lw s8, 0(s3) #s8 holds val at beginning at s3 = v0
    lw s9, 0(s4) #s9 holds val at beginning at s4 = v1
    mul t0, s8, s9 #t0 is product of these vals
    add s10, s10, t0 #add to dot product
    addi s5, s5, 1
    add s3, s3, s6
    add s4, s4, s7
    j loop_start

loop_end:
    addi a0, s10, 0
    # Epilogue
    lw s2, 0(sp) # num of elems
    lw s3, 4(sp) #
    lw s4, 8(sp)
    lw s5, 12(sp)
    lw s6, 16(sp)
    lw s7, 20(sp)
    lw s8, 24(sp)
    lw s9, 28(sp)
    lw s10, 32(sp)
    addi sp, sp, 36
    ret

error_75:
    addi a1, x0, 75
    jal exit2
    
error_76:
    addi a1, x0, 76
    jal exit2