const net = require('net');
const { hostname } = require('os');

const HOSTNAME = 'localhost';
const port = 8888;

const createTcpServer = (host, port) => {
    net.createServer((socket) => {
        console.log(`Client connected from ${socket.remoteAddress}`);
        socket.on("data", (data) => {
            socket.write("Welcome");
            console.log(`${data.toString()}`);
        });
        socket.on('error', (err) => {
            console.error(`err at createTcpServer -> ${err}`);
            return err;
        });
        socket.on('end', () => {
            console.info('Client disconnected.')
        })
    }).listen(port, host, () => {
        console.log(`Server created at ${host}:${port}, waiting for connection...`)
    });
}

createTcpServer(HOSTNAME, port);