from zig import Zig



# all default
'''
    host: 127.0.0.1
    port: 5000
    asset url: /assets
    asset folder: assets
    template folder: templates
    index file: index_flask

'''

app = Zig()



if __name__ == "__main__":
    app.run()
