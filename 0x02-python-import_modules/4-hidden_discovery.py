#!/usr/bin/python3
if __name__ == "__main__":
    """print all hidden directories"""
    import hidden_4
    for i in dir(hidden_4):
        if not i.startswith('__') and not i.endswith('__'):
            print(i)
