# 1. Generate key pairs:
##(EC)DSA
        openssl genrsa -des3 -out myCA.key 2048
	openssl dsaparam -genkey 1024 -out dsakey.pem
########openssl ecparam -list_curves
##(EC)DH
	openssl dhparam -out dhparam.pem 1024
	openssl genpkey -paramfile dhparam.pem -out dhkey.pem

# 1. Generate ECC key pair:
    openssl ecparam -out privatekey.key -name prime256v1 -genkey 
### or in two steps 
    openssl ecparam -out ecparam.pem -name prime256v1
    openssl genpkey -paramfile ecparam.pem -out ecdhkey.pem
### public key
    openssl ec -in ecprivkey.pem -pubout -out ecpubkey.pem

# 2. Create a CSR
    openssl req -new -key CA_private.pem \
    -subj '/C=DE/ST=Bavaria/L=Munich/O=Mixed-Mode/OU=BA-MitM-IoT/CN=CA/emailAddress=mitm@mixed-mode.de' \
    -out CSR.csr 
    openssl req -out CSR.csr -new -newkey rsa:2048 -nodes -keyout privateKey.key

# openssl req -config openssl.cnf \
      -key private/ca.key.pem \
      -new -x509 -days 7300 -sha256 -extensions v3_ca \
      -out certs/ca.cert.pem

# 3. Sign the CSR with the CA
    openssl req -x509 -days 3650 -sha256 \
    -in CSR.csr -key CA_private.pem \
    -out CA.crt
#   -CAcreateserial \

# 1-3. Root CA - self signed cert with corresponding private key
    openssl req \
    -x509 -nodes -days 3650 -sha256 \
    -subj '/C=DE/ST=Bavaria/L=Munich/O=Mixed-Mode/OU=EmbdSec/CN=BA-MitM-IoT/emailAddress=mitm@mixed-mode.de' \
    -newkey rsa:2048 -keyout CA_private.pem \
    -out CA_cert.crt


# Generate Certificate Revocation List
    -gencrl -out intermediate/crl/intermediate.crl.pem

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
