FROM x86:openSSL


WORKDIR /root
RUN wget https://www.openssl.org/source/openssl-1.0.1a.tar.gz && \
    tar xvfz openssl-1.0.1a.tar.gz && \
    cd openssl-1.0.1a && \
    ./config && \
    make && \
    make install

# create alias to use just installed openSSL version
RUN echo 'alias openssl="/usr/local/ssl/bin/openssl"' >> ~/.bashrc
