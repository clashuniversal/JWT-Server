#generate RSA key
ssh-keygen -t rsa -b 1024 -m PEM -f jwtRS256.key
# use empty passphrase 
openssl rsa -in jwtRS256.key -pubout -outform PEM -out jwtRS256.key.pub