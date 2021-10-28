const net = require('net');

const HOSTNAME = 'localhost';
const PORT = 8888;

const clientSocket = (port, host) => {
    const client = net.connect(port, host);
    client.on('connect', () => {
        console.info('Connect to server completed, will keep the connection...');
        client.write(`Hi, this is client from ${client.address().address}:${client.address().port}`);
    });
    client.on('data', (data) => {
        console.info(`${client.remoteAddress}:${client.remotePort} -> ${data}`);
    });
    client.on('error', (err) => {
        console.error(`err -> ${err}`);
        console.error('For some reason, the connection is lost');
        client.destroy();
    })
}

clientSocket(PORT, HOSTNAME);