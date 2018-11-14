# Generate key pairs:
##(EC)DSA
        openssl genrsa -des3 -out myCA.key 2048
	openssl dsaparam -genkey 1024 -out dsakey.pem
	openssl ecparam -genkey -out eckey.pem -name prime256v1
########openssl ecparam -list_curves
##(EC)DH
	openssl dhparam -out dhparam.pem 1024
	openssl genpkey -paramfile dhparam.pem -out dhkey.pem
	openssl ecparam -out ecparam.pem -name prime256v1
	openssl genpkey -paramfile ecparam.pem -out ecdhkey.pem

# Root CA - self signed cert with corresponding private key
openssl req \
	-x509 -nodes -days 365 -sha256 \
	-subj '/C=DE/ST=Bavaria/L=Munich/CN=www.mitm@mixed-mode.com/O=bad/OU=ass' \
	-newkey rsa:2048 -keyout RSA2048_private.pem \
	-out RSA2048_cert.crt

# Create a CSR
    openssl req -out CSR.csr -key privateKey.key -new
    openssl req -out CSR.csr -new -newkey rsa:2048 -nodes -keyout privateKey.key

# Sign the CSR with the CA
    openssl x509 -req -days 360 -in CSR.csr -CA ca.cert.pem -CAkey ca.key.pem -CAcreateserial -out CRT.crt -sha256

# Set start- and enddate with ca command
    openssl ca -config /etc/ssl/openssl.cnf -policy policy_anything -outdir . -out clientcert.pem -startdate 120815080000Z -enddate 120815090000Z -cert RSA2048_cert.crt -keyfile RSA2048_private.pem -infiles CSR.csr

# Checks 
    openssl req -text -noout -verify -in CSR.csr
    openssl rsa -in privateKey.key -check
    openssl x509 -in certificate.crt -text -noout

# Utils
## Extract key
    openssl pkey -in foo.pem -out foo-key.pem
## Extract all certs
    openssl crl2pkcs7 -nocrl -certfile foo.pem |
    openssl pkcs7 -print_certs -out foo-certs.pem
## Extract the textually first cert as DER
    openssl x509 -in foo.pem -outform DER -out first-cert.der
## Generate public key
    openssl rsa -in mykey.pem -pubout
## Check cert
    openssl x509 -text -noout -in mycert.pem
## Remove passphrase from key
    openssl rsa -in privateKey.pem -out newPrivateKey.pem

# Important flags
    -nocert                    Don't use any certificates (Anon-DH)
    -comp                      Use SSL/TLS-level compression
