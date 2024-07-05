# Self-Signed Certificate Generation

This guide explains how to create a self-signed SSL certificate using OpenSSL.

## Prerequisites

Ensure you have OpenSSL installed on your system. You can download and install it from the [OpenSSL official website](https://www.openssl.org/).

### Installation

#### On Windows
1. Download the installer from [OpenSSL for Windows](https://slproweb.com/products/Win32OpenSSL.html).
2. Run the installer and follow the instructions.

# Generating a Self-Signed Certificate

Create a configuration file named filename.cnf with the following content:
[req]
default_bits        = 2048
distinguished_name  = req_distinguished_name
x509_extensions     = v3_req
prompt              = no

[req_distinguished_name]
C                   = US
ST                  = California
L                   = San Francisco
O                   = MyCompany
OU                  = MyDivision
CN                  = server ip/domain name

[v3_req]
keyUsage = keyEncipherment, dataEncipherment
extendedKeyUsage = serverAuth
subjectAltName = @alt_names

[alt_names]
IP.1 = server ip/domain name

#Generate a private key using command: "openssl genpkey -algorithm RSA -out keyname.key"

Generate the self-signed certificate using private key and the configuration file: execute this command "openssl req -x509 -new -nodes -key keyname.key -sha256 -days 365 -out crtname.crt -config filename.cnf
"



****note: Place the Self-Signed Certificate file on the same directory of your coding file
