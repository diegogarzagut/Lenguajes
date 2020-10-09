main() 
    # Menu
    puts "Welcome"
    puts "Menu"
    puts "    1. Matrix Multiplication"
    puts "    2. Matrix Addition"
    puts "Select an option by typing the 1 or 2:"
    choice = gets

    # Input Values
    puts "Enter Matrix A 1st dimension size"
    dimA1 = gets
    while (dimA1 > 5) # las expresiones logicas pueden ser mas de 1 comparacion?
        puts "Enter Matrix A 1st dimension size"
        dimA1 = gets
    end

    puts "Enter Matrix A 2nd dimension size"
    dimA2 = gets
    while (dimA2 > 5)
        puts "Enter Matrix A 2nd dimension size"
        dimA2 = gets
    end

    puts "Enter Matrix B 1st dimension size"
    dimB1 = gets
    while (dimB1 > 5) 
        puts "Enter Matrix B 1st dimension size"
        dimA1 = gets
    end

    puts "Enter Matrix B 2nd dimension size"
    dimB2 = gets
    while (dimB2 > 5)
        puts "Enter Matrix B 2nd dimension size"
        dimB2 = gets
    end

    # Matrix variable declaration **** DUDA, se vale declararla así?
    matA[dimA1][dimA2]
	matB[dimB1][dimB2]

    # Multiplication Validation **** DUDA -> el if se escribe true y false?
    if (dimA2 == dimB1) 
        puts "Valid Matrix Multiplication"
    end
    if (dimA2 != dimB1)
        puts "Invalid Matrix Multiplication"
    end

    # Sum Validation ****** DUDA -> se vale usar ANDs? o los separo?

    if (dimA1 == dimB1 && dimA2 == dimB2)
        puts "Valid Matrix Multiplication"
    end
    if (dimA1 != dimB1 && dimA2 == dimB2)
        puts "Valid Matrix Multiplication"
    end

    # Fill Matrix A 
    puts "Fill Matrix A values: "
    while (iA < dimA1)
        while (jA < dimA2)
            valueA = gets
            matA[i][j]=valueA
            jA=jA+1
        end
        iA=iA+1
    end
    # Fill Matrix B
    puts "Fill Matrix B values: "
    while (iB < dimB1)
        while (jB < dimB2)
            valueB = gets 
            matB[i][j]=valueB
            jB=jB+1
        end
        iB=iB+1
    end

    # Menu Action

    if (choice == 1)
        # validation
        iM1=0
        iM2=0
        iM3=0
        if (dimA2 == dimB1) 
            puts "Valid Matrix Multiplication"
            matC[dimA1][dimB2]
            while (iM1 < (dimA1 - 1))
                while (iM2 < (dimB2 - 1))
                    while (iM3 < dimB1)
                        matC[iM1][iM2]= matC[iM1][iM2] + (matA[iM1][iM3] * matB[iM3][iM2])
                    iM3 = iM3 + 1
                    end
                iM2 = iM2 + 1
                end
            iM1 = iM1 + 1
            end
        end
        if (dimA2 != dimB1)
            puts "Invalid Matrix Multiplication"
        end
    end

    if (choice == 2)
        if (dimA1 != dimB1) && (dimA2 != dimB2)
            puts "Invalid Matrix Adittion"
        end
        if (dimA1 == dimB1) && (dimA2 == dimB2)
            while (iA1 < dimA1)
                while (iA2 < dimA2)
                    matC[iM1][iM2]= matC[iM1][iM2] + (matA[iM1][iM2] * matB[iM1][iM2])
                iA2 = iA2 + 1
                end
            iA1 = iA1 + 1
            end
        end
    end
end 
