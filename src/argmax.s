.globl argmax

.text
# =================================================================
# FUNCTION: Given a int vector, return the index of the largest
#	element. If there are multiple, return the one
#	with the smallest index.
# Arguments:
# 	a0 (int*) is the pointer to the start of the vector
#	a1 (int)  is the # of elements in the vector
# Returns:
#	a0 (int)  is the first index of the largest element
# Exceptions:
# - If the length of the vector is less than 1,
#   this function terminates the program with error code 77.
# =================================================================
argmax:
    addi t1, x0, 1
    blt a1, t1, exit_77
    # Prologue
    addi sp, sp, -24
    sw s2, 0(sp)
    sw s3, 4(sp) 
    sw s4, 8(sp)
    sw s5, 12(sp)
    sw s6, 16(sp)
    sw s7, 20(sp)
    addi s2, a1, 0 #s2 is number of elements in array
    addi s3, a0, 0 #s3 is pointer to start of array
    addi s4, x0, 0 #s4 is our counter, starts at 0
    addi s6, x0, 0 #s6 is the index of the current max value
    lw s7, 0(s3) #s7 is the maximum value
    j loop_start 


loop_start:
    beq s2, s4, loop_end #end if counter s4 = number of elems s2
    lw s5, 0(s3) #s5 is the val of first thing in array
    #if s5 is more than s7, go to loop_continue
    blt s7, s5, loop_continue
    #increment pointer and counter
    addi s4, s4, 1 #increment count
    addi s3, s3, 4 
    j loop_start 

loop_continue:
    #if s5 is new max, update index s6 and max val s7
    addi s7, s5, 0 #update max value
    addi s6, s4, 0 #make index s6 be current count s4
    j loop_start 

loop_end:
    addi a0, s6, 0
    # Epilogue
    lw s2, 0(sp)
    lw s3, 4(sp) 
    lw s4, 8(sp)
    lw s5, 12(sp)
    lw s6, 16(sp)
    lw s7, 20(sp)
    addi sp, sp, 24
    ret
    
exit_77:
    addi a1, x0, 77
    jal exit2