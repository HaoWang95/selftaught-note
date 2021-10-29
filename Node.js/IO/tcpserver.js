const net = require('net');


const HOSTNAME = 'localhost';
const port = 8888;

const createTcpServer = (host, port) => {
    net.createServer((socket) => {
        socket.on('connect', () => {
            console.log(`Client connected from ${socket.remoteAddress}`);
        });
        socket.on("data", (data) => {
            socket.write("Welcome to the server");
            console.log(`${data.toString()}`);
        });
        socket.on('error', (err) => {
            console.error(`err at createTcpServer -> ${err}`);
            return err;
        });
        socket.on('close', () => {
            console.info(`Client from ${socket.remoteAddress}:${socket.remotePort} disconnected`);
        });
    }).listen(port, host, () => {
        console.log(`Server created at ${host}:${port}, waiting for connection...`)
    });
}

createTcpServer(HOSTNAME, port);