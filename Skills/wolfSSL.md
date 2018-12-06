# Mutual Authentification
wolfSSL_CTX_set_verify(ctx, WOLFSSL_VERIFY_PEER, 0)
### für ECC: HAVE_ECC als Kompiler Flag

mbedtls_ssl_conf_own_cert( &conf, &cert, &key)
### Client verwendet 'Unknown CA' in cert
