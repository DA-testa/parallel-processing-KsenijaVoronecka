# python3 main.py
# Ksenija Voronecka RDCP0

def parallel_processing(n, m, data):
    output = []
    threads = [0] * n
    
    time = 0
    mask = False
    while True:
        
        for i in range(n):
            if threads[i] == 0:

                if len(data) == 0:
                    mask = True
                    break

                threads[i] = data[0]
                data.pop(0)
                output.append([i, time])
            threads[i] -= 1
        
        if mask == True:
            break

        time += 1


    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count

    print("Enter a thread count and job count: ")
    count = list(map(int, input().split()))
    n = count[0]
    m = count[1]

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    print("Enter data: ")
    data = list(map(int, input().split()))

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for i, j in result:
        print(i, j)



if __name__ == "__main__":
    main()
