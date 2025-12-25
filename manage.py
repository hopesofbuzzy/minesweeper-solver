from src.model.field import Field
import logging

logging.basicConfig(level=logging.DEBUG)


def main():
    field = Field(9, 9)
    field.open(5, 0)
    print(field.show(real=True))
    print(field)


if __name__ == "__main__":
    main()
