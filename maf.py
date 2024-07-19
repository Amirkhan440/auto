import os

# Set the SSL_CERT_FILE environment variable for Python SSL verification
os.environ['SSL_CERT_FILE'] = '/data/data/com.termux/files/usr/etc/tls/certs/proxy-ca-cert.pem'

# Set the CURL_CA_BUNDLE environment variable for curl SSL verification
os.environ['CURL_CA_BUNDLE'] = '/data/data/com.termux/files/usr/etc/tls/certs/proxy-ca-cert.pem'

# Ensure the binary has execute permissions
import faraziid
