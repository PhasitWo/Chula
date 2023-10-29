import argparse
parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
parser.add_argument('integers', metavar='N', type=int, nargs='+')
args = parser.parse_args()
NUMBER_OF_CUSTOMERS = 5
NUMBER_OF_RESOURCES = 3

available = [0 for _ in range(NUMBER_OF_RESOURCES)]
maximum = [[0 for _ in range(NUMBER_OF_RESOURCES)] for _ in range(NUMBER_OF_CUSTOMERS)]
allocation = [[0 for _ in range(NUMBER_OF_RESOURCES)] for _ in range(NUMBER_OF_CUSTOMERS)]
need = [[0 for _ in range(NUMBER_OF_RESOURCES)] for _ in range(NUMBER_OF_CUSTOMERS)]

def request_resources(customer_num:int, request:list[int]) -> int:
    global need, available, allocation
    for x in range(NUMBER_OF_RESOURCES):
        if request[x] > need[customer_num][x]:
            print("Invalid request : req > need")
            return -1
        if request[x] > available[x]:
            print("Invalid request : not enough resource")
            return -1
    # save state (deep copy)
    old_available = [item for item in available]
    old_allocation = [row[:] for row in allocation]
    old_need = [row[:] for row in need]
    # pretend to allocate requested resources
    for y in range(NUMBER_OF_RESOURCES):
        available[y] -= request[y]
        allocation[customer_num][y] += request[y]
        need[customer_num][y] -= request[y]
    # safety algorithm
    # step 1
    work = [item for item in available]
    finish = [False for _ in range(NUMBER_OF_CUSTOMERS)]
    # step 2
    while(True):
        i = find(finish, work, need)
        if i == -1: # no such i that can get resources
            break
        # step 3
        for j in range(NUMBER_OF_RESOURCES):
            work[j] += allocation[i][j]
        finish[i] = True
        print(i, "finished")
    
    # step 4
    all_finish = True
    for i in range(NUMBER_OF_CUSTOMERS):
        if finish[i] == False:
            all_finish = False
            break
    if all_finish:
        print("request accepted: safe")
        return 0
    else:
        print("request denied: unsafe")
        # restore state
        available = old_available
        allocation = old_allocation
        need = old_need
        return -1

def release_resources(customer_num:int, request:list[int]) -> None:
    for i in range(NUMBER_OF_RESOURCES):
        if allocation[customer_num][i] - request[i] < 0:
            print("invalid request")
            return
    for x in range(NUMBER_OF_RESOURCES):
        allocation[customer_num][x] -= request[x]
        need[customer_num][x] += request[x]
        available[x] += request[x]


def find(finish:list[bool], work, need):
    for i in range(NUMBER_OF_CUSTOMERS):
        if finish[i] == False:
            need_lessthan_work = True
            for j in range(NUMBER_OF_RESOURCES):
                if need[i][j] > work[j]:
                    need_lessthan_work = False
                    break
            if need_lessthan_work:
                return i
    return -1

def display_all_data():
    print("available:")
    print(available)
    print("maximum:")
    for cus in maximum:
        print(cus)
    print("allocation:")
    for cus in allocation:
        print(cus)
    print("need:")
    for cus in need:
        print(cus)
    

if __name__ == "__main__":
    allocation =[
        [0,1,0],
        [2,0,0],
        [3,0,2],
        [2,1,1],
        [0,0,2],
    ]
    # read file
    with open("OperSys/6.DeadLock/test.txt", "r") as file:
        id_ = 0
        for line in file:
            inputs = map(int ,line.strip().split(","))
            for res_id, res_value in enumerate(inputs):
                maximum[id_][res_id] = res_value
                need[id_][res_id] = res_value - allocation[id_][res_id]
            id_ += 1
    available = args.integers # init available
    # receive user command
    user_command = input("enter command: ")
    while(user_command != "quit"):
        if user_command == "*":
            display_all_data()
            user_command = input("enter command: ")
            continue
        user_inputs = user_command.strip().split(" ")
        request = list(map(int, user_inputs[2:]))
        cust_id = int(user_inputs[1])
        if user_inputs[0].upper() == "RQ":
            request_resources(cust_id, request)
        elif user_inputs[0].upper() == "RL":
            release_resources(cust_id, request)
        else:
            print("Invalid Command")
        user_command = input("enter command: ")

        