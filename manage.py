from src.generator import Generator
from src.solver import Solver


def main():
    while True:
        try:
            enter = input(">> ").split(" ")
            match enter[0]:
                case "generate":
                    x = int(enter[1])
                    y = int(enter[2])
                    field = Generator.auto_generate(x, y)
                    Solver.solve(field)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
