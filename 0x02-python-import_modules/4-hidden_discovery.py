#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for names in dir(hidden_4):
        if names[0] != '__' and names[1] != '__':
            print(names)
            