.globl relu

.text
# ==============================================================================
# FUNCTION: Performs an inplace element-wise ReLU on an array of ints
# Arguments:
# 	a0 (int*) is the pointer to the array
#	a1 (int)  is the # of elements in the array
# Returns:
#	None
# Exceptions:
# - If the length of the vector is less than 1,
#   this function terminates the program with error code 78.
# ==============================================================================
relu:
    addi t1, x0, 1
    blt a1, t1, exit_if_empty
    # Prologue
    addi sp, sp, -16 
    sw s2, 0(sp)
    sw s3, 4(sp) 
    sw s4, 8(sp)
    sw s5, 12(sp)
    addi s2, a1, 0 #s2 is number of elements in array
    addi s3, a0, 0 #s3 is pointer to start of array
    addi s4, x0, 0 #s4 is our counter, starts at 0
    j loop_start

loop_start:
    beq s2, s4, loop_end #end if counter s4 = number of elems s2
    lw s5, 0(s3) #s5 is the val of first thing in array
    #if s5 is negative, go to loop_continue
    blt s5, x0, loop_continue
    #if s5 is not negative, increment pointer and counter
    addi s4, s4, 1 #increment count
    addi s3, s3, 4 #moving pointer, THIS NUMBER IS PROB WRONG BC IDK HOW MANY BITS 
    j loop_start
 
loop_continue:
    #if the element s5 is pointing to is negative, make it zero
    addi s5, x0, 0
    sw s5, 0(s3) 
    j loop_start
    
loop_end:
    # Epilogue
    lw s2, 0(sp)
    lw s3, 4(sp)
    lw s4, 8(sp)
    lw s5, 12(sp)
    addi sp, sp, 16
	ret

exit_if_empty: 
   addi a1, x0, 78
   jal exit2