const net = require('net');

const HOSTNAME = 'localhost';
const PORT = 8888;

const clientSocket = (port, host) => {
    const client = net.connect(port, host);
    client.on('connect', () => {
        console.info('Connect to server completed, will keep the connection...');
        client.write('Connection from client.');
    });
}

clientSocket(PORT, HOSTNAME);