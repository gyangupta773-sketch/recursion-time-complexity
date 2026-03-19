def prints(n):
    if n <= 0:
        return
    
    print("Avenger's Assemble")
    prints(n // 2)
    prints(n // 2)

#Call the function
prints(8)