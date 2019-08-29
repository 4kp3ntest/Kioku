from scapy.all import *
from scapy_ssl_tls.ssl_tls import *
from scapy_ssl_tls.ssl_tls_registry import TLS_CIPHER_SUITE_REGISTRY
import socket
import sys, os
import select

default_cipher = [TLSCipherSuite.ECDHE_RSA_WITH_AES_128_CBC_SHA,
                  TLSCipherSuite.ECDHE_RSA_WITH_AES_256_CBC_SHA,
                  TLSCipherSuite.ECDHE_RSA_WITH_AES_128_CBC_SHA256,
                  TLSCipherSuite.ECDHE_RSA_WITH_AES_128_GCM_SHA256,
                  TLSCipherSuite.ECDHE_RSA_WITH_AES_256_CBC_SHA384,
                  TLSCipherSuite.ECDHE_RSA_WITH_AES_256_GCM_SHA384,
                  ]
cipher = [TLSCipherSuite.DHE_RSA_WITH_AES_256_GCM_SHA384,
          TLSCipherSuite.DHE_RSA_WITH_DES_CBC_SHA,
          TLSCipherSuite.DHE_RSA_WITH_AES_128_CBC_SHA]
local_ip = '192.168.10.1'
target1 = ('192.168.10.52', 11110)
target2 = ('192.168.10.50', 4433)
dtls12 = 65278 #DTLS1.2
dtls10 = 65279 #DTLS1.0
rand = os.urandom(28)

close_notify = DTLSRecord(content_type=0x15) / Raw(load=552)
client_hello = DTLSRecord(sequence=0x00, version=dtls10) / DTLSHandshake(sequence=0x00, fragment_offset=0) / \
               DTLSClientHello(cipher_suites=cipher, compression_methods=0x00, random_bytes=rand)


def create_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((local_ip, random.randint(1000, 65000)))
    return s


def send_client_hello(s, target, msg):
    # TODO add retry
    s.sendto(str(msg), target)
    raw = s.recv(128)
    # TODO try execpt
    cookie_raw = get_cookie(DTLSRecord(raw))
    cookie_length = len(cookie_raw)
    msg.cookie = cookie_raw
    msg.cookie_length = cookie_length
    s.sendto(str(msg), target)
    return s

def send_client_keyexchange():
    pass

def get_cookie(msg):
    return msg[Raw].load[3:]

def connection_timed_out():
    print('[*] Connection timed out')
    sys.exit()

def check_for_alert(msg):
    if msg.content_type == 21: #alert
        print('[*] Peer send alert - handshake failed')
        sys.exit()

def wait_for_response(sock, buffsize=2048, timeout=.02):
    sock.setblocking(0)
    ready = select.select([sock], [], [], timeout)
    if ready[0]:
        ret = sock.recv(buffsize)
    else:
        connection_timed_out()
    return ret


class DTLSSocket(object):

    def __init__(self, target, client=True, tls_ctx=None):
        self.client = client
        self.target = target

        try:
            self._s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        except Exception as err:
            print('[!] Cannot create socket')
            print(err)

        if tls_ctx is None:
            import scapy_ssl_tls.ssl_tls_crypto as tlsc
            self.tls_ctx = tlsc.TLSSessionCtx(self.client)
        else:
            self.tls_ctx = tls_ctx
        self.ctx = self.tls_ctx.client_ctx if self.client else self.tls_ctx.server_ctx
        self.compress_hook = None
        self.pre_encrypt_hook = None
        self.encrypt_hook = None

    #   def _get_pkt_origin(self, direction=None):
    #       if direction=='in':
    #           return 'server' if self.client else 'client'
    #       elif direction=='out':
    #           return 'client' if self.client else 'server'

    def sendall(self, pkt, timeout=2):
        prev_timeout = self._s.gettimeout()
        self._s.settimeout(timeout)
        if self.ctx.must_encrypt:
            #TODO
            self._s.sendall(str(tls_to_raw(pkt, self.tls_ctx, True, self.compress_hook, self.pre_encrypt_hook, self.encrypt_hook)))
        else:
            self._s.sendto(str(pkt), self.target)
        #       self.tls_ctx.insert(pkt, self._get_pkt_origin('out'))
        self._s.settimeout(prev_timeout)

    def recvall(self, size=8192, timeout=0.5):
        resp = []
        prev_timeout = self._s.gettimeout()
        self._s.settimeout(timeout)
        while True:
            try:
                data = self._s.recv(size)
                if not data:
                    break
                resp.append(DTLSRecord(data))
            except socket.timeout:
                break
        self._s.settimeout(prev_timeout)
        return resp

#   def __enter__(self):
#       return self

#   def __exit__(self, exc_type, exc_val, exc_tb):
#       self.close()

#   def do_handshake(self, version, ciphers, extensions=[]):
#       return tls_do_handshake(self, version, ciphers, extensions)

