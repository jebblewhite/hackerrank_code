from dataclasses import dataclass

@dataclass
class ListComp:
    x : int
    y : int
    z : int
    n : int

    def list_permuations(self) -> list(list(int)):
        # method that creates a list from x,y,z and returns a list of all permutations of 0-x,0-y,0-z in 3D space
        self.perm_list = [[i,j,k] for i in range(self.x+1), for j in range(self.y+1), for k in range(self.z+1)]

    def print_not_n(self) -> None:
        # Another method
        pass

def main() -> None:
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    # Instantiate an object of ListComp
    list_comp = ListComp(x,y,z,n)

    # Call methods on the object
    list_comp.list_permuations()
    list_comp.print_not_n()

if __name__ == "__main__":
    main()
