from server import server, views

server.run(
    debug = True,
    host = '0.0.0.0',
    threaded = True
)