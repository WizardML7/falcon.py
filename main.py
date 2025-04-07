import falcon
sk = falcon.SecretKey(2)
pk = falcon.PublicKey(sk)

print(sk)
print(pk)

sig = sk.sign(b"H")

print(pk.verify(b"H", sig))