#   def do_round_trip(self, pkt, recv=True):
#       return tls_do_round_trip(self, pkt, recv)
class TLSClientHello(PacketNoPayload):
    name = "TLS Client Hello"
    fields_desc = [XShortEnumField("version", TLSVersion.TLS_1_2, TLS_VERSIONS),
                   IntField("gmt_unix_time", int(time.time())),
                   StrFixedLenField("random_bytes", os.urandom(28), 28),
                   XFieldLenField("session_id_length", None, length_of="session_id", fmt="B"),
                   StrLenField("session_id", '', length_from=lambda x:x.session_id_length),
                   XFieldLenField("cipher_suites_length", None, length_of="cipher_suites", fmt="H"),
                   ReprFieldListField("cipher_suites", [TLSCipherSuite.RSA_WITH_AES_128_CBC_SHA], XShortEnumField("cipher", None, TLS_CIPHER_SUITES),
                                      length_from=lambda x: x.cipher_suites_length),
                   XFieldLenField("compression_methods_length", None, length_of="compression_methods", fmt="B"),
                   ReprFieldListField("compression_methods", [TLSCompressionMethod.NULL],
                                      ByteEnumField("compression", None, TLS_COMPRESSION_METHODS),
                                      length_from=lambda x:x.compression_methods_length),
                   StrConditionalField(XFieldLenField("extensions_length", None, length_of="extensions", fmt="H"),
                                       lambda pkt, s, val: True if val or pkt.extensions or (s and struct.unpack("!H", s[:2])[0] == len(s) - 2) else False),
                   TypedPacketListField("extensions", None, TLSExtension, length_from=lambda x:x.extensions_length, type_="TLSClientHello")]

class DTLSClientHello(PacketNoPayload):
    name = "DTLS Client Hello"
    fields_desc = [XShortEnumField("version", TLSVersion.DTLS_1_0, TLS_VERSIONS),
                   IntField("gmt_unix_time", int(time.time())),
                   StrFixedLenField("random_bytes", os.urandom(28), 28),
                   XFieldLenField("session_id_length", None, length_of="session_id", fmt="B"),
                   StrLenField("session_id", '', length_from=lambda x:x.session_id_length),
                   XFieldLenField("cookie_length", None, length_of="cookie", fmt="B"),
                   StrLenField("cookie", '', length_from=lambda x:x.cookie_length),
                   XFieldLenField("cipher_suites_length", None, length_of="cipher_suites", fmt="H"),
                   ReprFieldListField("cipher_suites", None, XShortEnumField("cipher", None, TLS_CIPHER_SUITES),
                                      length_from=lambda x:x.cipher_suites_length),
                   XFieldLenField("compression_methods_length", None, length_of="compression_methods", fmt="B"),
                   ReprFieldListField("compression_methods", None,
                                      ByteEnumField("compression", None, TLS_COMPRESSION_METHODS),
                                      length_from=lambda x:x.compression_methods_length),
                   StrConditionalField(XFieldLenField("extensions_length", None, length_of="extensions", fmt="H"),
                                       lambda pkt, s, val: True if val or
                                                                   pkt.extensions or
                                                                   (s and struct.unpack("!H", s[:2])[0] == len(s) - 2)
                                       else False),
                   PacketListField("extensions", None, TLSExtension, length_from=lambda x:x.extensions_length)]

class TLSServerHello(PacketNoPayload):
    name = "TLS Server Hello"
    fields_desc = [XShortEnumField("version", TLSVersion.TLS_1_2, TLS_VERSIONS),
                   # TLS 1.2: TLS 1.3 random does not start by a timestamp
                   ConditionalField(IntField("gmt_unix_time", int(time.time())), lambda pkt: pkt.version < TLSVersion.TLS_1_3),
                   ConditionalField(StrFixedLenField("random_bytes", os.urandom(28), 28), lambda pkt: pkt.version < TLSVersion.TLS_1_3),
                   # TLS 1.3 random is 32 random bytes only
                   ConditionalField(StrFixedLenField("random", os.urandom(32), 32), lambda pkt: pkt.version >= TLSVersion.TLS_1_3),
                   # Fields are not in TLS 1.3, moved to a proper psk extension
                   ConditionalField(XFieldLenField("session_id_length", None, length_of="session_id", fmt="B"), lambda pkt: pkt.version < TLSVersion.TLS_1_3),
                   ConditionalField(StrLenField("session_id", os.urandom(20), length_from=lambda x:x.session_id_length),
                                    lambda pkt: pkt.version < TLSVersion.TLS_1_3),
                   XShortEnumField("cipher_suite", TLSCipherSuite.RSA_WITH_AES_128_CBC_SHA, TLS_CIPHER_SUITES),
                   # Field deprecated in TLS 1.3
                   ConditionalField(ByteEnumField("compression_method", TLSCompressionMethod.NULL, TLS_COMPRESSION_METHODS),
                                    lambda pkt: pkt.version < TLSVersion.TLS_1_3),
                   StrConditionalField(XFieldLenField("extensions_length", None, length_of="extensions", fmt="H"),
                                       lambda pkt, s, val: True if val or pkt.extensions or (s and struct.unpack("!H", s[:2])[0] == len(s) - 2) else False),
                   TypedPacketListField("extensions", None, TLSExtension, length_from=lambda x:x.extensions_length, type_="TLSServerHello")]

class DTLSServerHello(PacketNoPayload):
    name = "DTLS Server Hello"
    fields_desc = [XShortEnumField("version", TLSVersion.DTLS_1_1, TLS_VERSIONS),
                   IntField("gmt_unix_time", int(time.time())),
                   StrFixedLenField("random_bytes", os.urandom(28), 28),
                   XFieldLenField("session_id_length", None, length_of="session_id", fmt="B"),
                   StrLenField("session_id", os.urandom(20), length_from=lambda x:x.session_id_length),
                   XShortEnumField("cipher_suite", TLSCipherSuite.RSA_WITH_AES_128_CBC_SHA, TLS_CIPHER_SUITES),
                   ByteEnumField("compression_method", TLSCompressionMethod.NULL, TLS_COMPRESSION_METHODS),
                   StrConditionalField(XFieldLenField("extensions_length", None, length_of="extensions", fmt="H"),
                                       lambda pkt, s, val: True if val or pkt.extensions or (s and struct.unpack("!H", s[:2])[0] == len(s) - 2) else False),
                   TypedPacketListField("extensions", None, TLSExtension, length_from=lambda x:x.extensions_length, type_="TLSServerHello")]
