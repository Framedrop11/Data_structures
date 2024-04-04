def TOH(n, source, auxiliary, target):
        if n == 1:
            print(f"Move disk {n} from rod {source} to rod {target}.")
            return
        TOH(n - 1, source, target, auxiliary)
        print(f"Move disk {n} from rod {source} to rod {target}")
        TOH(n - 1, auxiliary, source, target)

n = int(input("Enter the number of disks : "))
source = input("Enter source name : ")
target = input("Enter destination name : ")
auxiliary = input("Enter auxiliary name : ")
TOH(n,source, target, auxiliary)