from setup import setup
# add zig as package
setup()

from zig import Zig


# all default
app = Zig()



if __name__ == "__main__":
    app.run()
