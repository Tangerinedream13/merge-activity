def say_hello(name: str) -> None:
    print(f"Hello {name}!")

def say_hello_n(times) -> None:
     for i in range(times):
          print("hello world!")


if __name__ == "__main__":
     say_hello_n(3)
     say_hello("Walter")
     say_hello("Ruth")
     say_hello("Larry")
     say_hello("Helen")
